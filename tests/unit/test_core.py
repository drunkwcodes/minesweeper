# Sample Test passing with nose and pytest
import pytest
from minesweeper.core import *

def test_Board():
    b = Board()
    s1 = b.tile_states
    b.open_adjacent_tiles(7,0)
    b.reset()
    assert b.tile_states == s1

