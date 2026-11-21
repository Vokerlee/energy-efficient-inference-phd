#!/usr/bin/env python3
"""Install the checksum-pinned Pandoc binary locally, without Python packages."""

import hashlib
import io
import platform
import subprocess
import tarfile
import urllib.request
from pathlib import Path

VERSION = "3.14"
SHA256 = "c5f4720cdefb3f7bdc5d07202ef579feef0d1370773c873804dd8fdaa8c4f1b8"
ARTICLE = Path(__file__).resolve().parents[1]
PANDOC = ARTICLE / ".tools" / f"pandoc-{VERSION}" / "pandoc"


def main() -> None:
    if platform.system() != "Linux" or platform.machine() not in ("x86_64", "AMD64"):
        raise SystemExit("The pinned download supports Linux x86-64 only.")
    if PANDOC.exists():
        subprocess.run([str(PANDOC), "--version"], check=True)
        return
    name = f"pandoc-{VERSION}-linux-amd64.tar.gz"
    url = f"https://github.com/jgm/pandoc/releases/download/{VERSION}/{name}"
    print(f"Downloading {url}", flush=True)
    with urllib.request.urlopen(url, timeout=120) as response:
        archive = response.read()
    if hashlib.sha256(archive).hexdigest() != SHA256:
        raise SystemExit("Pandoc archive checksum mismatch; nothing installed.")
    with tarfile.open(fileobj=io.BytesIO(archive), mode="r:gz") as bundle:
        member = bundle.extractfile(f"pandoc-{VERSION}/bin/pandoc")
        if member is None:
            raise SystemExit("The archive has no Pandoc executable.")
        executable = member.read()
    PANDOC.parent.mkdir(parents=True, exist_ok=True)
    temporary = PANDOC.with_suffix(".tmp")
    temporary.write_bytes(executable)
    temporary.chmod(0o755)
    temporary.replace(PANDOC)
    subprocess.run([str(PANDOC), "--version"], check=True)


if __name__ == "__main__":
    main()
