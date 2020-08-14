"""Tile generation and Game Flow"""
from datetime import datetime
from random import randint

IS_OPENED = 1
IS_FLAG = 2
IS_MINE = 4


def init_matrix(row, col, defaults=0):
    matrix = []
    for i in range(row):
        matrix.append([])
        for j in range(col):
            matrix[i].append(defaults)
    return matrix


class Board:

    def __init__(self, width=8, height=8, mines=10):
        self.board_w = width
        self.board_h = height
        self.mines_amount = mines
        self.unused_flags = self.mines_amount
        self.tnumbers = init_matrix(height, width)
        self._init_tiles()
        self.game_over = False

    def _init_tiles(self):
        self.tile_states = init_matrix(self.board_h, self.board_w)
        self._place_mine()


    def _place_mine(self):
        counter = 0
        while counter < self.mines_amount:
            x = randint(0, self.board_h - 1)
            y = randint(0, self.board_w - 1)
            if not (self.tile_states[x][y] & IS_MINE):
                self.tile_states[x][y] |= IS_MINE
                counter += 1
                self._increment_adjacent_tnumber(x, y)

    def _get_adjacent_tiles(self, x, y):
        adjacent_tiles = []
        if not self.is_out_of_bound(x - 1, y - 1):
            adjacent_tiles.append((x - 1, y - 1))
        if not self.is_out_of_bound(x - 1, y):
            adjacent_tiles.append((x - 1, y))
        if not self.is_out_of_bound(x - 1, y + 1):
            adjacent_tiles.append((x - 1, y + 1))
        if not self.is_out_of_bound(x, y - 1):
            adjacent_tiles.append((x, y - 1))
        if not self.is_out_of_bound(x, y + 1):
            adjacent_tiles.append((x, y + 1))
        if not self.is_out_of_bound(x + 1, y - 1):
            adjacent_tiles.append((x + 1, y - 1))
        if not self.is_out_of_bound(x + 1, y):
            adjacent_tiles.append((x + 1, y))
        if not self.is_out_of_bound(x + 1, y + 1):
            adjacent_tiles.append((x + 1, y + 1))

        return adjacent_tiles
 
    def _increment_adjacent_tnumber(self, x, y):
        for x, y in self._get_adjacent_tiles(x, y):
            self.tnumbers[x][y] += 1


    def is_out_of_bound(self, x, y):
        return x < 0 or x >= self.board_w or y < 0 or y >= self.board_h

    def open_tile(self, x, y):
        self.tile_states[x][y] |= IS_OPENED

    def open_adjacent_tiles(self, x, y):
        for a, b in self._get_adjacent_tiles(x, y):
            tile = self.tile_states[a][b]

            if not (tile & IS_OPENED) and not (tile & IS_FLAG):
                self.open_tile(a, b)
                if self.tile_states[a][b] & IS_MINE:
                    self.game_over = True
                    return

                if self.tnumbers[a][b] == 0:
                    self.open_adjacent_tiles(a, b)

    def put_flag(self, x, y):
        self.tile_states[x][y] |= IS_FLAG
        self.unused_flags -= 1

    def take_flag(self, x, y):
        self.tile_states[x][y] &= ~IS_FLAG
        self.unused_flags += 1

    def reset(self):
        self.unused_flags = self.mines_amount
        self.game_over = False
        for i in range(self.board_h):
            for j in range(self.board_w):
                self.tile_states[i][j] &= ~IS_OPENED
                self.tile_states[i][j] &= ~IS_FLAG


class Game:

    def __init__(self, board):
        self._start_time = 0
        self._end_time = 0
        self.tiles = board
        self.over = self.tiles.game_over
        self.reset = self.tiles.reset
    
    def start(self):
        self._start_time = datetime.now()

    def stop(self):
        self._end_time = datetime.now()

    @property
    def used_time(self):
        delta = self._end_time - self._start_time
        return delta.total_seconds()

    def restart(self, width, height, mines):
        self.tiles = Board(width, height, mines)
