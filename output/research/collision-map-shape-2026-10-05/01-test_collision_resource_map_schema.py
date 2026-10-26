"""Collision-map shape tooling only; no GLB inspection or mover safety proof."""
from copy import deepcopy
import json
from pathlib import Path
import unittest

from jsonschema import Draft202012Validator
from referencing import Registry, Resource


ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "docs/phase-1-3d/collision-resource-map.schema.json"
PUBLICATION = ROOT / "docs/phase-1-architecture/contracts/publication-manifest.schema.json"


def synthetic_map():
    return {
        "schema_version": 1,
        "release_id": "synthetic-release",
        "stream": "S-HIGH",
        "client_build_sha256": "a" * 64,
        "collision_profile_id": "synthetic-collision-profile",
        "models": [{
            "artifact_id": "synthetic-collision", "container": "GLB", "gltf_version": "2.0",
            "scene_index": 0,
            "primitives": [
                {"node_index": 0, "primitive_index": 0, "purpose": "ground_candidate"},
                {"node_index": 1, "primitive_index": 0, "purpose": "barrier"},
            ],
        }],
    }


class CollisionResourceMapShapeTests(unittest.TestCase):
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

    def test_three_streams_and_explicit_placed_primitive_inventory(self):
        for stream in ("S-HIGH", "S-MEDIUM", "S-LOW"):
            with self.subTest(stream=stream):
                record = synthetic_map()
                record["stream"] = stream
                self.assert_shape(record, True)
        record = synthetic_map()
        record["models"][0]["primitives"].append(
            {"node_index": 0, "primitive_index": 1, "purpose": "barrier"},
        )
        second = deepcopy(record["models"][0])
        second["artifact_id"] = "synthetic-second-collision"
        record["models"].append(second)
        self.assert_shape(record, True)  # exact mesh/scene coverage still needs actual bytes

    def test_required_fields_and_closed_public_objects(self):
        for path in ((), ("models", 0), ("models", 0, "primitives", 0)):
            original = synthetic_map()
            target = original
            for key in path:
                target = target[key]
            for field in tuple(target):
                with self.subTest(path=path, missing=field):
                    record = deepcopy(original)
                    item = record
                    for key in path:
                        item = item[key]
                    del item[field]
                    self.assert_shape(record, False)
            for field in ("url", "script", "options", "staff_id", "room_permission",
                          "external_resources", "decoder_artifact_ids", "transform", "vertices"):
                with self.subTest(path=path, extra=field):
                    record = deepcopy(original)
                    item = record
                    for key in path:
                        item = item[key]
                    item[field] = "synthetic"
                    self.assert_shape(record, False)

    def test_release_build_profile_format_and_inventory_boundaries(self):
        for field, value in (("schema_version", True), ("schema_version", 2),
                             ("stream", "S-SEMANTIC"), ("release_id", ""),
                             ("release_id", "release\n"), ("collision_profile_id", "profile/path"),
                             ("collision_profile_id", "profile\n"),
                             ("client_build_sha256", "A" * 64),
                             ("client_build_sha256", "a" * 64 + "\n"), ("models", [])):
            with self.subTest(field=field, value=value):
                record = synthetic_map()
                record[field] = value
                self.assert_shape(record, False)
        for field, value in (("artifact_id", "collision/path"), ("container", "gltf_json"),
                             ("container", "fbx"), ("gltf_version", "3.0"), ("primitives", [])):
            with self.subTest(field=field, value=value):
                record = synthetic_map()
                record["models"][0][field] = value
                self.assert_shape(record, False)
        for purpose in ("walkable", "permission", "Ground", "ground_candidate\n", ""):
            record = synthetic_map()
            record["models"][0]["primitives"][0]["purpose"] = purpose
            self.assert_shape(record, False)

    def test_safe_integer_selectors_and_exact_record_duplicates(self):
        for path in (("models", 0, "scene_index"),
                     ("models", 0, "primitives", 0, "node_index"),
                     ("models", 0, "primitives", 0, "primitive_index")):
            for value in (-1, True, "0", 0.5, 9007199254740992):
                with self.subTest(path=path, value=value):
                    record = synthetic_map()
                    item = record
                    for key in path[:-1]:
                        item = item[key]
                    item[path[-1]] = value
                    self.assert_shape(record, False)
        for path in (("models",), ("models", 0, "primitives")):
            record = synthetic_map()
            items = record
            for key in path:
                items = items[key]
            items.append(deepcopy(items[0]))
            self.assert_shape(record, False)

    def test_shape_does_not_prove_key_uniqueness_or_semantic_binding(self):
        record = synthetic_map()
        duplicate_model = deepcopy(record["models"][0])
        duplicate_model["scene_index"] = 1
        record["models"].append(duplicate_model)
        self.assert_shape(record, True)  # actual inspector must reject repeated artifact_id
        record = synthetic_map()
        duplicate_primitive = deepcopy(record["models"][0]["primitives"][0])
        duplicate_primitive["purpose"] = "barrier"
        record["models"][0]["primitives"].append(duplicate_primitive)
        self.assert_shape(record, True)  # same node/primitive pair: whole objects differ
        record = synthetic_map()
        record["models"][0]["primitives"][0]["node_index"] = 9007199254740991
        record["release_id"] = "synthetic-other-release"
        record["collision_profile_id"] = "synthetic-unregistered-profile"
        self.assert_shape(record, True)  # no GLB, envelope, compiled registry or context exists


if __name__ == "__main__":
    unittest.main()
