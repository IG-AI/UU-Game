from game_engine.node import Node


class Minimax:
    """
    The Minimax algorithm for evaluating different moves
    Author(s): Viktor Enzell
    Last-edit-date: 10/02/2019
    """

    def __init__(self, game, depth, passed_piece):
        """
        Initialises the class variables
        :param game: the game instance
        :param depth: the depth where the algorithm should stop its search
        """
        self.board_state = game
        self.depth = depth
        self.passed_piece = passed_piece
        self.all_pieces = dict({str(i): bin(i)[2:].zfill(4) for i in range(2**4)}.items())

    def get_move(self):
        """
        Builds an evaluation tree for each possible move
        based on the current state of the game and the passed piece
        :return: the root node of the evaluation tree with the highest cost
        """
        remaining_spots = self.board_state.get_remaining_spots()
        remaining_pieces = list(self.board_state.pieces.keys())
        root_nodes = []
        for i in range(len(remaining_spots)):
            for j in range(len(remaining_pieces)):
                root = self.build_evaluation_tree(self.passed_piece,
                                                  remaining_spots[i],
                                                  remaining_pieces[j],
                                                  True,
                                                  self.board_state,
                                                  self.depth)
                root.tree_cost = self.minimax(root)
                if root.tree_cost > 0:
                    return root
                else:
                    root_nodes.append(root)

        # If no good move is found, pick an average move
        for root in root_nodes:
            if root.tree_cost == 0:
                return root
        # If there are only bad moves, pick a bad move
        if len(root_nodes) > 0:
            return root_nodes[0]

    def build_evaluation_tree(self, passed_piece, spot, next_piece, is_my_turn, board_state, depth):
        """
        Recursively builds a tree of possible moves.
        Each call makes a node from the previously passed piece and spot
        and adds as children to the node every other possible move
        :param passed_piece: the piece chosen by the opponent
        :param spot: the spot of the board where to place the passed piece
        :param next_piece: the piece to be passed to child node
        :param is_my_turn: true at root node, false at child of root, true at child of child of root and so on
        :param board_state: the current game instance
        :param depth: the depth of the node
        :return: the root node of the tree
        """
        node = Node(is_my_turn, next_piece, spot)
        new_board_state = board_state.clone_game()

        # Place piece
        row = int(spot/4)
        col = spot % 4
        new_board_state.board[row][col] = self.all_pieces.get(str(passed_piece))
        if new_board_state.pieces.get(str(passed_piece)) is not None:
            new_board_state.pieces.pop(str(passed_piece))

        if new_board_state.has_won_game(self.all_pieces.get(str(passed_piece))):
            node.set_is_leaf()
            node.set_has_won()
            return node

        if depth == 0 or next_piece == 16:
            node.set_is_leaf()
            return node

        remaining_spots = new_board_state.get_remaining_spots()
        remaining_pieces = list(new_board_state.pieces.keys())
        for i in range(len(remaining_spots)):
            if len(remaining_pieces) > 0:
                for j in range(len(remaining_pieces)):
                    node.add_child(
                        self.build_evaluation_tree(next_piece,
                                                   remaining_spots[i],
                                                   remaining_pieces[j],
                                                   not is_my_turn,
                                                   new_board_state,
                                                   depth - 1))
            else:
                node.add_child(
                    self.build_evaluation_tree(next_piece,
                                               remaining_spots[i],
                                               16,
                                               not is_my_turn,
                                               new_board_state,
                                               depth - 1))
        return node

    def minimax(self, node):
        """
        Minimax algorithm. The method is recursively called for the children of node
        and the leaves are evaluated and passed to the root.
        :param node: the node to evaluate
        :return: the cost of the tree
        """
        if node.is_leaf:
            if node.has_won:
                return 1 if node.is_my_turn else -1
            else:
                return 0

        cost = 0
        for child in node.children:
            child_cost = self.minimax(child)
            if node.is_my_turn:
                cost = min(cost, child_cost)
            else:
                cost = max(cost, child_cost)
        return cost
