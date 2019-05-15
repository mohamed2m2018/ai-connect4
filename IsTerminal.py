width = 7

def CheckHorizontal(board):
    list= [ ]
    for RowNumber in range(len(board) - 1,-1,-1):
        #print(row)
        CountPlayer1 = 0
        CountPlayer2 = 0
        CountForHollow = 0
        for e in board[RowNumber]:
            if e == 1:
                CountPlayer1 = CountPlayer1 + 1
                CountPlayer2 = 0
            elif e == 0:
                CountPlayer2 = CountPlayer2 + 1
                CountPlayer1 = 0
            elif e == -1:
                CountForHollow = CountForHollow + 1
                CountPlayer1 = 0
                CountPlayer2 = 0

            if CountPlayer1 >= 4:
                return "player1 wins"
            elif CountPlayer2 >= 4:
                return "player2 wins"
            elif CountForHollow >= 5:
                break









def CheckVertical(board):
    global width
    for col in range(0,width):
        #print("col = ",col)
        CountPlayer1 = 0
        CountPlayer2 = 0
        for RowNumber in range(len(board) - 1, -1, -1):
            e = board[RowNumber][col]
            if e == 1:
                CountPlayer1 = CountPlayer1 + 1
                CountPlayer2 = 0
            elif e == 0:
                CountPlayer2 = CountPlayer2 + 1
                CountPlayer1 = 0
            if e == -1:    # There is a hollow
                break

        if CountPlayer1 == 4:
            return "player1 wins"

        elif CountPlayer2 == 4:
            return "player2 wins"


def CheckLeftDiagonal(board):
    global width
    k = 3
    for L in range(0,3):        # first loop ( iterating for 3 diagonals )
        col = 0
        CountPlayer1 = 0
        CountPlayer2 = 0
        for row in range(k,-1,-1):         # To iterate in one diagonal
            e = board[row][col]

            if e == 1:
                CountPlayer1 = CountPlayer1 + 1
                CountPlayer2 = 0
            elif e == 0:
                CountPlayer2 = CountPlayer2 + 1
                CountPlayer1 = 0
            if e == -1:          # There is a hollow
                CountPlayer1 = 0
                CountPlayer2 = 0

            col = col + 1

            if CountPlayer1 >= 4:
                return "player1 wins"

            elif CountPlayer2 >= 4:
                return "player2 wins"


        k = k + 1


    k = 1
    for L in range(0,3):         # second loop ( iterating for 3 diagonals )
        row = 5
        CountPlayer1 = 0
        CountPlayer2 = 0
        for col in range(k,width):      # To iterate in one diagonal
            e = board[row][col]
            if e == 1:
                CountPlayer1 = CountPlayer1 + 1
                CountPlayer2 = 0
            elif e == 0:
                CountPlayer2 = CountPlayer2 + 1
                CountPlayer1 = 0
            elif e == -1:  # There is a hollow
                CountPlayer1 = 0
                CountPlayer2 = 0

            row = row - 1

            if CountPlayer1 >= 4:
                return "player1 wins"

            elif CountPlayer2 >= 4:
                return "player2 wins"


        k = k + 1


def CheckRightDiagonal(board):
    global width
    k = 3
    for L in range(0,3):        # first loop ( iterating for 3 diagonals )
        row = 5
        CountPlayer1 = 0
        CountPlayer2 = 0
        for col in range(k,-1,-1):         # To iterate in one diagonal
            e = board[row][col]

            if e == 1:
                CountPlayer1 = CountPlayer1 + 1
                CountPlayer2 = 0
            elif e == 0:
                CountPlayer2 = CountPlayer2 + 1
                CountPlayer1 = 0
            if e == -1:          # There is a hollow
                CountPlayer1 = 0
                CountPlayer2 = 0

            row = row - 1

            if CountPlayer1 >= 4:
                return "player1 wins"

            elif CountPlayer2 >= 4:
                return "player2 wins"



        k = k + 1

    k = 5
    for L in range(0, 3):  # second loop ( iterating for 3 diagonals )
        col = 6
        CountPlayer1 = 0
        CountPlayer2 = 0
        for row in range(k,-1 ,-1):  # To iterate in one diagonal
            e = board[row][col]

            if e == 1:
                CountPlayer1 = CountPlayer1 + 1
                CountPlayer2 = 0
            elif e == 0:
                CountPlayer2 = CountPlayer2 + 1
                CountPlayer1 = 0
            elif e == -1:  # There is a hollow
                CountPlayer1 = 0
                CountPlayer2 = 0


            col = col - 1

            if CountPlayer1 >= 4:
                return "player1 wins"

            elif CountPlayer2 >= 4:
                return "player2 wins"


        k = k - 1


def isTerminal(board):
    ret = "None"
    ret = CheckHorizontal(board)

    if ret == "player1 wins":
        return "player1 wins"
    elif ret == "player2 wins":
        return "player2 wins"

    ret = CheckVertical(board)

    if ret == "player1 wins":
        return "player1 wins"
    elif ret == "player2 wins":
        return "player2 wins"

    # we should check this from the fourth row
    ret = CheckLeftDiagonal(board)

    if ret == "player1 wins":
        return "player1 wins"
    elif ret == "player2 wins":
        return "player2 wins"

    ret = CheckRightDiagonal(board)


    if ret == "player1 wins":
        return "player1 wins"
    elif ret == "player2 wins":
        return "player2 wins"

    else:
        return 0


# def ColIsNotValid(col):

def initializeBoard():
    board = [
        [ -1 , -1 , -1 , -1 , -1 , -1  , -1 ],
        [ 1 , -1 , -1 , -1 , -1 , -1  , -1 ],
        [ 0 , 1 , -1 , -1 , -1 , -1  , -1 ],
        [ 1 , 1 , 1 , 0 , -1 , -1  , -1 ],
        [ 0 , 1 , 0 , 1 , -1 , -1  , -1 ],
        [ 0 , 0 , 0 , 1 , -1 , -1  , -1 ]
    ]
    return board

# board = initializeBoard()
# ret = isTerminal(board)
# print(ret)