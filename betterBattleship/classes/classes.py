import logging
import numpy as np
from collections import namedtuple
from dataclasses import dataclass

module_logger = logging.getLogger('battleship.classes')


class Board:
    """
    Main class that defines the boards where ships will be placed
    """

    def __init__(self, player_name, rows=10, columns=10, water_char='~'):
        self.logger = logging.getLogger('battleship.classes.Board')
        self.player_name = player_name
        self.size = namedtuple("boardSize", "rows columns")(rows, columns)
        self.tiles = np.full(shape=(rows, columns), fill_value=water_char, dtype=object)
        return

    def __repr__(self):
        return f"A board owned by {self.player_name} with a size of {self.size.rows}x{self.size.columns}"
