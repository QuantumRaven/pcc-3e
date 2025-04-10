#!/usr/bin/env python3

from pathlib import Path

path = Path("pi_digits.txt")
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(line)
