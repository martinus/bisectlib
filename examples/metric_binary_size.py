#!/usr/bin/env python3
"""A metric bisect: find where a numeric budget was crossed.

Here: the commit where the built binary first exceeded 5 MiB. Any measurable
number works the same way — startup time, generated-code line count, a memory
high-water mark from a profiler, etc.

    git bisect start <BAD> <GOOD>
    git bisect run python examples/metric_binary_size.py
"""
from bisectlib import run, test, check

run("make -j")
size = int(check("stat -c%s build/app").out or 0)   # measure (never exits)
print(f"binary is {size / 1024 / 1024:.2f} MiB")
test(f"test {size} -le {5 * 1024 * 1024}")           # bad once it exceeds 5 MiB
