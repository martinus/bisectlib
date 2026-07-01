#!/usr/bin/env python3
"""Bisect on the CONTENT of output, not just an exit code.

Find the commit that introduced a specific compiler warning. The build itself
must still succeed (that's infrastructure); warnings are captured to a file and
the verdict greps for them.

    git bisect start <BAD> <GOOD>
    git bisect run python examples/bisect_on_output.py
"""
from bisectlib import run, test

run("cmake -B build")
run("cmake --build build 2>build.log")   # build must succeed; warnings -> build.log
# 'bad' once the deprecation warning appears in the build output
test("! grep -q 'deprecated-declarations' build.log")
