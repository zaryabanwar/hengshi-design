"""Execute only within a separately authorized isolated candidate environment."""
import json
from pathlib import Path
import sys
import warnings

# Authlib installs an 'always' filter on first import; initialize before errors.
from authlib.deprecate import AuthlibDeprecationWarning
from starlette.exceptions import StarletteDeprecationWarning

for category in (AuthlibDeprecationWarning, StarletteDeprecationWarning):
    warnings.simplefilter('error', category)
    try:
        warnings.warn('synthetic warning-filter admission probe', category)
    except category:
        pass
    else:
        raise RuntimeError('Required deprecation filter is ineffective')
Path('warning-filter-admission.json').write_text(json.dumps({
    'product_release': 'v1', 'status': 'DOING',
    'authlib_initialization_preceded_filters': True,
    'both_error_filters_exercised': True,
    'scope': 'Synthetic warning filter admission, not natural fallback or identity behavior'
}, indent=2) + '\n')
import pytest

raise SystemExit(pytest.main([
    '-W', 'error::authlib.deprecate.AuthlibDeprecationWarning',
    '-W', 'error::starlette.exceptions.StarletteDeprecationWarning',
    *sys.argv[1:],
]))
