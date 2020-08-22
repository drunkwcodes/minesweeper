# Sample Test passing with nose and pytest
import pytest
from minesweeper.core import *


def test_Board():
    b = Board()
    s1 = b.tile_states
    b.open_adjacent_tiles(7, 0)

    fc = b.unused_flags
    b.put_flag(0, 0)
    assert fc - b.unused_flags == 1

    b.take_flag(0, 0)
    assert fc == b.unused_flags

    b.take_flag(0, 0)
    assert fc == b.unused_flags

    b.reset()
    assert b.tile_states == s1


def test_make_matrix():
    m = make_matrix(2, 3)
    m = make_matrix(2, 3, defaults=1)


def test_Game():
    b = Board()

    # Game has a required argument: board
    with pytest.raises(TypeError):
        g = Game()

    g = Game(b)

    g.start()
    g.stop()
    assert g.used_time is not None
    g.restart(8, 8, 10)

    with pytest.raises(TypeError):
        g.restart()
