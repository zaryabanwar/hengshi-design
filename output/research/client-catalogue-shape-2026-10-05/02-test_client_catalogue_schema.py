"""Client catalogue shape evidence; no emitted-build, JCS or runtime proof."""
from copy import deepcopy
import json
from pathlib import Path
import unittest

from jsonschema import Draft202012Validator
from referencing import Registry, Resource


ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "docs/phase-1-architecture/contracts/client-build-catalogue.schema.json"
PUBLICATION = ROOT / "docs/phase-1-architecture/contracts/publication-manifest.schema.json"


def synthetic_unit(unit_id, role="script", gate="semantic"):
    return {
        "unit_id": unit_id, "asset_key": "client/units/" + unit_id + ".bin",
        "sha256": "b" * 64, "bytes": 1, "role": role,
        "media_type": "application/wasm" if role == "decoder_wasm" else "text/javascript",
        "fetch_gate": gate, "required_unit_ids": [], "optional_unit_ids": [],
    }


def synthetic_catalogue():
    core = synthetic_unit("synthetic-core")
    core["optional_unit_ids"] = ["synthetic-world"]
    world = synthetic_unit("synthetic-world", gate="world_entry")
    world["required_unit_ids"] = ["synthetic-core"]
    return {
        "schema_version": 1, "toolchain_lock_sha256": "a" * 64, "build_config_sha256": "c" * 64,
        "units": [core, world],
        "entries": {"semantic": {"activation_gate": "semantic", "unit_ids": ["synthetic-core"]},
                    "world": {"activation_gate": "world_entry", "unit_ids": ["synthetic-world"]}},
        "profiles": [{"profile_id": "synthetic-profile", "gltf_version": "2.0",
                      "base_decoder_unit_ids": [], "extension_rules": []}],
    }


class ClientCatalogueShapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        resources = []
        for path in (SCHEMA, PUBLICATION):
            schema = json.loads(path.read_text(encoding="utf-8"))
            Draft202012Validator.check_schema(schema)
            resources.append((path.as_uri(), Resource.from_contents(schema)))
        cls.validator = Draft202012Validator(
            {"$ref": SCHEMA.as_uri()}, registry=Registry().with_resources(resources),
        )

    def assert_shape(self, record, valid):
        self.assertEqual(not list(self.validator.iter_errors(record)), valid)

    def test_core_visual_profile_optional_audio_and_decoder_shapes(self):
        self.assert_shape(synthetic_catalogue(), True)
        record = synthetic_catalogue()
        record["units"].append(synthetic_unit("synthetic-audio", gate="audio_enablement"))
        record["entries"]["audio"] = {"activation_gate": "audio_enablement", "unit_ids": ["synthetic-audio"]}
        self.assert_shape(record, True)
        record["units"].append(synthetic_unit("synthetic-decoder", "decoder_wasm", "world_entry"))
        record["profiles"][0]["extension_rules"] = [
            {"extension_name": "KHR_texture_basisu", "handling": "interpret", "decoder_unit_ids": ["synthetic-decoder"]},
            {"extension_name": "VENDOR_synthetic", "handling": "ignore_optional", "decoder_unit_ids": []},
        ]
        self.assert_shape(record, True)  # does not select or verify those implementations
        for role in ("style", "image", "font", "worker", "decoder_wrapper"):
            record = synthetic_catalogue()
            record["units"].append(synthetic_unit("synthetic-" + role, role, "world_entry"))
            self.assert_shape(record, True)  # MIME/role agreement remains semantic

    def test_all_nested_public_records_are_closed(self):
        record = synthetic_catalogue()
        record["profiles"][0]["extension_rules"] = [
            {"extension_name": "VENDOR_synthetic", "handling": "ignore_optional", "decoder_unit_ids": []},
        ]
        paths = ((), ("units", 0), ("entries",), ("entries", "semantic"),
                 ("profiles", 0), ("profiles", 0, "extension_rules", 0))
        for path in paths:
            for field in ("url", "callback", "options", "staff_id", "release_id", "manifest_sha256"):
                with self.subTest(path=path, field=field):
                    candidate = deepcopy(record)
                    target = candidate
                    for key in path:
                        target = target[key]
                    target[field] = "synthetic"
                    self.assert_shape(candidate, False)

    def test_fixed_entry_gates_and_optional_ignore_condition(self):
        for entry, gate in (("semantic", "world_entry"), ("world", "semantic"), ("world", "audio_enablement")):
            record = synthetic_catalogue()
            record["entries"][entry]["activation_gate"] = gate
            self.assert_shape(record, False)
        for entry in ("semantic", "world"):
            record = synthetic_catalogue()
            del record["entries"][entry]
            self.assert_shape(record, False)
            record = synthetic_catalogue()
            record["entries"][entry]["unit_ids"] = []
            self.assert_shape(record, False)
        record = synthetic_catalogue()
        record["profiles"][0]["extension_rules"] = [{
            "extension_name": "VENDOR_synthetic", "handling": "ignore_optional",
            "decoder_unit_ids": ["synthetic-decoder"],
        }]
        self.assert_shape(record, False)

    def test_scalar_identifier_enum_and_duplicate_record_domains(self):
        for field, value in (("schema_version", True), ("toolchain_lock_sha256", "A" * 64),
                             ("build_config_sha256", "c" * 64 + "\n"), ("units", []), ("profiles", [])):
            record = synthetic_catalogue()
            record[field] = value
            self.assert_shape(record, False)
        for field, value in (("bytes", 0), ("bytes", True), ("bytes", 0.5), ("bytes", 9007199254740992),
                             ("unit_id", "unit/path"), ("asset_key", "https://example.com/a"),
                             ("role", "other"), ("fetch_gate", "anytime"), ("media_type", "Text/JavaScript"),
                             ("media_type", "text/javascript; charset=utf-8"), ("media_type", "text/javascript\n"),
                             ("required_unit_ids", ["duplicate", "duplicate"]), ("optional_unit_ids", None)):
            with self.subTest(field=field, value=value):
                record = synthetic_catalogue()
                record["units"][0][field] = value
                self.assert_shape(record, False)
        record = synthetic_catalogue()
        record["units"].append(deepcopy(record["units"][0]))
        self.assert_shape(record, False)
        record = synthetic_catalogue()
        record["profiles"][0]["gltf_version"] = "3.0"
        self.assert_shape(record, False)


if __name__ == "__main__":
    unittest.main()
