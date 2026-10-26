"""Resource-map shape tooling only; no actual glTF or loader enforcement proof."""
from copy import deepcopy
import json
from pathlib import Path
import unittest

from jsonschema import Draft202012Validator
from referencing import Registry, Resource


ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "docs/phase-1-3d/gltf-resource-map.schema.json"
PUBLICATION = ROOT / "docs/phase-1-architecture/contracts/publication-manifest.schema.json"


def synthetic_map():
    return {
        "schema_version": 1,
        "release_id": "synthetic-release",
        "stream": "S-HIGH",
        "client_build_sha256": "a" * 64,
        "profile_id": "synthetic-profile",
        "models": [{
            "artifact_id": "synthetic-model", "container": "GLB", "gltf_version": "2.0",
            "scene_index": 0, "extensions_used": [], "extensions_required": [],
            "external_resources": [{
                "uri": "textures/leaf.base.png", "artifact_id": "synthetic-image",
                "uses": [{"location": "/images/0/uri", "usage": "image"}],
            }],
            "decoder_artifact_ids": [],
        }],
    }


class GltfResourceMapShapeTests(unittest.TestCase):
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

    def test_core_containers_streams_and_complete_embedded_shape(self):
        for stream in ("S-HIGH", "S-MEDIUM", "S-LOW"):
            for container in ("GLB", "gltf_json"):
                with self.subTest(stream=stream, container=container):
                    record = synthetic_map()
                    record["stream"] = stream
                    record["models"][0]["container"] = container
                    self.assert_shape(record, True)
        record = synthetic_map()
        record["models"][0]["external_resources"] = []
        self.assert_shape(record, True)
        record = synthetic_map()
        model = record["models"][0]
        model["extensions_used"] = ["KHR_texture_basisu"]
        model["extensions_required"] = ["KHR_texture_basisu"]
        model["decoder_artifact_ids"] = ["synthetic-decoder"]
        model["external_resources"][0]["uses"] = [
            {"location": "/images/0/uri", "usage": "image"},
            {"location": "/extensions/VENDOR_synthetic/uri", "usage": "extension"},
        ]
        self.assert_shape(record, True)  # no selected support or byte verification follows

    def test_uri_subset_blocks_uncontrolled_sources_and_normalization_aliases(self):
        for uri in ("https://example.com/a.png", "//example.com/a", "/a.png", "../a.png",
                    "a/./b.png", "a/../b.png", "a//b.png", "a/", "a\\b.png",
                    "a%2Fb.png", "a.png?q=x", "a.png#x", "a b.png", "é.png",
                    "data:image/png;base64,AAAA", "blob:synthetic", "a.png\n", ""):
            with self.subTest(uri=uri):
                record = synthetic_map()
                record["models"][0]["external_resources"][0]["uri"] = uri
                self.assert_shape(record, False)

    def test_public_objects_are_closed_and_required_fields_are_explicit(self):
        paths = ((), ("models", 0), ("models", 0, "external_resources", 0),
                 ("models", 0, "external_resources", 0, "uses", 0))
        for path in paths:
            for field in ("url", "script", "options", "staff_id", "approval", "wasm_url"):
                with self.subTest(path=path, field=field):
                    record = synthetic_map()
                    target = record
                    for key in path:
                        target = target[key]
                    target[field] = "synthetic"
                    self.assert_shape(record, False)
        for field in ("client_build_sha256", "profile_id", "models"):
            record = synthetic_map()
            del record[field]
            self.assert_shape(record, False)
        for field in ("scene_index", "external_resources", "decoder_artifact_ids", "extensions_required"):
            record = synthetic_map()
            del record["models"][0][field]
            self.assert_shape(record, False)

    def test_identifier_index_enum_pointer_and_duplicate_shape_boundaries(self):
        for field, value in (("schema_version", True), ("stream", "S-SEMANTIC"),
                             ("client_build_sha256", "A" * 64), ("profile_id", "profile/path"),
                             ("models", [])):
            record = synthetic_map()
            record[field] = value
            self.assert_shape(record, False)
        for field, value in (("scene_index", -1), ("scene_index", True), ("scene_index", 0.5),
                             ("scene_index", 9007199254740992), ("gltf_version", "3.0"),
                             ("container", "fbx"), ("extensions_used", ["KHR_bad\n"]),
                             ("decoder_artifact_ids", ["duplicate", "duplicate"])):
            record = synthetic_map()
            record["models"][0][field] = value
            self.assert_shape(record, False)
        for field, value in (("location", "/images/0/url"), ("location", "/images/~1/uri"),
                             ("usage", "script")):
            record = synthetic_map()
            record["models"][0]["external_resources"][0]["uses"][0][field] = value
            self.assert_shape(record, False)
        record = synthetic_map()
        record["models"].append(deepcopy(record["models"][0]))
        self.assert_shape(record, False)


if __name__ == "__main__":
    unittest.main()
