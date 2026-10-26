"""Pure Windows child-environment construction; not a process or network sandbox.

Caller must separately verify the actual SystemRoot and private trial ownership,
filesystem/reparse containment and executable identities. Lexical path checks
here do not establish those properties. No parent environment is read/copied;
no global variable, filesystem, process, account or network state is changed.
"""
import ntpath
import re
import unicodedata


class EnvironmentError(ValueError):
    """Fixed category only; never include supplied machine values."""


def _local_root(value):
    if (type(value) is not str or re.match(r"^[A-Za-z]:\\", value) is None or
            "/" in value or ";" in value or
            value != unicodedata.normalize("NFC", value)):
        raise EnvironmentError("invalid_root")
    parts = value[3:].split("\\")
    if any(part in ("", ".", "..") or ":" in part or ntpath.isreserved(part) for part in parts):
        raise EnvironmentError("invalid_root")
    if ntpath.normpath(value) != value:
        raise EnvironmentError("invalid_root")
    return value


def child_environment(*, system_root: str, trial_root: str,
                      phase: str, source_build: bool = False) -> dict[str, str]:
    """Return only fixed settings plus separately supplied trusted root paths.

    The controller must pass this as the complete subprocess env, not merge it
    with os.environ. Use reviewed absolute argv, shell=False and -I/-B as
    applicable. Descendant behavior and actual bundled pip need separate checks.
    """
    system_root = _local_root(system_root)
    trial_root = _local_root(trial_root)
    if phase not in ("runtime", "build", "qualification") or type(source_build) is not bool:
        raise EnvironmentError("invalid_phase")
    if source_build and phase != "build":
        raise EnvironmentError("invalid_phase")
    try:
        common = ntpath.commonpath((system_root, trial_root))
    except ValueError:  # Different local volumes are not overlapping roots.
        common = None
    if common and common.casefold() in (system_root.casefold(), trial_root.casefold()):
        raise EnvironmentError("overlapping_roots")
    runtime_tools = ntpath.join(trial_root, "runtime", "tools")
    system_tools = ntpath.join(system_root, "System32")
    search = [runtime_tools, system_tools]
    if phase != "runtime":
        search.insert(0, ntpath.join(trial_root, phase + "-env", "Scripts"))
    env = {
        "SystemRoot": system_root,
        "WINDIR": system_root,
        "ComSpec": ntpath.join(system_tools, "cmd.exe"),
        "PATHEXT": ".COM;.EXE;.BAT;.CMD",
        "PATH": ";".join(search),
        "TEMP": ntpath.join(trial_root, "tmp"),
        "TMP": ntpath.join(trial_root, "tmp"),
        "PIP_CONFIG_FILE": "nul",
        "PIP_CACHE_DIR": ntpath.join(trial_root, "cache", "pip"),
        "PYTHONUSERBASE": ntpath.join(trial_root, "python-userbase"),
        "PYTHONPYCACHEPREFIX": ntpath.join(trial_root, "cache", "pycache"),
        "PYTHONDONTWRITEBYTECODE": "1",
        "PYTHONNOUSERSITE": "1",
        "PYTEST_DISABLE_PLUGIN_AUTOLOAD": "1",
    }
    if source_build:
        env.update(PYYAML_FORCE_LIBYAML="0", SOURCE_DATE_EPOCH="1760000000")
    return env
