"""Validate two synthetic policy inputs in the merge-protection lab."""

from pathlib import Path

selected = Path("selected.txt").read_text().strip()
blocked = Path("blocked.txt").read_text().strip()
assert selected != blocked, "The selected option is blocked."
print("Synthetic contract satisfied.")
