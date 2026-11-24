"""One Word From Grandma — entry program.

Writes exactly one word, the word a grandma would text about AI,
to /output/entry.txt. Python standard library only, no network,
no randomness, fully deterministic.
"""

import os
import shutil

WORD = "ROBOTO"
OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def clear_output_dir():
    """Remove the *contents* of /output only, never /output itself."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)


def validate(word):
    """Gate: 1-30 chars, UTF-8, not only whitespace."""
    if not isinstance(word, str):
        raise ValueError("word must be a string")
    if not 1 <= len(word) <= 30:
        raise ValueError("word must be 1-30 characters")
    if not word.strip():
        raise ValueError("word must not be only whitespace")
    word.encode("utf-8")
    return word


def main():
    word = validate(WORD)
    clear_output_dir()
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(word)
    os.chmod(OUTPUT_FILE, 0o644)
    # Re-read and re-check what actually landed on disk.
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        validate(f.read())


if __name__ == "__main__":
    main()
