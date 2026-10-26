"""Read-only Request.json probes; no ASGI application or production parser implementation."""
import asyncio
import hashlib
import importlib.metadata
import inspect
import json
import math
import sys
from pathlib import Path
from starlette.requests import Request

CASES = [
    ("valid_object", b'{"state":"pending","revision":1}', "raw_syntax_control"),
    ("valid_unicode", '{"text":"Hengshi \U0001f333"}'.encode("utf-8"), "raw_syntax_control"),
    ("valid_surrogate_pair", b'{"text":"\\ud83c\\udf33"}', "raw_syntax_control"),
    ("duplicate", b'{"state":"pending","state":"confirmed"}', "reject_duplicate_names"),
    ("escape_duplicate", b'{"state":1,"\\u0073tate":2}', "reject_duplicate_names"),
    ("nested_duplicate", b'{"context":{"wing":1,"wing":2}}', "reject_duplicate_names"),
    ("nan", b'{"revision":NaN}', "reject_non_json_number"),
    ("infinity", b'{"revision":Infinity}', "reject_non_json_number"),
    ("negative_infinity", b'{"revision":-Infinity}', "reject_non_json_number"),
    ("overflow_exponent", b'{"value":1e400}', "field_numeric_range_or_precision_check"),
    ("underflow_exponent", b'{"value":1e-400}', "field_numeric_range_or_precision_check"),
    ("unsafe_integer", b'{"value":9007199254740993}', "field_numeric_range_or_precision_check"),
    ("unpaired_value", b'{"text":"\\ud800"}', "reject_invalid_unicode_scalar"),
    ("unpaired_key", b'{"\\ud800":1}', "reject_invalid_unicode_scalar"),
    ("utf16", '{"state":"pending"}'.encode("utf-16"), "reject_non_utf8"),
    ("utf32", '{"state":"pending"}'.encode("utf-32"), "reject_non_utf8"),
    ("utf8_bom", b'\xef\xbb\xbf{"state":"pending"}', "reject_bom_project_profile"),
    ("trailing", b'{"state":"pending"}{}', "reject_trailing_data"),
    ("malformed_utf8", b'{"text":"\xff"}', "reject_non_utf8"),
    ("array_root", b'[]', "directional_envelope_check"),
]

async def inspect_case(name, raw, obligation):
    delivered = False
    async def receive():
        nonlocal delivered
        if delivered:
            return {"type":"http.disconnect"}
        delivered = True
        return {"type":"http.request", "body":raw, "more_body":False}
    scope = {"type":"http", "method":"POST", "path":"/synthetic", "headers":[], "query_string":b""}
    row = {"name":name,"raw_hex":raw.hex(),"contract_obligation":obligation}
    try:
        value = await Request(scope, receive=receive).json()
        row["parser_accepted"] = True
        row["root_type"] = type(value).__name__
        # Diagnostic categories only; no private data, normalisation or admission code.
        if name in {"duplicate","escape_duplicate"}:
            row["retained_members"] = len(value)
        if name == "nested_duplicate":
            row["retained_nested_members"] = len(value["context"])
        if name in {"nan","infinity","negative_infinity","overflow_exponent"}:
            row["nonfinite_value"] = not math.isfinite(value.get("revision",value.get("value")))
        if name == "underflow_exponent":
            row["rounded_to_zero"] = value["value"] == 0
        if name == "unsafe_integer":
            row["integer_preserved_by_python"] = value["value"] == 9007199254740993
        if name in {"unpaired_value","unpaired_key"}:
            text = value["text"] if name == "unpaired_value" else next(iter(value))
            row["contains_surrogate"] = any(0xD800 <= ord(c) <= 0xDFFF for c in text)
    except (ValueError, UnicodeDecodeError) as exc:
        row["parser_accepted"] = False
        row["exception_type"] = type(exc).__name__
    return row

async def main():
    source=Path(inspect.getsourcefile(Request.json))
    return {"scope":"native installed Request.json raw parsing only; no actual HTTP endpoint, closed shape, auth, deployment or selected stable graph", "python":sys.version.split()[0], "fastapi":importlib.metadata.version("fastapi"),"starlette":importlib.metadata.version("starlette"),"source_file":str(source),"source_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),"source_line":inspect.getsourcelines(Request.json)[1],"source":inspect.getsource(Request.json),"cases":[await inspect_case(*case) for case in CASES]}

if __name__ == "__main__":
    print(json.dumps(asyncio.run(main()),ensure_ascii=True,indent=2))
