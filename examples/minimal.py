#!/usr/bin/env python3
"""The simplest possible recipe: build, then run the test suite.

    git bisect start <BAD> <GOOD>
    git bisect run python examples/minimal.py
"""
from bisectlib import run, test

run("make -j")        # infra: a broken build ABORTS (fix the recipe, then resume)
test("make check")    # verdict: a non-zero exit means this commit is bad
# reaching the end == good
