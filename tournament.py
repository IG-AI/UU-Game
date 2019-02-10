#!/usr/bin/env python3
import random
import graphics as g

class Tournament:
    """
    A class which makes a tournament bracket.
    Determines which game is next to be played, based on previous \
    match results, fed back into tournament. Also produces string \
    of bracket

    Attributes
    ----------
    game_list : dictionary
        A dictionary containing all the games to be played. \
        keyed by a int
    next_game : int
        A int representing the next game, contained in game_list \
        to be played
    nr_games : int
        int reprsenting number of games in tournament

    Methods
    -------
    get_next_game(self)
        Retrieves next game from game_list and returns it
    set_winner(self, game, winner)
        Sets a winner of a certain game, to determine players of \
        future games
    get_bracket(self)
        Formats a string of the tournament bracket and returns it
    """
    game_list = {}
    next_game = 0
    nr_games = 0

    def __init__(self, player_list_orig):
        """
        Creates all Game(s), determines tournament order depending on tournament size.
        player_list_orig is copied due to the nature of selecting players. \
        It removes them from the list as they are selected.

        Parameters
        ----------
        player_list_orig : array
            list of players participating in tournament
        """
        player_list = player_list_orig.copy()
        nr_players = len(player_list)
        if nr_players == 3:
            # Game 1
            p1, p2 = get_2_random(player_list)
            g1 = Game(p1, p2, 1)
            self.game_list[0] = g1
            # Game 2
            p3 = player_list[0]
            g2 = Game(p3, "TBD", 2)
            self.game_list[1] = g2
            g1.set_child(g2)
            self.nr_games = 2

        if nr_players == 4:
            # Game 1
            p1, p2 = get_2_random(player_list)
            g1 = Game(p1, p2, 1)
            self.game_list[0] = g1
            # Game 2
            p1, p2 = get_2_random(player_list)
            g2 = Game(p1, p2, 2)
            self.game_list[1] = g2
            # Game 3
            g3 = Game("TBD", "TBD", 3)
            self.game_list[2] = g3
            g1.set_child(g3)
            g2.set_child(g3)
            self.nr_games = 3

        if nr_players == 5:
            # Game 1
            p1, p2 = get_2_random(player_list)
            g1 = Game(p1, p2, 1)
            self.game_list[0] = g1
            # Game 2
            p1, p2 = get_2_random(player_list)
            g2 = Game(p1, p2, 2)
            self.game_list[1] = g2
            # Game 3
            p1 = player_list[0]
            g3 = Game(p1, "TBD", 3)
            self.game_list[2] = g3
            g1.set_child(g3)
            # Game 4
            g4 = Game("TBD", "TBD", 4)
            self.game_list[3] = g4
            g2.set_child(g4)
            g3.set_child(g4)
            self.nr_games = 4

        if nr_players == 6:
            # Game 1
            p1, p2 = get_2_random(player_list)
            g1 = Game(p1, p2, 1)
            self.game_list[0] = g1
            # Game 2
            p1, p2 = get_2_random(player_list)
            g2 = Game(p1, p2, 2)
            self.game_list[1] = g2
            # Game 3
            p1, p2 = get_2_random(player_list)
            g3 = Game(p1, p2, 3)
            self.game_list[2] = g3
            # Game 4
            g4 = Game("TBD", "TBD", 4)
            self.game_list[3] = g4
            g1.set_child(g4)
            g2.set_child(g4)
            # Game 5
            g5 = Game("TBD", "TBD", 5)
            self.game_list[4] = g5
            g3.set_child(g5)
            g4.set_child(g5)
            self.nr_games = 5

        if nr_players == 7:
            # Game 1
            p1, p2 = get_2_random(player_list)
            g1 = Game(p1, p2, 1)
            self.game_list[0] = g1
            # Game 2
            p1, p2 = get_2_random(player_list)
            g2 = Game(p1, p2, 2)
            self.game_list[1] = g2
            # Game 3
            p1, p2 = get_2_random(player_list)
            g3 = Game(p1, p2, 3)
            self.game_list[2] = g3
            # Game 4
            p1 = player_list[0]
            g4 = Game(p1, "TBD", 4)
            self.game_list[3] = g4
            g1.set_child(g4)
            # Game 5
            g5 = Game("TBD", "TBD", 5)
            self.game_list[4] = g5
            g2.set_child(g5)
            g3.set_child(g5)
            # Game 6
            g6 = Game("TBD", "TBD", 6)
            self.game_list[5] = g6
            g4.set_child(g6)
            g5.set_child(g6)
            self.nr_games = 6

        if nr_players == 8:
            # Game 1
            p1, p2 = get_2_random(player_list)
            g1 = Game(p1, p2, 1)
            self.game_list[0] = g1
            # Game 2
            p1, p2 = get_2_random(player_list)
            g2 = Game(p1, p2, 2)
            self.game_list[1] = g2
            # Game 3
            p1, p2 = get_2_random(player_list)
            g3 = Game(p1, p2, 3)
            self.game_list[2] = g3
            # Game 4
            p1, p2 = get_2_random(player_list)
            g4 = Game(p1, p2, 4)
            self.game_list[3] = g4
            # Game 5
            g5 = Game("TBD", "TBD", 5)
            self.game_list[4] = g5
            g1.set_child(g5)
            g2.set_child(g5)
            # Game 6
            g6 = Game("TBD", "TBD", 6)
            self.game_list[5] = g6
            g3.set_child(g6)
            g4.set_child(g6)
            # Game 7
            g7 = Game("TBD", "TBD", 7)
            self.game_list[6] = g7
            g5.set_child(g7)
            g6.set_child(g7)
            self.nr_games = 7



    def get_next_game(self):
        """
        returns next game to be played, increments next_game int.
        If final game has been played, returns "END"
        """
        if self.next_game == self.nr_games:
            return "END"
        else:
            game = self.game_list[self.next_game]
            self.next_game += 1
            return game

    def set_winner(self, game, winner):
        """
        Sets winner of game. Logic for this is contained in Game class
        Parameters
        ----------
        game : Game
            game in which a winner has been determined
        winner : string
            Name of winner of game
        """
        game.advance_player(winner)

    def get_bracket(self):
        """
        Formats bracket into a string, bracket is formatted as a list of games
        """
        i = 1
        display = ""
        for game in self.game_list:
            players = self.game_list[game].get_players()
            if self.game_list[game].get_child():
                child_ID = self.game_list[game].get_child().get_ID()
            display += "Game " + str(i) + ":"
            display += '{:^10}'.format(players[0])
            display += " vs "
            display += '{:^10}'.format(players[1])
            if self.game_list[game].get_child():
                display += " - Advances to game: " + str(child_ID) + "\n"
            else:
                display += " - Wins the tournament!\n"
            i += 1

        return display

class Game:
    """
    A class to keep track of which game leads to which in the tournament. Contains \
    various data related to actual games

    Attributes
    ----------
    child : Game
        game which winner of current game should advance tournament
    ID : int
        Identity of game. This is to be able to print identity of games in tournament
    player1 : string
        The name of a player in game
    player2 : string
        The name of a player in game
    """
    child = None
    ID = 0
    player1 = ""
    player2 = ""

    def __init__(self, player1, player2, ID):
        """
        Creates game

        Parameters
        ----------
        player1 : string
            The name of a player in game
        player2 : string
            The name of a player in game
        ID : int
            Identity of game
        """
        self.ID = ID
        self.player1 = player1
        self.player2 = player2

    def get_ID(self):
        """
        Returns identity of this game
        """
        return self.ID

    def set_child(self, child):
        """
        Sets subsequent game this game leads to

        Parameters
        ----------
        child : Game
            Game which winner of this game will advance to.
        """
        self.child = child

    def get_child(self):
        """
        Returns this game's child
        """
        if self.child:
            return self.child

    def get_players(self):
        """
        Returns this game's players, in the form of a array
        """
        return [self.player1, self.player2]

    def set_next(self, player):
        """
        Sets the players in this game.

        Raises
        ------
        Exception
            If both players have already been set, Exception is raised to avoid problems \
            further down in execution
        """
        if self.player1 == "TBD":
            self.player1 = player
        elif self.player2 == "TBD":
            self.player2 = player
        else:
            raise Exception("Trying to fill full game")

    def advance_player(self, player):
        """
        Sets a player of this games child.

        Parameters
        ----------
        player : string
            player which should be set
        """
        if self.child:
            self.child.set_next(player)


def get_2_random(player_list):
    """
    Sig:    array ==> string, string
    Pre:    player_list contains at least 2 players
    Post:   two random players from array

    Example:
            get_2_random(["player1", "player2", "player3"]) ==> "player1", "player2"
            get_2_random(["player1", "player2", "player3"]) ==> "player3", "player1"
    """
    limit = len(player_list) - 1
    i = random.randint(0,limit)
    p1 = player_list[i]
    del player_list[i]
    i = random.randint(0,limit - 1)
    p2 = player_list[i]
    del player_list[i]
    return p1, p2


if __name__ == "__main__":
	main()

