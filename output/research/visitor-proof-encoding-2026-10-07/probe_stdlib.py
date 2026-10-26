"""Read-only installed stdlib observations using public synthetic byte values.

No visitor credential is generated and no Hengshi application boundary runs.
"""
import base64
import binascii
import hashlib
import inspect
import json
import secrets
import sys
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parent
canonical = "A" * 43
noncanonical = "A" * 42 + "B"
standard_alphabet = "/" * 42 + "8"

def strict_library_decode(text):
    return base64.b64decode(text + "=", altchars=b"-_", validate=True)

decoded = strict_library_decode(canonical)
noncanonical_decoded = strict_library_decode(noncanonical)
standard_decoded = strict_library_decode(standard_alphabet)
whitespace_accepted = base64.urlsafe_b64decode(canonical + "\n=") == decoded
try:
    strict_library_decode(canonical + "\n")
except binascii.Error:
    strict_library_rejects_whitespace = True
else:
    strict_library_rejects_whitespace = False

source_records = []
for module in (base64, secrets, hashlib):
    path = Path(module.__file__)
    data = path.read_bytes()
    snapshot = root / (module.__name__ + ".installed.py")
    snapshot.write_bytes(data)
    source_records.append({"module": module.__name__, "observed_path": str(path),
                           "snapshot": snapshot.name, "bytes": len(data),
                           "sha256": hashlib.sha256(data).hexdigest()})

observation = {
    "observed_at": datetime.now(timezone.utc).isoformat(),
    "runtime_observed_not_selected": sys.version,
    "decoder_signature": str(inspect.signature(base64.b64decode)),
    "input_scope": "Public synthetic all-zero and all-one values; no CSPRNG credential generated",
    "canonical_shape": "43 ASCII A characters decode to 32 zero bytes with one internal padding character",
    "canonical_decoded_bytes": len(decoded),
    "strict_decoder_accepts_nonzero_unused_pad_bits": noncanonical_decoded == decoded,
    "strict_decoder_accepts_standard_alphabet_with_urlsafe_altchars": len(standard_decoded) == 32,
    "urlsafe_decoder_discards_whitespace": whitespace_accepted,
    "strict_decoder_rejects_whitespace": strict_library_rejects_whitespace,
    "sha256_digest_bytes": len(hashlib.sha256(decoded).digest()),
    "installed_sources": source_records,
    "limits": "Library observations only; no randomness, constant-time, ingress, credential, store, authorization, expiry or application enforcement proof"
}
(root / "observations.json").write_text(json.dumps(observation, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in observation.items() if k != "installed_sources"}, indent=2))
