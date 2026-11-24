"""The Funniest Toaster Error Message — make.fun entry.

Writes one line (62 characters, within the 1-120 gate) to /output/entry.txt:
the funniest error message a kitchen toaster would show its owner.

Stdlib only. No network, no reads outside this repository.
The output directory honours $MAKEFUN_OUTPUT_DIR (default /output) so the
program can be tested locally without touching the sandbox path.
"""

import os

LINE = "ERROR: The crumb tray is full of evidence. I am not saying whose."

# The gate: 1-120 characters, not only whitespace, a single line.
assert 1 <= len(LINE) <= 120, "line outside the 1-120 gate"
assert LINE.strip() == LINE and "\n" not in LINE, "line must be a single line"


def main() -> None:
    os.umask(0o022)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)
    # Self-check: re-read and confirm the file is exactly the line + newline.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != LINE + "\n":
            raise SystemExit("entry.txt does not match the approved line")


if __name__ == "__main__":
    main()
