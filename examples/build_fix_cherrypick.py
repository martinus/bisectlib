#!/usr/bin/env python3
"""Keep an un-buildable range testable by cherry-picking a fix commit.

Older commits in a range fail to build until fix commit `deadbeef` (e.g. a
toolchain-compat fix). Apply it on the fly (--no-commit, auto-reverted) just for
those commits, so they can be tested instead of skipped — preserving bisect
resolution.

    git bisect start <BAD> <GOOD>
    git bisect run python examples/build_fix_cherrypick.py
"""
from bisectlib import run, test, fixup, in_range

with fixup(cherry_pick="deadbeef", when=in_range("v1.0..v1.5")):
    run("cmake -B build")
    run("cmake --build build -j")
test("ctest --test-dir build -R regression")
