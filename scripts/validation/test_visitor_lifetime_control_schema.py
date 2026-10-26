"""Lifetime control representations only; no expiry, ownership or End runtime proof."""
import copy
import json
import unittest

from jsonschema import Draft202012Validator
from referencing import Resource

from scripts.validation import test_booking_creation_request_schema as fixture


class VisitorLifetimeControlShapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        base = fixture.BookingCreationRequestShapeTests
        base.setUpClass()
        registry = base.registry
        for name in ('booking-creation-response.schema.json', 'chat-event-control.schema.json',
                     'visitor-lifetime-control.schema.json'):
            path = fixture.CONTRACTS / name
            schema = json.loads(path.read_text(encoding='utf-8'))
            Draft202012Validator.check_schema(schema)
            registry = registry.with_resource(path.as_uri(), Resource.from_contents(schema))
        cls.validators = {
            direction: Draft202012Validator({'$ref': path.as_uri() + '#/$defs/' + direction},
                                             registry=registry, format_checker=base.checker)
            for direction in ('client', 'server')
        }
        cls.module = Draft202012Validator({'$ref': path.as_uri()}, registry=registry)

    channel = '9c3567ad-12bf-4b3a-a76d-7e56b9dfe051'
    stream = '919108f7-52d1-4320-9bac-f847db4148a8'
    operation = '10286f82-cad4-4b14-a76a-e60d6c09ca09'

    def header(self, kind):
        return {'protocol_version': 1, 'kind': kind,
                'channel_id': self.channel, 'stream_id': self.stream}

    def command(self, kind):
        value = {**self.header(kind), 'operation_id': self.operation, 'command_revision': 1}
        if kind == 'extend_idle':
            value['expected_lifetime_revision'] = 3
        return value

    def lifetime(self):
        return {'lifetime_revision': 3, 'server_time_ms': 1791336000000,
                'idle_deadline_ms': 1791337800000}

    def admission(self):
        ticket = {'operation_id': self.operation, 'command_revision': 1}
        return {**self.header('lifetime_admission'), 'proof_generation': 2,
                'lifetime': self.lifetime(), 'renewal_ticket': ticket,
                'ending_ticket': {**ticket, 'operation_id': self.channel}}

    def extension_result(self, state='applied'):
        value = {**self.command('reconcile_idle_extension'),
                 'kind': 'idle_extension_result', 'state': state}
        if state != 'pending':
            value['lifetime'] = self.lifetime()
        if state == 'applied':
            value.update(applied_lifetime_revision=3, applied_deadline_ms=1791337800000)
        elif state == 'not_applied':
            value['code'] = 'stale_ticket'
        return value

    def valid(self, direction, value):
        return self.validators[direction].is_valid(value)

    def test_closed_directions_do_not_allow_client_forged_success_or_server_commands(self):
        for kind in ('extend_idle', 'reconcile_idle_extension', 'end_conversation', 'reconcile_end'):
            value = self.command(kind)
            self.assertTrue(self.valid('client', value))
            self.assertFalse(self.valid('server', value))
            self.assertFalse(self.module.is_valid(value))
        for value in (self.admission(), self.extension_result(), self.extension_result('pending'),
                      self.extension_result('not_applied'),
                      {**self.command('reconcile_end'), 'kind': 'end_result', 'state': 'ended'}):
            self.assertTrue(self.valid('server', value))
            self.assertFalse(self.valid('client', value))
            self.assertFalse(self.module.is_valid(value))

    def test_untrusted_duration_role_history_and_cross_process_selectors_are_excluded(self):
        for direction, value in (('client', self.command('extend_idle')),
                                 ('client', self.command('end_conversation')),
                                 ('server', self.admission())):
            for key in ('duration_ms', 'server_time_ms', 'idle_deadline_ms', 'role',
                        'staff_id', 'session_id', 'consent', 'retention_days', 'history', 'cookie'):
                self.assertFalse(self.valid(direction, {**value, key: 'forbidden'}))
        self.assertFalse(self.valid('server', {
            **self.command('reconcile_end'), 'kind': 'end_result', 'state': 'ended',
            'deleted': True, 'booking_cancelled': True}))
        for key in self.command('end_conversation'):
            value = self.command('end_conversation')
            del value[key]
            self.assertFalse(self.valid('client', value))

    def test_result_branches_cannot_turn_pending_into_a_clock_or_completed_effect(self):
        pending = self.extension_result('pending')
        for key, value in (('lifetime', self.lifetime()), ('applied_lifetime_revision', 3),
                           ('applied_deadline_ms', 1791337800000), ('code', 'stale_ticket')):
            self.assertFalse(self.valid('server', {**pending, key: value}))
        for key in ('lifetime', 'applied_lifetime_revision', 'applied_deadline_ms'):
            value = self.extension_result()
            del value[key]
            self.assertFalse(self.valid('server', value))
        self.assertFalse(self.valid('server', {**self.extension_result('not_applied'),
                                               'applied_lifetime_revision': 3}))
        for state in ('cancelled', 'deleted', 'closed_socket', 'confirmed', 'applied'):
            value = {**self.command('reconcile_end'), 'kind': 'end_result', 'state': state}
            self.assertFalse(self.valid('server', value))

    def test_exact_integer_bounds_and_shape_only_temporal_limit(self):
        for key in ('server_time_ms', 'idle_deadline_ms'):
            for value in (-1, True, 0.5, '1791336000000', 9007199254740992):
                invalid = copy.deepcopy(self.admission())
                invalid['lifetime'][key] = value
                self.assertFalse(self.valid('server', invalid))
        for value in (0, True, '3', 9007199254740992):
            invalid = self.command('extend_idle')
            invalid['expected_lifetime_revision'] = value
            self.assertFalse(self.valid('client', invalid))
        # JSON Schema does not compare two instance properties or prove current authority.
        # The actual coordinator must reject this impossible active snapshot later.
        reversed_clock = self.admission()
        reversed_clock['lifetime']['idle_deadline_ms'] = 1
        self.assertTrue(self.valid('server', reversed_clock))


if __name__ == '__main__':
    unittest.main()
