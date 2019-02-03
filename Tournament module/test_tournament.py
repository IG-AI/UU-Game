import tournament as t
import random

def main():
    players = 9
    tournament_depth = 5
    player_list = []
    for i in range(players):
        player_list.append(i)
    tournament1 = t.Tournament(player_list)
    print("Chosen opponents: ", tournament1.opponents_list)
    for i in range((tournament_depth) - 1):
        winner_list = []
        for i in range(len(tournament1.opponents_list)):
            random_number = random.randint(0, 1)
            winner = tournament1.opponents_list[i][random_number]
            winner_list.append(winner)
        print("Winners: ",  winner_list)
        tournament1.update_opponents(winner_list)
        print("New opponents: ", tournament1.opponents_list)

if __name__ == "__main__":
	main()