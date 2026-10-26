"""Prospective offline library cases; run only in the approved new trial environment."""
import importlib.util

import pytest
import yaml
from fastapi import FastAPI
from uvicorn import Config


def test_yaml_uses_the_explicit_pure_python_build():
    assert yaml.__version__ == "6.0.3"
    assert yaml.__with_libyaml__ is False
    assert importlib.util.find_spec("yaml._yaml") is None


def test_yaml_parses_declared_mapping_and_unicode():
    assert yaml.safe_load("kind: synthetic\nlabel: '森林'\ncount: 7\n") == {
        "kind": "synthetic", "label": "森林", "count": 7}


def test_yaml_emission_can_be_read_without_losing_values():
    output = yaml.safe_dump({"kind": "synthetic", "enabled": True, "values": [1, 2]},
                            allow_unicode=True)
    assert yaml.safe_load(output) == {"kind": "synthetic", "enabled": True, "values": [1, 2]}


def test_yaml_malformed_input_is_rejected():
    with pytest.raises(yaml.YAMLError):
        yaml.safe_load("values: [unterminated\n")


def test_yaml_safe_loader_rejects_python_object_tags():
    with pytest.raises(yaml.constructor.ConstructorError):
        yaml.safe_load('!!python/object/apply:builtins.eval ["1 + 1"]')


def test_uvicorn_yaml_configuration_and_httptools_load_without_listener(tmp_path):
    path = tmp_path / "synthetic-logging.yaml"
    path.write_text("version: 1\ndisable_existing_loggers: false\nhandlers: {}\n"
                    "root:\n  level: WARNING\n  handlers: []\n", encoding="utf-8")
    config = Config(FastAPI(), loop="asyncio", http="httptools", ws="none",
                    lifespan="off", log_config=str(path), access_log=False)
    config.load()
    assert config.loaded
    assert config.http_protocol_class.__module__ == "uvicorn.protocols.http.httptools_impl"
    # Configuration/import only. No listener, request parser traffic or Hengshi API proof.
