import numpy as np
import matplotlib.pyplot as plt


class ChessBoard:
    def __init__(self):
        self.grid = np.zeros((8, 8, 3))
        self.grid[0::2, 0::2] = [1, 1, 1]
        self.grid[1::2, 1::2] = [1, 1, 1]
        self.red_pos = None
        self.blue_pos = None

    def add_red(self, row, col):
        self.grid[row, col] = (1, 0.2, 0)  # red

    def add_blue(self, row, col):
        self.grid[row, col] = (0, 1, 1)  # blue

    def render(self):
        plt.imshow(self.grid)

    def is_under_attack(self):
        red_pos = np.argwhere(np.all(self.grid == (1, 0.2, 0), axis=2)).flatten()
        blue_pos = np.argwhere(np.all(self.grid == (0, 1, 1), axis=2)).flatten()

        for red_row, red_col in zip(red_pos // 8, red_pos % 8):
            for blue_row, blue_col in zip(blue_pos // 8, blue_pos % 8):
                if (
                    red_row == blue_row  # Horizontal attack
                    or red_col == blue_col  # Vertical attack
                    or abs(red_row - blue_row) == abs(red_col - blue_col)  # Diagonal attack
                ):
                    return True

        return False



chess_board = ChessBoard()

chess_board.add_red(1, 5)
chess_board.add_blue(2, 3)

chess_board.render()

under_attack = chess_board.is_under_attack()
print("Is red under attack?", under_attack)
