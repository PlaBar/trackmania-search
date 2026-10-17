"""The one Trackmania 2020 palette (from trackmania.com) shared by the charts and the video.

Colours are hex strings (what matplotlib wants). Pillow in video.py wants RGB tuples: use rgb().

    from .color import SURFACE, SERIES, rgb
    BG = rgb(SURFACE)
"""

from __future__ import annotations

SURFACE = "#071A2C"   # ink, the background
NAVY = "#0B3256"
TEXT = "#F1FFF6"
MUTED = "#8DA2B5"
GRID = "#1A3550"
SERIES = "#6EFAA0"    # TM mint: the AI / a single data series
GOLD = "#E2BA12"
AHEAD = "#3AA0FF"     # blue split when ahead of the PB ghost
BEHIND = "#FF5A5A"

# Aliases for the names the existing files already use.
REF = MUTED           # the PB / reference line in charts
INK = SURFACE
MINT = SERIES
GHOST = TEXT          # my PB ghost in the video
AUTHOR = SERIES       # author medal colour in the video


def rgb(hex_str: str) -> tuple[int, int, int]:
    """'#6EFAA0' -> (110, 250, 160)."""
    h = hex_str.lstrip("#")
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))
