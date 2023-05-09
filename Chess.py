import numpy as np
import matplotlib.pyplot as plt


class ChessBoard:
    def __init__(self):
        """
        Initializes a ChessBoard object.

        The ChessBoard object represents an 8x8 chessboard grid with red and blue positions.
        The grid is initialized with all squares colored in a checkerboard pattern.
        The initial red and blue positions are set to None.
        """
        self.grid = np.zeros((8, 8, 3))
        self.grid[0::2, 0::2] = [1, 1, 1]
        self.grid[1::2, 1::2] = [1, 1, 1]
        self.red_pos = None
        self.blue_pos = None

    def render(self):
        """
        Renders the current state of the chessboard.

        This function visualizes the current state of the chessboard by displaying
        the grid using matplotlib's `imshow` function.
        """
        self.set_grid()
        plt.imshow(self.grid)

    def set_grid(self):
        """
        Sets the grid with the current state of the chessboard.

        This function updates the grid based on the current red and blue positions.
        If a red position is set, it adds a red piece to the grid.
        If a blue position is set, it adds a blue piece to the grid.
        """
        self.grid = np.zeros((8, 8, 3))
        self.grid[0::2, 0::2] = [1, 1, 1]
        self.grid[1::2, 1::2] = [1, 1, 1]

        if self.red_pos is not None:
            self.add_red(self.red_pos[0], self.red_pos[1])

        if self.blue_pos is not None:
            self.add_blue(self.blue_pos[0], self.blue_pos[1])

    def add_red(self, row, col):
        """
        Adds a red piece to the specified position on the chessboard.

        Parameters:
        - row (int): The row index of the position.
        - col (int): The column index of the position.
        """
        self.grid[row][col] = [1, 0.2, 0]
        self.red_pos = (row, col)

    def add_blue(self, row, col):
        """
        Adds a blue piece to the specified position on the chessboard.

        Parameters:
        - row (int): The row index of the position.
        - col (int): The column index of the position.
        """
        self.grid[row][col] = [0, 1, 1]
        self.blue_pos = (row, col)

    def is_under_attack(self):
        """
        Checks if the red and blue pieces are under attack.

        Returns:
        - bool: True if the red and blue pieces are under attack, False otherwise.
        """
        if self.red_pos is None or self.blue_pos is None:
            return False
        elif self.red_pos[0] == self.blue_pos[0] or self.red_pos[1] == self.blue_pos[1]:
            return True
        diff_row = abs(self.red_pos[0] - self.blue_pos[0])
        diff_col = abs(self.red_pos[1] - self.blue_pos[1])
        return diff_row == diff_col


board = ChessBoard()
board.render()

board.add_red(7, 4)
board.add_blue(6, 1)
board.render()
board.is_under_attack()
