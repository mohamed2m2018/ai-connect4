from utility import utility
from IsTerminal import isTerminal
                                                                                        #
                                                                                        # board = [
                                                                                        #         [E, E, E, E, E, E, E],
                                                                                        #         [E, E, E, E, E, E, E],
                                                                                        #         [E, E, E, E, E, E, E],
                                                                                        #         [A, E, E, E, E, E, E],
                                                                                        #         [A, H, E, H, A, H, E],
                                                                                        #         [A, H, E, H, A, H, E]
                                                                                        #     ]
                                                                                        #     return board

count = 1
def minimax(board, depth, alpha, beta, maximizingPlayer,AiIsFirstPlayer,difficulty):
    global count
    # if board == [[-1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1], [+1, -1, -1, -1, -1, -1, -1], [1, -1, -1, -1, -1, -1, -1], [1, 0, -1, 0, 1, 0, -1], [1, 0, -1, 0, 1, 0, -1]]:
    # print("HIIII")
    ret = isTerminal(board)
    if(depth == 0 or ret):
        output = utility(board,ret,AiIsFirstPlayer,difficulty)
        # print("count = " , count ," is ",output)
        # count = count + 1
        return 0, output

    if maximizingPlayer:
        value = -1000008
        # col = 0
        # children function to be implemented
        for child in children(board, AiIsFirstPlayer):
            columnIndex=child["col"]
            childBoard=child["board"]

            _,outputFromMinMax = minimax(childBoard, depth-1, alpha, beta, False,AiIsFirstPlayer,difficulty)

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
        value = 1000008
        # col = 0
        for child in children(board, not (AiIsFirstPlayer)):
            columnIndex = child["col"]
            childBoard = child["board"]
            _,outputFromMinMax = minimax(childBoard, depth-1, alpha, beta, True,AiIsFirstPlayer,difficulty)

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
                children.append({"col":columnIndex, "board":childBoard})
    children.sort(key=lambda k: k['col'])
    return children



def initializeBoard():
    E = -1     # Empty
    H = 0      # Human
    A = 1      # AI
    board = [
        [E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E]
    ]
    return board
#
# depth = 2
# initialBoard = initializeBoard()
# col,ret = minimax(initialBoard,depth,-1000000,1000000,True)
# print("Chosen col = ",col)
# print("score =",ret)
# # depth level of 6 seemed to be the optimal



 # Testing children #
# initialBoard = initializeBoard()
# chiiii = children(initialBoard,1)
#
# print(chiiii)


# [[2, [[-1, -1, -1, -1, -1, -1, -1],
#       [-1, -1, -1, -1, -1, -1, -1],
#       [-1, -1, -1, -1, -1, -1, -1],
#       [1, -1, -1, -1, -1, -1, -1],
#       [1, 0, -1, 0, 1, 0, -1],
#       [1, 0, 1, 0, 1, 0, -1]]],
#
#  [6, [[-1, -1, -1, -1, -1, -1, -1],
#       [-1, -1, -1, -1, -1, -1, -1],
#       [-1, -1, -1, -1, -1, -1, -1],
#       [1, -1, -1, -1, -1, -1, -1],
#       [1, 0, -1, 0, 1, 0, -1],
#       [1, 0, -1, 0, 1, 0, 1]]],
#
#
#  [1, [[-1, -1, -1, -1, -1, -1, -1],
#       [-1, -1, -1, -1, -1, -1, -1],
#       [-1, -1, -1, -1, -1, -1, -1],
#       [1, 1, -1, -1, -1, -1, -1],
#       [1, 0, -1, 0, 1, 0, -1],
#       [1, 0, -1, 0, 1, 0, -1]]],
#
#
#  [3, [[-1, -1, -1, -1, -1, -1, -1],
#       [-1, -1, -1, -1, -1, -1, -1],
#       [-1, -1, -1, -1, -1, -1, -1],
#       [1, -1, -1, 1, -1, -1, -1],
#       [1, 0, -1, 0, 1, 0, -1],
#       [1, 0, -1, 0, 1, 0, -1]]],
#
#  [4, [[-1, -1, -1, -1, -1, -1, -1],
#       [-1, -1, -1, -1, -1, -1, -1],
#       [-1, -1, -1, -1, -1, -1, -1],
#       [1, -1, -1, -1, 1, -1, -1],
#       [1, 0, -1, 0, 1, 0, -1],
#       [1, 0, -1, 0, 1, 0, -1]]],
#
#  [5, [[-1, -1, -1, -1, -1, -1, -1],
#       [-1, -1, -1, -1, -1, -1, -1],
#       [-1, -1, -1, -1, -1, -1, -1],
#       [1, -1, -1, -1, -1, 1, -1],
#       [1, 0, -1, 0, 1, 0, -1],
#       [1, 0, -1, 0, 1, 0, -1]]],
#
#  [0, [[-1, -1, -1, -1, -1, -1, -1],
#       [-1, -1, -1, -1, -1, -1, -1],
#       [1, -1, -1, -1, -1, -1, -1],
#       [1, -1, -1, -1, -1, -1, -1],
#       [1, 0, -1, 0, 1, 0, -1],
#       [1, 0, -1, 0, 1, 0, -1]]]]
