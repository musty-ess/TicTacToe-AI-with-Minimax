"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns the player who has the next turn on the board.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    
    if x_count > o_count:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available_actions = set()
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                available_actions.add((i, j))
    
    return available_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    Raises an exception if the action is invalid.
    """
    i, j = action
    
    # Check if the action is valid
    if action not in actions(board):
        raise ValueError("Invalid action")
    
    new_board = [row[:] for row in board]  # Create a deep copy of the board
    new_board[i][j] = player(board)        # Make the move
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    
    if not any(EMPTY in row for row in board):
        return True
    
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board using alpha-beta pruning.
    """
    if terminal(board):
        return None

    if player(board) == X:
        value, best_action = max_value(board, -math.inf, math.inf)
    else:
        value, best_action = min_value(board, -math.inf, math.inf)

    return best_action

def max_value(board, alpha, beta):
    """
    Returns the best possible value for X and the corresponding action using alpha-beta pruning.
    """
    if terminal(board):
        return utility(board), None

    v = -math.inf
    best_action = None

    for action in actions(board):
        value, _ = min_value(result(board, action), alpha, beta)
        if value > v:
            v = value
            best_action = action
        alpha = max(alpha, v)
        if alpha >= beta:
            break  # Beta cutoff

    return v, best_action

def min_value(board, alpha, beta):
    """
    Returns the best possible value for O and the corresponding action using alpha-beta pruning.
    """
    if terminal(board):
        return utility(board), None

    v = math.inf
    best_action = None

    for action in actions(board):
        value, _ = max_value(result(board, action), alpha, beta)
        if value < v:
            v = value
            best_action = action
        beta = min(beta, v)
        if alpha >= beta:
            break  # Alpha cutoff

    return v, best_action