import os
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CLI_SCRIPT = REPO_ROOT / "ecss-mbse-framework" / "tools" / "compliance_checker.py"


def _run_cli(args, cwd=None):
    if not CLI_SCRIPT.exists():
        raise FileNotFoundError(f"CLI script not found: {CLI_SCRIPT}")
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


def test_cli_help_smoke():
    result = _run_cli(["--help"])
    assert result.returncode == 0
    assert "ECSS Compliance Checker" in result.stdout


def test_cli_version_smoke():
    result = _run_cli(["--version"])
    assert result.returncode == 0
    assert "ECSS Compliance Checker v" in result.stdout
