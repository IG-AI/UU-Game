import tournament as t
import random

def main():
    players = 4
    player_list = []
    player_name = ["Pettersson", "Undran", "Ola", "Mr.X", "Bumbi-Bu", "Pelle", "Gerald", "Ronald", "Nisse", "Megamen", "Baby-Jesus", "Tyke", "Kim", "Q"]
    for i in range(players):
        temp = random.choice(player_name)
        player_name.remove(temp)
        player_list.append(temp)
    tournament1 = t.Tournament(player_list)
    print(tournament1.get_scoreboard())
    while tournament1.winner_state == 0:
        print("Players waiting: ", tournament1.waiting_players)
        random_number = random.randint(0, 1)
        print("All Opponents: ", tournament1.all_opponents)
        print("Opponents queue: ", tournament1.opponents_queue)
        print("Opponents: ", tournament1.opponents)
        winner = tournament1.opponents[random_number]
        print("Winner_list_temp: ", tournament1.winner_list_temp)
        print("Winner_list: ", tournament1.winner_list)
        print("Winners this game: ",  winner)
        print()
        print("-------------------------------------------------------------")
        tournament1.next_game(winner)
        print(tournament1.get_scoreboard())
    print("Winner_list: ", tournament1.winner_list)
    print("OPPONENTS: ", tournament1.all_opponents)
    print("WINNER: ", tournament1.winner_list[tournament1.tournament_depth - 1][0])

if __name__ == "__main__":
    main()