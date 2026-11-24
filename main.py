# One-line pitch for u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.
# Writes a single sentence (at most 240 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
# The pitch leans on a concrete payoff (a working version by tonight) and low
# risk (no code, nothing to lose) rather than on a slogan.
import os
from pathlib import Path

PITCH = "You've had that app idea for years — tell an AI agent about it in plain words on make.fun, and by tonight you could be tapping around a real, working version of it: no code, no risk, nothing to lose but the excuse."

def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(PITCH, encoding="utf-8")

if __name__ == "__main__":
    main()
