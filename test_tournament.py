import tournament as t
import random

def main():
    players = 8
    player_list = []
    for i in range(players):
        player_list.append(i)
    tournament1 = t.Tournament(player_list)
    while tournament1.winner_state == 0:
    # for i in range(20):
        print("Players waiting: ", tournament1.waiting_player_list)
        random_number = random.randint(0, 1)
        print("Opponents_list: ", tournament1.opponents_list)
        print("Opponents: ", tournament1.opponents)
        winner = tournament1.opponents[random_number]
        print("Winner_list_temp: ", tournament1.winner_list_temp)
        print("Winner_list: ", tournament1.winner_list)
        print("Winners this game: ",  winner)
        tournament1.get_opponents(winner)
    print("Winner_list: ", tournament1.winner_list)
    print("OPPONENTS: ", tournament1.all_opponents)
    print("WINNER: ", tournament1.winner_list[tournament1.tournament_depth][0])

if __name__ == "__main__":
    main()