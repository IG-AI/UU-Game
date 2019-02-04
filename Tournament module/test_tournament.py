import tournament as t
import random

def main():
    players = 8
    player_list = []
    for i in range(players):
        player_list.append(i)
    tournament1 = t.Tournament(player_list)
    while tournament1.winner_state == 0:
        print("Players left: ", tournament1.current_player_list)
        random_number = random.randint(0, 1)
        print("Opponents: ", tournament1.opponents)
        winner = tournament1.opponents[random_number]
        print("Winners this game: ",  winner)
        tournament1.get_opponents(winner)
    print("WINNER: ", tournament1.winner_list[0])

if __name__ == "__main__":
    main()