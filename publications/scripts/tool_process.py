"""Run document-conversion tools with one logging and error policy."""

from collections.abc import Sequence
from pathlib import Path
import subprocess


def run_tool(
    arguments: Sequence[str | Path],
    *,
    cwd: Path,
    data: str | None = None,
    log: Path | None = None,
    allow_diagnostics: bool = False,
) -> str:
    result = subprocess.run(
        [str(value) for value in arguments],
        cwd=cwd,
        input=data,
        text=True,
        capture_output=True,
        check=False,
    )
    if log:
        log.write_text(result.stdout + result.stderr)
    if result.returncode:
        raise RuntimeError(
            f"Command failed: {arguments[0]}\n{result.stdout}\n{result.stderr}"
        )
    if result.stderr.strip() and not allow_diagnostics:
        raise RuntimeError(f"Unexpected conversion diagnostic:\n{result.stderr}")
    return result.stdout
