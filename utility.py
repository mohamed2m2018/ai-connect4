# Victor Allis solved the game, showing that with perfect play by
# both players, the first player can always win if he plays the middle
# column first, and if he chooses another column first the second
# player can always force a draw.

# parameters:
# 1-current state of board,
# 2-ai won or not
# 3-ai first player or not

# board = [
#         [0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, -1, 0, 0],
#         [0, 0, 0,-1, -1, 0, 0],
#         [0, 0, 1, -1, 0, 0, 0],
#         [0, 1, 0, 1, 1, 1, -1],
#         [1, 0, 1, 0, 1, 0, 0]
# ]

def utility(board, win, firstPlayer,difficulty):
    score = 0
 
    if (win=="player1 wins" and not(firstPlayer)) or (win=="player2 wins" and firstPlayer) :
        score= -1000000
          
    elif (win=="player2 wins" and not(firstPlayer)) or (win=="player1 wins" and firstPlayer) :
        score = 1000000


    else:    
        # Check if ai is the first player then its piece will be 1, else the default will be 0 (second player)
    
        if(firstPlayer):
            aiPiece = 1
            playerPiece=0

        else:
            aiPiece = 0
            playerPiece=1

        if difficulty == "Hard" or difficulty == "Medium":
            score += checkCenter(board, aiPiece)

        score += checkWinChances(board, aiPiece,difficulty)
        score -= checkWinChances(board,playerPiece,difficulty)
        #print(score)
    return score

def checkCenter(board, aiPiece):
    score = 0
    for row in range(len(board)):
        if(board[row][3] == aiPiece):
            score += 2
    #print("checkCenter= ",score)
    return score


def checkWinChances(board, piece,difficulty):
    score = 0
    if difficulty == "Hard":
        score += checkAllHorizontalChances(board, piece,"Hard")
        score += checkAllVerticalChances(board, piece,"Hard")
        score += checkAllDiagonalChances(board, piece,"Hard")

    elif difficulty == "Medium":
        score += checkAllHorizontalChances(board, piece,"Medium")
        score += checkAllVerticalChances(board, piece,"Medium")
        score += checkAllDiagonalChances(board, piece,"Medium")

    elif difficulty == "Easy":
        score += checkAllHorizontalChances(board, piece,"Easy")
        #score += checkAllVerticalChances(board, piece,"Easy")
        #score += checkAllDiagonalChances(board, piece,"Easy")


    return score


def checkAllHorizontalChances(board, aiPiece,difficulty):
    score = 0
    for i in range(len(board)):
        for j in range(0, 4):
            if i < 5:
                score += checkFourConsecutivePieces(
                    board[i][j:j+4], aiPiece,"Horizontal",difficulty, board[i+1][j:j+4])
            else:
                score += checkFourConsecutivePieces(board[i][j:j+4], aiPiece,"Horizontal",difficulty)

    #print("checkAllHorizontalChances= ",score)
    return score


def checkAllVerticalChances(board, aiPiece,difficulty):
    score = 0
    columnValues = []
    for j in range(0, 7):
        for i in range(len(board)):
            columnValues.append(board[i][j])

        for k in range(0, 3):
            score += checkFourConsecutivePieces(columnValues[k:k+4], aiPiece,"Vertical",difficulty)
        columnValues = []

    #print("checkAllVerticalChances= ",score)
    return score


def checkAllDiagonalChances(board, aiPiece,difficulty):
    list = []
    list = (CheckLeftDiagonalForUtility(board))
    list = list+(CheckRightDiagonalForUtility(board))
    score = 0
    for element in list:
        length = len(element)
        numberOfAlternatives = length-3
        for k in range(0, numberOfAlternatives):
            score += checkFourConsecutivePieces(element[k:k+4], aiPiece,"Diagonal",difficulty)

    #print("checkAllDiagonalChances= ",score)
    return score


def checkFourConsecutivePieces(list, piece, orientation,difficulty,secondList=None):
    # print('I am first list', list)
    full = 0
    empty = 0
    if(secondList):
        # print ('I am second list', secondList)
        for index, element in enumerate(list):
            if element == piece:
                full += 1
            elif secondList and element == -1 and secondList[index] != -1:
                empty += 1
    else:
        for element in list:
            if element == piece:
                full += 1
            elif element == -1:
                empty += 1

    # check if condition applied

    if(full == 2 and empty == 2):
        # print('detected')

        # for Hard
        if difficulty == "Hard":
            return 7

        # for Medium
        elif difficulty == "Medium" and orientation == "Horizontal":
            return 7
        elif difficulty == "Medium" and orientation == "Vertical":
            return 5
        elif difficulty == "Medium" and orientation == "Diagonal":
            return 1

        # for Easy
        elif difficulty == "Easy" and orientation == "Horizontal":
            return 4



    if(full == 3 and empty == 1):
        # print('detected')

        # for Hard
        if difficulty == "Hard":
            return 11

        # for Medium
        elif difficulty == "Medium" and orientation == "Horizontal":
            return 11
        elif difficulty == "Medium" and orientation == "Vertical":
            return 9
        elif difficulty == "Medium" and orientation == "Diagonal":
            return 1

        # for Easy
        elif difficulty == "Easy" and orientation == "Horizontal":
            return 9





    else:
        return 0


def CheckLeftDiagonalForUtility(board):
    k = 3
    list2 = []
    for L in range(0, 3):        # first loop ( iterating for 3 diagonals )
        col = 0
        list1 = []
        for row in range(k, -1, -1):         # To iterate in one diagonal
            e = board[row][col]
            if row != 5:
                if board[row+1][col] == -1:
                    e=-111
            list1.append(e)
            col = col + 1

        k = k + 1
        list2.append(list1)

    k = 1
    for L in range(0, 3):         # second loop ( iterating for 3 diagonals )
        row = 5
        list1 = []
        for col in range(k, 7):      # To iterate in one diagonal
            e = board[row][col]
            if row != 5:
                if board[row+1][col] == -1:
                    #flag that this is not a chance
                    e=-111

            list1.append(e)

            row = row - 1

        list2.append(list1)

        k = k + 1

    return list2


def CheckRightDiagonalForUtility(board):
    k = 3
    list2 = []
    for L in range(0, 3):        # first loop ( iterating for 3 diagonals )
        row = 5
        list1 = []
        for col in range(k, -1, -1):         # To iterate in one diagonal
            e = board[row][col]
            if row != 5:
                if board[row+1][col] == -1:
                    e=-111
            list1.append(e)
            row = row - 1

        k = k + 1
        list2.append(list1)

    k = 5
    for L in range(0, 3):  # second loop ( iterating for 3 diagonals )
        col = 6
        list1 = []
        for row in range(k, -1, -1):  # To iterate in one diagonal
            e = board[row][col]

            if row != 5:
                if board[row+1][col] == -1:
                    e=-111
            list1.append(e)

            col = col - 1

        list2.append(list1)
        k = k - 1

    return list2


# checkAllHorizontalChances(board,1)
# checkAllVerticalChances(board, 1)
# utility(board,-1,True)
