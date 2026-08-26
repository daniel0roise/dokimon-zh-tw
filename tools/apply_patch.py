#!/usr/bin/env python3
"""Apply the Dokimon Traditional Chinese fan-translation binary patch.

Uses only Python's standard library. The patch is bound to the exact original
`data.win` SHA-256 listed below; it refuses to modify other game versions.
"""
from pathlib import Path
import argparse, base64, gzip, hashlib, json, shutil, struct, sys

MAGIC = b"DOKIPATCH1"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def read_patch(chunks_dir: Path):
    encoded = "".join(p.read_text(encoding="ascii") for p in sorted(chunks_dir.glob("patch_*.b64")))
    if not encoded:
        raise RuntimeError("Patch chunks not found")
    data = gzip.decompress(base64.b64decode(encoded))
    pos = 0
    if data[:len(MAGIC)] != MAGIC:
        raise RuntimeError("Invalid patch file")
    pos += len(MAGIC)
    header_len = struct.unpack_from("<I", data, pos)[0]
    pos += 4
    header = json.loads(data[pos:pos+header_len].decode("utf-8"))
    pos += header_len
    ranges = []
    for _ in range(header["range_count"]):
        offset, length = struct.unpack_from("<QI", data, pos)
        pos += 12
        chunk = data[pos:pos+length]
        if len(chunk) != length:
            raise RuntimeError("Truncated patch file")
        pos += length
        ranges.append((offset, chunk))
    return header, ranges


def main():
    parser = argparse.ArgumentParser(description="Apply Dokimon Traditional Chinese patch")
    parser.add_argument("game_dir", nargs="?", default=".", help="Dokimon game directory (default: current directory)")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    repo_dir = script_dir.parent
    game_dir = Path(args.game_dir).resolve()
    data_win = game_dir / "data.win"
    patch_chunks = repo_dir / "patches" / "chunks"
    zh_dir = repo_dir / "Localization" / "japanese"

    if not data_win.is_file():
        sys.exit(f"Cannot find: {data_win}")

    header, ranges = read_patch(patch_chunks)
    current = sha256_file(data_win)
    if current == header["patched_sha256"]:
        print("data.win is already patched.")
    elif current != header["original_sha256"]:
        sys.exit(
            "Unsupported data.win version.\n"
            f"Expected original SHA-256: {header['original_sha256']}\n"
            f"Your file SHA-256:         {current}\n"
            "Use Steam to verify game files, then try again."
        )
    else:
        backup = game_dir / "data.win.zhTW-backup"
        if not backup.exists():
            shutil.copy2(data_win, backup)
            print(f"Backup created: {backup.name}")

        temp = game_dir / "data.win.zhTW-temp"
        shutil.copy2(data_win, temp)
        with temp.open("r+b") as f:
            for offset, chunk in ranges:
                f.seek(offset)
                f.write(chunk)
        patched = sha256_file(temp)
        if patched != header["patched_sha256"]:
            temp.unlink(missing_ok=True)
            sys.exit("Patch verification failed; original data.win was not changed.")
        temp.replace(data_win)
        print("data.win patch applied successfully.")

    target_jp = game_dir / "Localization" / "japanese"
    if target_jp.exists():
        backup_jp = game_dir / "Localization" / "japanese.zhTW-backup"
        if not backup_jp.exists():
            shutil.copytree(target_jp, backup_jp)
            print("Original Japanese localization backed up.")
    target_jp.mkdir(parents=True, exist_ok=True)
    for src in zh_dir.glob("*.txt"):
        shutil.copy2(src, target_jp / src.name)
    print("Traditional Chinese localization installed.")
    print("Launch Dokimon, select Japanese/繁體中文, and keep HD Text OFF.")


if __name__ == "__main__":
    main()
