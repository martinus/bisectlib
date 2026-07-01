#!/usr/bin/env python3
"""Bisect isn't only for regressions — find when something started WORKING.

`bad_when="pass"` flips the direction: the "old" side is where the test FAILS
and the "new"/bad side is where it PASSES, so the first-bad commit is the one
that *fixed* the bug / landed the feature / made the output start matching.

    #     old (fails) .................. new (passes)
    git bisect start <PASSES-commit> <FAILS-commit>
    git bisect run python examples/find_when_fixed.py
"""
from bisectlib import run, test

run("make -j")
test("./run_tests --only feature_x", bad_when="pass")
