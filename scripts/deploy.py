"""Copy ./home into the user's home directory, adding a leading dot to each top-level folder.

home/agents -> ~/.agents  (mirrored: files not present in the source are deleted, after confirmation)
home/claude -> ~/.claude  (files are overwritten; other files are left untouched)
"""

import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent.parent / "home"
TARGET = Path.home()
MIRRORED = {"agents"}


def source_files(source: Path, target: Path) -> dict[Path, Path]:
    return {file: target / file.relative_to(source) for file in source.rglob("*") if file.is_file()}


def find_extraneous(target: Path, keep: set[Path]) -> list[Path]:
    if not target.exists():
        return []
    return sorted(p for p in target.rglob("*") if (p.is_file() or p.is_symlink()) and p not in keep)


def remove_empty_dirs(target: Path) -> None:
    if not target.exists():
        return
    for path in sorted(target.rglob("*"), key=lambda p: len(p.parts), reverse=True):
        if path.is_dir() and not any(path.iterdir()):
            path.rmdir()


def confirm_deletion(extraneous: list[Path]) -> bool:
    print("The following files are not in the source and will be deleted:")
    for path in extraneous:
        print(f"  {path}")
    return input("Delete them? [y/N] ").strip().lower() == "y"


def main() -> None:
    plan = {}
    to_delete = []
    for folder in sorted(p for p in SOURCE.iterdir() if p.is_dir()):
        target = TARGET / f".{folder.name}"
        files = source_files(folder, target)
        plan[target] = files
        if folder.name in MIRRORED:
            to_delete += find_extraneous(target, set(files.values()))

    delete = bool(to_delete) and confirm_deletion(to_delete)

    for target, files in plan.items():
        for source, destination in files.items():
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
        print(f"copied {len(files)} files to {target}")

    if delete:
        for path in to_delete:
            path.unlink()
        for target in plan:
            if target.name[1:] in MIRRORED:
                remove_empty_dirs(target)
        print(f"deleted {len(to_delete)} files")
    elif to_delete:
        print("deletion skipped")


if __name__ == "__main__":
    main()
