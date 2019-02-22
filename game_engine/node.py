class Node:
    """
    A node in the evaluation tree used in the Minimax algorithm
    Author(s): Viktor Enzell
    Last-edit-date: 10/02/2019
    """

    def __init__(self, is_my_turn, passed_piece, spot):
        """
        Initialises the class variables
        :param is_my_turn: True if it is the turn of the ai making the tree False otherwise
        :param passed_piece: the piece chosen by the opponent
        :param spot: the spot of the board where to place the passed piece
        """
        self.spot = spot
        self.passed_piece = passed_piece
        self.is_my_turn = is_my_turn
        self.children = []  # The child nodes
        self.is_leaf = False
        self.has_won = False
        self.tree_cost = None  # Cost added to root node when evaluated

    def add_child(self, child):
        """
        :param child: node to add as child
        """
        self.children.append(child)

    def get_string(self):
        """
        :return: a string for printing the node
        """
        return "| My turn: " + str(self.is_my_turn) + ". Leaf: " + str(self.is_leaf)

    def set_is_leaf(self):
        """
        Mark node as leaf
        """
        self.is_leaf = True

    def set_has_won(self):
        """
        Indicate that the node represents a winning state
        """
        self.has_won = True
