from game_engine.play import Play
from game_engine.player_human import PlayerHuman


class GameEngine:
    """
    This is temporary class for the CLI testing and presentation
    Author(s):      Adam Ross; Gustav From
    Last-edit-date: 14/02/2019
    """

    def __init__(self):
        """
        The GameEngine CLI test class constructor
        """
        self.play = Play()  # initiates a Play class instance
        self.introduction()  # Prints to terminal an introduction to the game

    def introduction(self):
        print("\n*** Welcome to GameEngine ***")

    def declare_available_pieces(self):
        """
        Declares to the players the pieces available for selection
        Temporary for the CLI testing
        """
        print("\nGame pieces status:")
        print(list(self.play.game.pieces.items())[:int((len(self.play.game.
                                                            pieces) + 1) / 2)])

        if len(self.play.game.pieces) > 1:
            print(list(self.play.game.pieces.
                       items())[int((len(self.play.game.pieces) + 1) / 2):])

    def declare_board_status(self):
        """
        Declares to the players the current status of the game board
        Temporary for the CLI testing
        """
        print("\nGame board status:")
        print(*(row for row in self.play.game.board), sep="\n")

    def declare_current_player(self):
        """
        Temporary printing of current player for CLI testing and presenting
        """
        print("\nCurrent player: '" + self.play.current_player.name + "'")

    def declare_selected_piece(self):
        """
        Temporary printing of selected piece for CLI testing and presenting
        """
        print("\nCurrent piece: " + self.play.selected_piece)

    def game_mode_selection(self):
        while True:
            print("\nSelect a following game mode (enter number 1 - 3):")
            n = input("1: Player vs Player\n2: Player vs AI\n3: AI vs AI\n")

            if n == "2" or n == "3":
                print("\nSelect a following difficulty (enter number 1 - 3):")
                d = input("1: easy\n2: medium\n3: hard\n")

                if d == "1" or d == "2" or d == "3":
                    self.play.init_players(int(n), int(d))  # initializes play
                    break
            elif n == "1":
                self.play.init_players(int(n), None)  # initializes players
                break
        self.declare_current_player()  # prints the starting player turn

    def play_game(self):
        self.declare_available_pieces()  # prints game board status
        self.declare_board_status()  # prints available pieces status

        if isinstance(self.play.current_player, PlayerHuman):
            while True:
                pce = input("\nEnter number 0-15 of piece selection: ")

                if self.play.play_selection(pce):
                    break
        else:
            self.play.play_selection()
        self.declare_selected_piece()  # prints the selected piece
        self.declare_current_player()  # prints the current player turn

        if isinstance(self.play.current_player, PlayerHuman):
            while True:
                try:
                    y, x = input("\nEnter 2 ints 0-3 separated by a space: ").\
                        split()

                    if self.play.play_placement(y, x):
                        break
                except:
                    continue
        else:
            self.play.play_placement()

        if self.play.game.has_won_game(self.play.selected_piece):
            self.declare_board_status()  # prints final status of board
            print("game won by " + self.play.current_player.name)
        elif not self.play.game.has_next_play():  # checks if turns remaining
            self.declare_board_status()  # prints final status of board
        else:
            self.play_game()  # plays the next turn


if __name__ == '__main__':
    app = GameEngine()
    app.game_mode_selection()
    app.play_game()
