"""The one Trackmania 2020 palette (from trackmania.com) shared by the charts and the video.

Colours are hex strings (what matplotlib wants). Pillow in video.py wants RGB tuples: use rgb().

    from .color import SURFACE, SERIES, rgb
    BG = rgb(SURFACE)
"""

from __future__ import annotations

SURFACE = "#071A2C"  
NAVY_HEX = "#0B3256"    
TEXT = "#F1FFF6"
MUTED = "#8DA2B5"
GRID = "#1A3550"
SERIES = "#6EFAA0"    
GOLD = "#E2BA12"
AHEAD_HEX = "#3AA0FF"  
BEHIND_HEX = "#FF5A5A"
REF = MUTED 

BG = rgb(SURFACE)       
NAVY = rgb(NAVY_HEX)        
ACCENT = rgb(SERIES) 
GHOST = rgb(TEXT)        
WHITE = rgb(TEXT)        
AUTHOR = rgb(SERIES)       
AHEAD = rgb(AHEAD_HEX)     
BEHIND = rgb(BEHIND_HEX)   
GOLD_RGB = rgb(GOLD)     
MUTED_RGB = rgb(MUTED) 


def rgb(hex_str: str) -> tuple[int, int, int]:
    """'#6EFAA0' -> (110, 250, 160)."""
    h = hex_str.lstrip("#")
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))
