class Game:
    """
    Game entity class
    Author(s):      Adam Ross
    Last-edit-date: 11/02/2019
    """

    N = 4  # constant for n in the n * n size of the board

    def __init__(self):
        """
        Inits a 4x4 board and 16 unique pieces with 4-binary characteristics
        """
        self.pieces = dict({str(i): bin(i)[2:].zfill(self.N)  # dictionary
                            for i in range(2**self.N)}.items())
        self.board = [[None for i in range(self.N)] for j in range(self.N)]

    def is_cell_empty(self, y, x):
        """
        Validates that the selected cell is available for placing a piece
        :param y: the row position of the multidimensional array game board
        :param x: the column position of the multidimensional array game board
        :return: true if the selected cell is empty, false otherwise
        """
        return not self.board[y][x]  # checks if a board cell is empty

    def bin_count(self, pce, y, x, d_y, d_x, blc=3):
        """
        Counts the similarities found for each binary characteristic of a
        selected piece in a given direction from a given available
        position on the board for a given number of blocks/difficulty
        :param pce: the selected piece for placing somewhere on the board
        :param y: the row position of the available/empty board cell
        :param x: the column position of the available/empty board cell
        :param d_y: the x-direction being checked for similarities (-1, 0, 1)
        :param d_x: the y-direction being checked for similarities (-1, 0, 1)
        :param blc: the number of blocks being compared; either 1, 2, or 3
        :return: a list of similarity counts for each characteristic of a piece
        """
        return [len([k for i in range(1, blc + 1) if not self.
                is_cell_empty((d_y * i + y) % self.N, (d_x * i + x) % self.N)
                and self.board[(d_y * i + y) % self.N][(d_x * i + x) % self.N]
                [j] == k]) for j, k in enumerate(pce)]

    def has_won_game(self, pce):
        """
        Checks if 4 pieces in a row on the board have similar characteristics
        :param pce the game piece most recently placed on the board
        :return: true if there are 4 similar pieces in a row, false otherwise
        """
        return True in [max(self.bin_count(pce, i, j, 0, 1)) == 3 or max(self.
                        bin_count(pce, i, j, 1, 0)) == 3 or (i + j == 3 and
                        max(self.bin_count(pce, i, j, 1, -1)) == 3) or (i == j
                        and max(self.bin_count(pce, i, j, 1, 1)) == 3) for j in
                        range(self.N) for i in range(self.N) if self.
                        board[i][j] == pce]

    def has_next_play(self):
        """
        Checks that there are game pieces available for game play to continue
        :return: true if there are pieces available, false otherwise
        """
        return len(self.pieces) != 0

    def clone_game(self):
        """
        Clones the current game instance in order for ai to try different moves
        without altering the game state
        :return: a new instance of a game with the same state as this one
        """
        game_clone = Game()
        game_clone.pieces = dict({i for i in self.pieces.items()})
        game_clone.board = [i.copy() for i in self.board]
        return game_clone

    def get_remaining_spots(self):
        """
        :return: a list of the spots with no piece in it
        """
        remaining_spots = []
        for i in range(self.N):
            for j in range(self.N):
                if self.board[i][j] is None:
                    remaining_spots.append(i*4+j)
        return remaining_spots
