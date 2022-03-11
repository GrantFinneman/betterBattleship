import logging
import numpy as np
import sys
from classes.classes import Board

# ======================================================================================================================
# The logging setup is kinda new to me
logger = logging.getLogger('battleship')
logger.setLevel(logging.DEBUG)

# Filehandler so logs get sent to a file
fh = logging.FileHandler('battleship.log')
fh.setLevel(logging.DEBUG)

# Formatter for the log messages
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

# Adds handlers to logger
logger.addHandler(fh)
# ======================================================================================================================

Version = "0.01"

grant_board = Board("grant")
print(grant_board)

for r in range(grant_board.size.rows):
    row_string = " ".join(grant_board.tiles[r, :])
    print(row_string)


