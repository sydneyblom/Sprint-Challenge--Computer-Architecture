#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()

# Implement a Multiply instruction (run `mult.ls8`)
if len(sys.argv) != 2:
    print("ERROR: Must have file name", file=sys.stderr)
    sys.exit(1)

cpu.load()
cpu.run()