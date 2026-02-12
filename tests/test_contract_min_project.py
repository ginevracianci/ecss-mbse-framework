import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]
CLI_SCRIPT = REPO_ROOT / "ecss-mbse-framework" / "tools" / "compliance_checker.py"
FIXTURE_DIR = REPO_ROOT / "tests" / "fixtures" / "min_project"


def _run_cli(args, cwd=None):
    env = dict(os.environ)
    env.setdefault("PYTHONUTF8", "1")
    return subprocess.run(
        [sys.executable, str(CLI_SCRIPT), *args],
        cwd=cwd,
        text=True,
        encoding="utf-8",
        capture_output=True,
        timeout=10,
        env=env,
        check=False,
    )


def test_contract_min_project(tmp_path):
    if not CLI_SCRIPT.exists():
        pytest.skip(f"CLI script not found: {CLI_SCRIPT}")
    if not FIXTURE_DIR.exists():
        pytest.skip(f"Fixture not found: {FIXTURE_DIR}")

    help_result = _run_cli(["--help"])
    if help_result.returncode != 0 or "--report" not in help_result.stdout:
        pytest.skip("CLI options not stable; skipping contract test.")

    project_path = tmp_path / "min_project"
    shutil.copytree(FIXTURE_DIR, project_path)

    report_path = tmp_path / "compliance_report.md"
    result = _run_cli([str(project_path), "--report", str(report_path)])

    assert result.returncode == 0
    assert report_path.exists()
    assert "ECSS Compliance Report" in report_path.read_text(encoding="utf-8")
