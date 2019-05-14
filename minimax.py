
from utility import utility 
from isTerminal import isTerminal 

def minimax(board, depth, alpha, beta, maximizingPlayer):
    
    if(depth == 0 or isTerminal(board)):
        return utility(board,)

    if maximizingPlayer:
        value = -1000000
        # children function to be implemented
        for child in children(board, 0):
            value = max(value, minimax(child, depth-1, alpha, beta, False))

            alpha = max(alpha, value)

            # cutoff
            if(alpha >= beta):
                break

        return value
    else:
        value = 1000000
        for child in children(board, 1):
            value = min(value, minimax(child, depth-1, alpha, beta, True))
            beta = min(beta, value)
            if(alpha >= beta):
                break
        return value


# children(board)=> 1- generate tree 2- store tree 3- return stored tree as list
# utilty(board)


# isTerminal(board)
# ColIsNotValid(col)


def initializeBoard():
    board = [
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1]
    ]
    return board


def children(board, coin):
    children = []
    columnsDiscovered = [0, 0, 0, 0, 0, 0, 0]
    # print(board[5])
    for rowIndex in range(5, -1, -1):
        for columnIndex in range(7):
            if(columnsDiscovered[columnIndex]):
                continue
            childBoard = list(map(list, board))
            row = childBoard[rowIndex]
            if(row[columnIndex] == -1):
                row[columnIndex] = coin
                columnsDiscovered[columnIndex] = 1
                children.append(childBoard)
    return children

# Initial call
# minimax(initialBoard,depth,-1000000,1000000,true)
# depth level of 6 seemed to be the optimal
