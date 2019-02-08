#!/usr/bin/env python3
import random
import graphics as g

def main():
    plist = ["ETT", "TVÅ", "TRE", "FYRA", "FEM", "SEX", "SJU", "ÅTTA"]
    t = Tour(plist)
    t.display_board()
    game = t.get_next_game()
    t.set_winner(game, game.tmp())
    t.display_board()
    game = t.get_next_game()
    t.set_winner(game, game.tmp())
    t.display_board()
    game = t.get_next_game()
    t.set_winner(game, game.tmp())
    t.display_board()
    game = t.get_next_game()
    t.set_winner(game, game.tmp())
    t.display_board()
    game = t.get_next_game()
    t.set_winner(game, game.tmp())
    t.display_board()
    game = t.get_next_game()
    t.set_winner(game, game.tmp())
    t.display_board()
    game = t.get_next_game()


class Tournament:
    game_list = {}
    next_game = 0
    nr_games = 0

    def __init__(self, player_list_orig):
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
        if self.next_game == self.nr_games:
            return "END"
        else:
            game = self.game_list[self.next_game]
            self.next_game += 1
            return game

    def set_winner(self, game, winner):
        game.advance_player(winner)

    def get_bracket(self):

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
    child = None
    ID = 0
    player1 = ""
    player2 = ""

    def __init__(self, player1, player2, ID):
        self.ID = ID
        self.player1 = player1
        self.player2 = player2

    def display_game(self):
        print(self.player1, "vs", self.player2)

    def get_ID(self):
        return self.ID

    def set_child(self, child):
        self.child = child

    def get_child(self):
        if self.child:
            return self.child

    def get_players(self):
        return [self.player1, self.player2]

    def set_next(self, player):
        if self.player1 == "TBD":
            self.player1 = player
        elif self.player2 == "TBD":
            self.player2 = player
        else:
            raise Exception("Trying to fill full game")

    def advance_player(self, player):
        if self.child:
            self.child.set_next(player)

    def tmp(self):
        return self.player1


def get_2_random(player_list):
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

