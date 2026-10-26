"""Scene descriptor shape evidence only; no compiler, loader or mover proof."""
from copy import deepcopy
import json
from pathlib import Path
import unittest

from jsonschema import Draft202012Validator
from referencing import Registry, Resource


ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "docs/phase-1-3d/scene-descriptor.schema.json"
PUBLICATION = ROOT / "docs/phase-1-architecture/contracts/publication-manifest.schema.json"


def synthetic_area(area_id, role="traversable"):
    """Handwritten contract fixture; coordinates are not production dimensions."""
    area = {
        "area_id": area_id,
        "geometry_revision": "synthetic-geometry",
        "role": role,
        "placement": {"translation": [0, 0, 0], "rotation": [0, 0, 0, 1], "scale": [1, 1, 1]},
        "bounds": {"min": [-1, -1, -1], "max": [1, 1, 1]},
        "bundle": {
            "variant_id": "synthetic-variant",
            "placement_revision": "synthetic-placement",
            "interpretation_artifact_id": "synthetic-interpretation",
            "visual_artifact_ids": ["synthetic-visual"],
            "collision_artifact_ids": ["synthetic-collision"],
            "panel_artifact_ids": ["synthetic-panels"],
        },
        "anchors": [
            {"anchor_id": "entry", "purpose": "safe_entry", "pose": {"translation": [0, 0, 0], "rotation": [0, 0, 0, 1]}},
            {"anchor_id": "crossing", "purpose": "crossing_endpoint", "pose": {"translation": [0, 0, 0], "rotation": [0, 0, 0, 1]}},
            {"anchor_id": "panel", "purpose": "semantic_interaction", "pose": {"translation": [0, 0, 0], "rotation": [0, 0, 0, 1]},
             "destination_key": "synthetic-destination", "route_id": "synthetic-route",
             "node_binding": {"artifact_id": "synthetic-visual", "node_index": 0}},
        ],
        "optional_details": [{"artifact_id": "synthetic-detail", "interpretation_artifact_id": "synthetic-interpretation",
                              "bounds": {"min": [-1, -1, -1], "max": [1, 1, 1]}}],
    }
    if role == "scenery":
        area["bundle"]["collision_artifact_ids"] = []
        area["bundle"]["panel_artifact_ids"] = []
        area["anchors"] = []
    return area


def synthetic_descriptor():
    return {
        "schema_version": 1,
        "release_id": "synthetic-release",
        "stream": "S-HIGH",
        "coordinate_frame": "gltf_y_up_meters",
        "areas": [synthetic_area("area-a"), synthetic_area("area-b"), synthetic_area("distant", "scenery")],
        "connections": [
            {"connection_id": "a-to-b", "source": {"area_id": "area-a", "anchor_id": "crossing"},
             "target": {"area_id": "area-b", "anchor_id": "crossing"}, "threshold_destination_keys": ["synthetic-destination"]},
        ],
        "destinations": [
            {"destination_key": "synthetic-destination", "route_id": "synthetic-route",
             "safe_entry": {"area_id": "area-b", "anchor_id": "entry"}, "interactions": [{"area_id": "area-b", "anchor_id": "panel"}]},
            {"destination_key": "synthetic-semantic-only", "route_id": "synthetic-semantic-route", "safe_entry": None, "interactions": []},
        ],
    }


class SceneDescriptorShapeTests(unittest.TestCase):
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

    def assert_valid_shape(self, descriptor):
        self.assertEqual(list(self.validator.iter_errors(descriptor)), [])

    def assert_invalid_shape(self, descriptor):
        self.assertTrue(list(self.validator.iter_errors(descriptor)))

    def test_three_3d_streams_traversable_scenery_and_semantic_only_mapping(self):
        for stream in ("S-HIGH", "S-MEDIUM", "S-LOW"):
            with self.subTest(stream=stream):
                descriptor = synthetic_descriptor()
                descriptor["stream"] = stream
                self.assert_valid_shape(descriptor)
        descriptor = synthetic_descriptor()
        descriptor["connections"].append({
            "connection_id": "b-to-a", "source": {"area_id": "area-b", "anchor_id": "crossing"},
            "target": {"area_id": "area-a", "anchor_id": "crossing"}, "threshold_destination_keys": [],
        })
        self.assert_valid_shape(descriptor)

    def test_closed_records_exclude_private_authority_urls_and_audio(self):
        additions = (
            ((), "manifest_sha256", "0" * 64),
            ((), "staff_email", "synthetic@example.invalid"),
            ((), "approved", True),
            (("areas", 0), "asset_url", "https://example.invalid/model.glb"),
            (("areas", 0, "bundle"), "audio_artifact_ids", ["synthetic-audio"]),
            (("areas", 0, "placement"), "matrix", [1] * 16),
            (("areas", 0, "anchors", 0), "booking_token", "synthetic-only"),
            (("connections", 0), "open", True),
            (("destinations", 0), "staff_online", True),
        )
        for path, key, value in additions:
            with self.subTest(path=path, key=key):
                descriptor = synthetic_descriptor()
                target = descriptor
                for part in path:
                    target = target[part]
                target[key] = value
                self.assert_invalid_shape(descriptor)

    def test_area_roles_require_ground_and_entry_and_exclude_scenery_anchors(self):
        changes = (
            (("areas", 0, "bundle", "visual_artifact_ids"), []),
            (("areas", 0, "bundle", "collision_artifact_ids"), []),
            (("areas", 0, "anchors"), []),
            (("areas", 0, "anchors", 0, "purpose"), "crossing_endpoint"),
            (("areas", 2, "bundle", "collision_artifact_ids"), ["synthetic-collision"]),
            (("areas", 2, "bundle", "panel_artifact_ids"), ["synthetic-panels"]),
            (("areas", 2, "anchors"), [deepcopy(synthetic_area("unused")["anchors"][0])]),
        )
        for path, value in changes:
            with self.subTest(path=path):
                descriptor = synthetic_descriptor()
                target = descriptor
                for part in path[:-1]:
                    target = target[part]
                target[path[-1]] = value
                self.assert_invalid_shape(descriptor)
        for key in ("destination_key", "route_id"):
            with self.subTest(missing_interaction_binding=key):
                descriptor = synthetic_descriptor()
                del descriptor["areas"][0]["anchors"][2][key]
                self.assert_invalid_shape(descriptor)

    def test_identifier_numeric_and_field_boundaries(self):
        changes = (
            (("schema_version",), 2),
            (("stream",), "S-SEMANTIC"),
            (("coordinate_frame",), "blender_z_up"),
            (("release_id",), "synthetic-release\n"),
            (("areas",), []),
            (("areas", 0, "placement", "translation"), [0, 0]),
            (("areas", 0, "placement", "rotation"), [0, 0, 1]),
            (("areas", 0, "placement", "scale"), [1, 0, 1]),
            (("areas", 0, "bounds", "max"), [True, 1, 1]),
            (("areas", 0, "bounds", "max"), [float("inf"), 1, 1]),
            (("areas", 0, "anchors", 2, "node_binding", "node_index"), -1),
            (("areas", 0, "anchors", 2, "node_binding", "node_index"), 9007199254740992),
            (("areas", 0, "bundle", "visual_artifact_ids"), ["synthetic-visual", "synthetic-visual"]),
            (("areas", 0, "bundle", "interpretation_artifact_id"), "../private"),
            (("connections", 0, "source", "anchor_id"), None),
            (("destinations", 0, "interactions"), None),
        )
        for path, value in changes:
            with self.subTest(path=path, value=value):
                descriptor = synthetic_descriptor()
                target = descriptor
                for part in path[:-1]:
                    target = target[part]
                target[path[-1]] = value
                self.assert_invalid_shape(descriptor)
        for key in ("release_id", "connections", "destinations"):
            with self.subTest(missing=key):
                descriptor = synthetic_descriptor()
                del descriptor[key]
                self.assert_invalid_shape(descriptor)


if __name__ == "__main__":
    unittest.main()
