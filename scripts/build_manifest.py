"""Write or check manifest.json: path, bytes, SHA-256 and git blob SHA-1 of every tracked file except the manifest.

    python scripts/build_manifest.py --previous <commit> --skill-commit <commit>   # write
    python scripts/build_manifest.py --check                                        # verify
"""
import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
SCOPE = "Complete Trading Edge Lab v1-v4 authored archive; repository-relative paths; manifest excludes itself"


def entries():
    paths = subprocess.run(["git", "-C", str(root), "ls-files", "-z"], capture_output=True, check=True).stdout
    out = []
    for rel in sorted(p for p in paths.decode().split("\0") if p and p != "manifest.json"):
        data = (root / rel).read_bytes()
        blob = hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()
        out.append({"path": rel, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(), "git_blob_sha1": blob})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--previous")
    ap.add_argument("--skill-commit")
    a = ap.parse_args()
    path = root / "manifest.json"
    if a.check:
        saved = json.loads(path.read_text())
        now = entries()
        ok = saved["files"] == now
        print(f"{len(now)} tracked files; manifest {'matches' if ok else 'DIFFERS'}")
        if not ok:
            have = {e["path"]: e for e in saved["files"]}
            for e in now:
                if have.get(e["path"]) != e:
                    print("  differs:", e["path"])
            for p in set(have) - {e["path"] for e in now}:
                print("  missing on disk:", p)
        return 0 if ok else 1
    if not (a.previous and a.skill_commit):
        sys.exit("give --previous and --skill-commit")
    manifest = {"scope": SCOPE, "previous_edge_commit": a.previous, "installed_skill_commit": a.skill_commit,
                "files": entries()}
    path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {path} with {len(manifest['files'])} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
