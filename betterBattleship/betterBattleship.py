import logging, numpy as np
from collections import namedtuple

Version = "0.01"


class Board:
    def __init__(self, player_name, ships_positions, rows=10, columns=10):
        self.player_name = player_name
        self.size = namedtuple("boardSize", "rows columns")(rows, columns)
        self.ship_info = ships_positions
        self.tiles = np.full(shape=(rows, columns), fill_value="=", dtype=object)
        return

    def __repr__(self):
        return f"A board owned by {self.player_name} with a size of {self.size.rows}x{self.size.columns}"

    @property
    def tiles(self):
        return self._tiles

    @tiles.setter
    def tiles(self, new_tiles):
        self._tiles = new_tiles
        return


grant_board = Board("grant", {(1, 2): "destroyer"})
print(grant_board)
print(grant_board.tiles)
