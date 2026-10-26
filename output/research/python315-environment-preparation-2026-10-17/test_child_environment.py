"""Synthetic environment values only; no child, real env, trial or package run."""
import unittest
from unittest.mock import patch

from child_environment import EnvironmentError, child_environment


class ChildEnvironmentTests(unittest.TestCase):
    def make(self, **kwargs):
        return child_environment(system_root=kwargs.pop("system_root", r"C:\Windows"),
                                 trial_root=kwargs.pop("trial_root", r"C:\Research\Trial"),
                                 phase=kwargs.pop("phase", "runtime"), **kwargs)

    def test_complete_environment_does_not_inherit_parent_secrets_or_overrides(self):
        # An injected parent cannot contribute even a benign extra setting.
        parent = {"SYNTHETIC_SECRET": "fixture-only", "HTTP_PROXY": "fixture-only",
                  "PYTHONPATH": "fixture-only", "PIP_INDEX_URL": "fixture-only",
                  "PYTEST_ADDOPTS": "fixture-only", "PATH": "fixture-only"}
        with patch.dict("os.environ", parent, clear=True):
            result = self.make()
        self.assertEqual(set(result), {
            "SystemRoot", "WINDIR", "ComSpec", "PATHEXT", "PATH", "TEMP", "TMP",
            "PIP_CONFIG_FILE", "PIP_CACHE_DIR", "PYTHONUSERBASE", "PYTHONPYCACHEPREFIX",
            "PYTHONDONTWRITEBYTECODE", "PYTHONNOUSERSITE", "PYTEST_DISABLE_PLUGIN_AUTOLOAD"})
        self.assertNotIn("fixture-only", result.values())
        self.assertEqual(result["PIP_CONFIG_FILE"], "nul")

    def test_runtime_path_has_only_private_tools_and_windows_system_tools(self):
        env = self.make()
        self.assertEqual(env["PATH"], r"C:\Research\Trial\runtime\tools;C:\Windows\System32")
        self.assertEqual(env["ComSpec"], r"C:\Windows\System32\cmd.exe")
        self.assertEqual(env["TEMP"], r"C:\Research\Trial\tmp")
        self.assertEqual(env["TMP"], env["TEMP"])

    def test_build_and_qualification_paths_do_not_use_other_environments(self):
        expected = {
            "build": r"C:\Research\Trial\build-env\Scripts;C:\Research\Trial\runtime\tools;C:\Windows\System32",
            "qualification": r"C:\Research\Trial\qualification-env\Scripts;C:\Research\Trial\runtime\tools;C:\Windows\System32"}
        for phase, path in expected.items():
            with self.subTest(phase=phase):
                self.assertEqual(self.make(phase=phase)["PATH"], path)

    def test_source_build_flags_apply_only_to_declared_builds(self):
        built = self.make(phase="build", source_build=True)
        self.assertEqual(built["PYYAML_FORCE_LIBYAML"], "0")
        self.assertEqual(built["SOURCE_DATE_EPOCH"], "1760000000")
        for phase in ("runtime", "build", "qualification"):
            self.assertNotIn("PYYAML_FORCE_LIBYAML", self.make(phase=phase))
        with self.assertRaisesRegex(EnvironmentError, "^invalid_phase$"):
            self.make(source_build=True)

    def test_nonlocal_ambiguous_or_search_path_injecting_roots_are_refused(self):
        roots = ("relative", r"C:relative", "C:/Research/Trial", "C:\\",
                 r"\\host\share\trial", r"\\?\C:\trial", r"C:\a\..\b",
                 r"C:\a\NUL", r"C:\a.", r"C:\a:b", r"C:\a;D:\extra",
                 "C:\\a\nb", "C:\\e\u0301", None, True)
        for root in roots:
            for key in ("system_root", "trial_root"):
                with self.subTest(root=root, key=key), self.assertRaisesRegex(EnvironmentError, "^invalid_root$"):
                    self.make(**{key: root})

    def test_overlapping_roots_are_refused_but_other_local_volumes_are_allowed(self):
        for root in (r"C:\Windows", r"c:\windows\nested"):
            with self.subTest(root=root), self.assertRaisesRegex(EnvironmentError, "^overlapping_roots$"):
                self.make(trial_root=root)
        result = self.make(trial_root=r"D:\Private\Trial")
        self.assertEqual(result["TEMP"], r"D:\Private\Trial\tmp")

    def test_unknown_phase_and_nonboolean_build_switch_are_refused(self):
        for args in ({"phase": "unknown"}, {"phase": None}, {"source_build": 1}):
            with self.subTest(args=args), self.assertRaisesRegex(EnvironmentError, "^invalid_phase$"):
                self.make(**args)

    def test_returned_environment_is_fresh_and_does_not_change_later_calls(self):
        first = self.make()
        first["PATH"] = "synthetic mutation"
        self.assertEqual(self.make()["PATH"], r"C:\Research\Trial\runtime\tools;C:\Windows\System32")


if __name__ == "__main__":
    unittest.main()
