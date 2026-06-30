#!/usr/bin/env python3
"""Example bisectlib recipe: a performance regression with a one-line build fix.

Finds the commit where the benchmark got too slow. A `test` attempt "passes"
when the run is fast enough; with min_passes=1 over 5 attempts, the verdict is
"good" iff the *fastest* of 5 runs is under the threshold (i.e. min < 6.7s),
which filters out noise from a loaded machine.

Run with:  git bisect start <BAD> <GOOD> && git bisect run python examples/perf_regression.py
"""
from bisectlib import run, test, replace

# A trivial build fix needed across the whole range (auto-reverted afterwards).
replace("CMakeLists.txt", "c++14", "c++17")

run("cmake -B build -DCMAKE_BUILD_TYPE=Release")
run("cmake --build build -j")

# Good iff the fastest of up to 5 runs is under 6.7s (stops early once one is).
test("./build/bench --run", attempts=5, min_passes=1,
     passed=lambda r: r.ok and r.seconds < 6.7)
