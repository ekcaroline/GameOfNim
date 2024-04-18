from games import *

class GameOfNim(Game):
    """Play Game of Nim with first player 'MAX'.
    A state has the player to move, a cached utility, a list of moves in
    the form of a list of (x, y) positions, and a board, in the form of
    a list with number of objects in each row."""

    def __init__(self, board=[3, 1]):
        self.board = board
        validMoves = []

        # Creates initial game state
        for x in range(len(self.board)):
            for y in range(1, self.board[x] + 1):
                validMoves.append((x, y))
        self.initial = GameState(to_move='MAX', utility=None, board=board, moves=validMoves)

    #
    def actions(self, state):
        """Legal moves are at least one object, all from the same row. Returns a list of valid actions in the given state. 
        This is easy if you generate the list of valid moves when a child state is created."""
        return state.moves

    def result(self, state, move):
        """that returns the new state reached from the given state and the given move. 
        Assume the move is a valid move. Note that the state for a multiplayer 
        game also includes the player whose turn it is to play"""
        if move not in state.moves:
            return state  
        
        currentBoard = state.board.copy()
        newMoves = []
        index, amount = move[0], move[1]
        currentBoard[index] -= amount 
    
        
        for x in range(len(currentBoard)):
            for y in range(1, currentBoard[x] + 1):
                newMoves.append((x, y))
        return GameState(to_move = ('MAX' if state.to_move == 'MIN' else 'MIN'),
                         utility = self.utility(currentBoard, state.to_move), 
                         board = currentBoard, moves = newMoves)
                
    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        return 1 if player == 'MAX' else -1
            

    def terminal_test(self, state):
        """A state is terminal if there are no objects left"""
        return not state.moves

    def display(self, state):
        board = state.board
        print("board: ", board)


if __name__ == "__main__":
    nim = GameOfNim(board=[0, 5, 3, 1]) # Creating the game instance
    #nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger tree to search
    print(nim.initial.board) # must be [0, 5, 3, 1]
    print(nim.initial.moves) # must be [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (3, 1)]
    print(nim.result(nim.initial, (1,3) ))
    utility = nim.play_game(alpha_beta_player, query_player) # computer moves first 
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")
