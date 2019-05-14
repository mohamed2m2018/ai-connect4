from utility import utility
from IsTerminal import isTerminal
count = 1
def minimax(board, depth, alpha, beta, maximizingPlayer):
    global count
    ret = isTerminal(board)
    if(depth == 0 or ret):
        output = utility(board,ret,True)
        # print("count = " , count ," is ",output)
        # count = count + 1
        return 0, output

    if maximizingPlayer:
        value = -1000000
        col = 0
        # children function to be implemented
        for child in children(board, 1):
            columnIndex=child[0]
            childBoard=child[1]
            _,outputFromMinMax = minimax(childBoard, depth-1, alpha, beta, False)

            if outputFromMinMax > value:    # lw al fr3 dah maximum
                value = outputFromMinMax   # save al value
                col = columnIndex          # save al index


            alpha = max(alpha, value)

            # cutoff
            if(alpha >= beta):
                # print("alpha cutoff")
                break



        return col,value
    else:
        value = 1000000
        col = 0
        for child in children(board, 0):
            columnIndex = child[0]
            childBoard = child[1]
            _,outputFromMinMax = minimax(childBoard, depth-1, alpha, beta, True)

            if outputFromMinMax < value:    # lw al fr3 dah minimum
                value = outputFromMinMax   # save al value
                col = columnIndex          # save al index


            beta = min(beta, value)
            if(alpha >= beta):
                # print("beta cutoff")
                break




        return col,value


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
                children.append([columnIndex,childBoard])
    return children





def initializeBoard():
    E = -1     # Empty
    H = 0      # Human
    A = 1      # AI
    board = [
        [E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E],
        [A, E, E, E, E, E, E],
        [A, H, E, H, A, H, E],
        [A, H, E, H, A, H, E]
    ]
    return board

depth = 4
initialBoard = initializeBoard()
col,ret = minimax(initialBoard,depth,-1000000,1000000,True)
print("Chosen col = ",col+1)
print("score =",ret)
# depth level of 6 seemed to be the optimal

# ai =>


#children = [[0, board],[1,board],[],[]]