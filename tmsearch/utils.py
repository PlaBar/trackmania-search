"""Shared constants and helpers used by every search and tool (moved out of search.py).

  TICK_MS        one physics tick in milliseconds
  ACTIONS        the 8 key combinations the beam search and A* choose from
  to_tmi_script  export an input list as TMInterface press/release lines
  verify         replay an input list from the race start and return the finish time

Nothing here is specific to beam search, so local.py, play.py, record.py, astar.py and search.py
can all import from this module without pulling in each other.
"""

from __future__ import annotations

import warnings

from .bridge import Action, Bridge

TICK_MS = 10

ACTIONS = {
    "G": Action(up=True),
    "GL": Action(up=True, left=True),
    "GR": Action(up=True, right=True),
    "-": Action(),
    "L": Action(left=True),
    "R": Action(right=True),
    "BL": Action(down=True, left=True),
    "BR": Action(down=True, right=True),
}


def to_tmi_script(inputs: list[tuple[int, Action]], offset_ms: int) -> str:
    """TMInterface script. An action applied from race time T corresponds to an input event at T + offset.

    Caveats: only the four keys are exported (analog steering is dropped), and playing a script is known
    not to reproduce searched runs exactly. Use play.py / record.py (which drive the plugin) to watch a run.
    """
    if any(a.steer for _, a in inputs):
        warnings.warn("to_tmi_script ignores analog steering; the exported script will not match this run",
                      stacklevel=2)
    lines = []
    held = {"up": False, "down": False, "left": False, "right": False}
    t = 0
    for n, a in inputs:
        want = {"up": a.up, "down": a.down, "left": a.left, "right": a.right}
        for key in ("up", "down", "left", "right"):
            if want[key] != held[key]:
                lines.append(f"{(t + offset_ms) / 1000:.2f} {'press' if want[key] else 'rel'} {key}")
                held[key] = want[key]
        t += n * TICK_MS
    return "\n".join(lines) + "\n"


def verify(bridge: Bridge, inputs: list[tuple[int, Action]], root_sid: int | None = None) -> int:
    """Replay an input sequence from the race start and return the finish time (-1 if none).

    With root_sid (a kept race-start state) the race is not restarted."""
    sid = root_sid if root_sid is not None else bridge.wait_start(restart=True).sid
    used = []
    finish = -1
    for n, a in inputs:
        node = bridge.expand(sid, a, n)
        if sid != root_sid:
            used.append(sid)
        sid = node.sid
        if node.finished:
            finish = node.finish_time
            break
    bridge.free(used + [sid])
    return finish
