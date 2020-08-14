# Sample Test passing with nose and pytest
import pytest

def test_pass():
    assert True, "dummy sample test"

from ...minesweeper import *
    b = Board()
    b.tile_states
    b.open_adjacent_tiles(7,0)
    b.tile_states
    b.reset()
    b.tile_states

