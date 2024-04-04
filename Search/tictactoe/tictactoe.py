"""
Tic Tac Toe Player
"""

import math
import copy

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
    Returns player who has the next turn on a board.
    """
    XCount = 0
    OCount = 0
    for i in board:
        for j in i:
            if j == X:
                XCount += 1
            elif j == O:
                OCount += 1
    if XCount == OCount:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    RActions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                RActions.add((i,j))
    return RActions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] == EMPTY and action[0] in [0,1,2] and action[1] in [0,1,2]:
        ResultBoard = copy.deepcopy(board)
        p = player(board)
        ResultBoard[action[0]][action[1]] = p
        return ResultBoard
    else:
        raise Exception

def winnerHorizontal(board):
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][1] != EMPTY:
            return board[i][0]
    return False
def winnerVertical(board):
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[1][i] != EMPTY:
            return board[0][i]
    return False
def winnerDiagonal(board):
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
    return False

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    wH = winnerHorizontal(board)
    wV = winnerVertical(board)
    wD = winnerDiagonal(board)
    if wH == False:
        if wV == False:
            if wD == False:
                return None
            else:
                return wD
        else:
            return wV
    else:
        return wH


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    else:
        for i in board:
            for j in i:
                if j == EMPTY:
                    return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    return 0

def MaxValue(board):
    if terminal(board):
        return utility(board)
    else:
        v=-2
        for i in actions(board):
            if MinValue(result(board,i)) > v:
                v = MinValue(result(board,i))
        return v
def MinValue(board):
    if terminal(board):
        return utility(board)
    else:
        v=2
        for i in actions(board):
            if MaxValue(result(board,i)) < v:
                v = MaxValue(result(board,i))
        return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            v=-2
            for i in actions(board):
                if MinValue(result(board,i))>v:
                    v=MinValue(result(board,i))
                    bestAction = i
            return bestAction
        else:
            v=2
            for i in actions(board):
                if MaxValue(result(board,i)) < v:
                    v=MaxValue(result(board,i))
                    bestAction = i
            return bestAction


board1 = [[O, X, X],
          [O, O, O],
          [X, O, X]]
print(winner(board1))