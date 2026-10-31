"""Tests for the AI for Nurse Managers & Leaders static site build.

Run: python test_build.py

Stdlib only. No secrets, no network, no API keys.
"""

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
SITE = ROOT / "site"
LICENSE = ROOT / "LICENSE"
README = ROOT / "README.md"

EXPECTED_PAGES = [
    "index.html",
    "staff-education.html",
    "policy-drafts.html",
    "meeting-prep.html",
    "workload-planning.html",
    "worksheets.html",
    "disclaimer.html",
]

EXPECTED_CREDIT = "Asdale Dynamics, LLC"
EXPECTED_COPYRIGHT = "Copyright (c) 2026 Asdale Dynamics, LLC"
EXPECTED_DISCLAIMER = "Education only — not medical or HR advice"


def run(cmd):
    return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)


def test_build_runs():
    result = run([sys.executable, "build.py"])
    assert result.returncode == 0, f"build.py failed:\n{result.stderr}"


def test_pages_exist():
    for page in EXPECTED_PAGES:
        assert (SITE / page).exists(), f"Missing page: {page}"


def test_css_exists():
    assert (SITE / "assets" / "style.css").exists(), "Missing style.css"


def test_pages_have_structure():
    for page in EXPECTED_PAGES:
        text = (SITE / page).read_text(encoding="utf-8")
        assert "<!DOCTYPE html>" in text, f"{page} missing doctype"
        assert "</html>" in text, f"{page} missing closing html tag"
        assert 'assets/style.css' in text, f"{page} missing stylesheet link"
        assert EXPECTED_CREDIT in text, f"{page} missing Asdale Dynamics credit"
        assert EXPECTED_DISCLAIMER in text, f"{page} missing education-only disclaimer"


def test_license_copyright_line():
    lines = LICENSE.read_text(encoding="utf-8").splitlines()
    assert EXPECTED_COPYRIGHT in lines, f"LICENSE missing exact copyright line: {EXPECTED_COPYRIGHT}"


def test_readme_credits():
    text = README.read_text(encoding="utf-8")
    assert EXPECTED_CREDIT in text, "README missing Asdale Dynamics credit"
    assert EXPECTED_COPYRIGHT in text, "README missing copyright line"


def test_no_github_workflows():
    assert not (ROOT / ".github" / "workflows").exists(), ".github/workflows must not exist"


def test_no_secrets():
    import re
    patterns = [r"sk-", r"api[_-]?key", r"secret", r"password", r"token"]
    for path in list(ROOT.rglob("*.md")) + list(ROOT.rglob("*.html")) + list(ROOT.rglob("*.py")) + [LICENSE]:
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pat in patterns:
            if re.search(pat, text, re.IGNORECASE):
                # Allow prose mentioning "no secrets"/"API keys" as educational content
                if "no secrets" in text.lower() or "no api keys" in text.lower():
                    continue
                raise AssertionError(f"Possible secret in {path}: matched {pat}")


if __name__ == "__main__":
    tests = [
        test_build_runs,
        test_pages_exist,
        test_css_exists,
        test_pages_have_structure,
        test_license_copyright_line,
        test_readme_credits,
        test_no_github_workflows,
        test_no_secrets,
    ]
    failed = 0
    for test in tests:
        try:
            test()
            print(f"PASS {test.__name__}")
        except Exception as exc:  # noqa: BLE001
            failed += 1
            print(f"FAIL {test.__name__}: {exc}")
    print(f"\n{len(tests) - failed}/{len(tests)} tests passed")
    sys.exit(1 if failed else 0)
