from game_engine.player_abstract import Player
from random import choice


class PlayerAI(Player):
    """
    AI player abstract class - super class for AI difficulty classes
    Author(s):      Adam Ross; Gustav From
    Last-edit-date: 17/02/2019
    """

    def __init__(self, game, name):
        """
        Initialises the class variables
        :param game: the Game class instance
        :param name: the player's name
        """
        super().__init__(game, name)

    def max_similarities(self, pce):
        """
        Computes the maximum number of similarities found between each of the
        four characteristics for a given piece across four adjacent board cells
        in each possible horizontal, vertical and diagonal direction for each
        empty board cell and the count of occurrences of this similarity count
        :param pce: potential piece for either selecting or placing on board
        :return: list of tuples: [((pos: y, x), max similarities, count), ...]
        """
        return [(k, max(max([l[m] for m in range(len(l))])), sum([l[m].
                count(max(max([l[m] for m in range(len(l))]))) for m in range
                (len(l))])) for (k, l) in [((i, j), [self.game.bin_count(pce,
                i, j, 0, 1), self.game.bin_count(pce, i, j, 1, 0)] + [self.
                game.bin_count(pce, i, j, 1, 1) if i == j else [0, 0, 0, 0]] +
                [self.game.bin_count(pce, i, j, 1, -1) if i + j == 3 else [0,
                0, 0, 0]]) for j in range(self.game.N) for i in range(self.
                game.N) if self.game.is_cell_empty(i, j)]]

    @staticmethod
    def get_best(best, dif):
        """
        Selects a preferred piece based on provided difficulty (dif) from a
        provided list of preferred board cells (best). Determines which from
        preference list is best based on the occurrence of the preference. Eg.
        An input list has three cells with equal similarity counts, but one has
        a greater/lesser occurrence of similarities in a combination of
        horizontal, and vertical (and maybe diagonal) rows. Depending on which
        difficulty, the method will return greater (hard) / lesser (easy).
        :param best: list of tuples for preferred moves ((pos), sims, count)
        :param dif: randomly chosen difficulty; hard or easy - True or False
        :return: the selected piece for placing on the board
        """
        sims = [(l, m[1], m[2]) for l, m in best.items() if (dif and m[1] ==
                max([j for i, j, k in best.values()])) or (not dif and m[1]
                == min([j for i, j, k in best.values()]))]  # similarity
        return choice([i for i, j, k in sims if (dif and k == max([n for l, m,
                n in sims])) or (not dif and k == min([n for l, m, n in sims]))])

    def select_best_sim_count(self, prfrd, dif, pce):
        """
        Selects randomly from a list of identical best/worst possible moves
        :param prfrd: list of identical best/worst possible next moves
        :param dif: boolean to determine if searching for the min or max count
        :param pce: the piece being selected or placed on the game board
        :return: a single tuple containing ((pos: y, x), similarities, count)
        """
        opp, sim = self.easy(pce) if dif else self.hard(pce), prfrd.copy()

        while True:
            best = choice([(i, j, k) for i, j, k in sim if (dif and k == max([n
                        for l, m, n in sim])) or (not dif and k == min([n
                        for l, m, n in sim]))])

            if best[0] not in [i for i, j, k in opp]:
                return best
            else:
                sim.pop(sim.index(best))

            if len(sim) == 0:
                return choice([(i, j, k) for i, j, k in prfrd if (dif and k ==
                               max([n for l, m, n in prfrd])) or (not dif and k
                               == min([n for l, m, n in prfrd]))])

    def easy(self, pce):
        """
        Randomly chooses from a list of computed next moves that have either
        the minimum similarity of all potential next moves or a similarity of
        two and the greatest occurrence count of the selected similarity count
        For the first four plays a purely random board position is returned
        :param pce: potential piece for either selecting or placing on board
        :return: a single tuple containing ((pos: y, x), similarities, count)
        """
        sims = self.max_similarities(pce)  # max similarities & their counts
        return [(i, j, k) for i, j, k in sims if (j == 2 and 2 in [m for l, m,
                n in sims]) or j == min([m for l, m, n in sims])] if len(self.
                game.pieces) < 14 else [choice([((y, x), 1, 1) for x in
                range(self.game.N) for y in range(self.game.N) if self.game.
                is_cell_empty(y, x)])]

    def hard(self, pce):
        """
        Randomly chooses from a list of computed next moves that have either
        the maximum similarity of all potential next moves if that similarity
        is not two and the greatest occurrence count of that similarity count
        For the first two plays a purely random board position is returned
        :param pce: potential piece for either selecting or placing on board
        :return: a single tuple containing ((pos: y, x), similarities, count)
        """
        sims = self.max_similarities(pce)  # max similarities & their counts
        return [(i, j, k) for i, j, k in sims if (len([m for l, m, n in sims if
                m != 2]) > 0 and j == max([m for l, m, n in sims if m != 2]))
                or j == max([m for l, m, n in sims])] if len(self.game.pieces)\
                < 15 else [choice([((y, x), 0, 0) for x in range(self.game.N)
                for y in range(self.game.N) if self.game.is_cell_empty(y, x)])]
