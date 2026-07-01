#!/usr/bin/env python3
"""You know HEAD is broken but not which old commit was good.

`find_anchors` searches backward (1, 2, 4, 8, … commits) for a good commit,
then the driver runs the bisect between them — all from one script, no manual
`git bisect start` needed.

    python examples/find_anchors_then_bisect.py
"""
from bisectlib import find_anchors, bisect, check


def is_good() -> bool | None:
    """Non-exiting probe: True=good, False=bad, None='can't tell' (keep searching)."""
    if check("make -j").code != 0:
        return None                                  # won't build -> skip over it
    return check("./run_tests --only regression").ok


good, bad = find_anchors(bad="HEAD", probe=is_good, max_back=1000)
bisect(good, bad, "examples/minimal.py")             # reuse a recipe for the fine bisect
