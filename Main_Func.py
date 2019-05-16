from minimax import *
import numpy as np
HumanIsFirstPlayer = 1

def drawBoard(board):

    newBoard=list(map(list, board))
    for row in range(5, -1, -1):
        for columnIndex in range(7):
            if(newBoard[row][columnIndex]==1 or newBoard[row][columnIndex]=="X"):
                newBoard[row][columnIndex]="X"
            elif (newBoard[row][columnIndex] == 0 or newBoard[row][columnIndex] =="O"):
                newBoard[row][columnIndex] ="O"
            else:
                newBoard[row][columnIndex]="_"

    print(np.matrix(newBoard))

    print("###################################")

def load():
    global board
    global HumanIsFirstPlayer
    list = []
    loading_board = []
    f = open("connect4.txt",'r')
    x = f.read()
    #tsplit(x,('[',']',','))
    #x = x.split()

    x=x.replace('[','')
    x=x.replace(']','')
    x=x.replace(',','')
    x=x.replace("'",'')
    x=x.replace(' ','')

    count = 0
    flag = 0
    for ch in x:
        if flag == 0:
            HumanIsFirstPlayer = int(ch)
            flag = 1
            continue

        if count == 6:
            if ch == "_":
                list.append(-1)
            elif ch == "X":
                list.append(HumanIsFirstPlayer)
            elif ch == "O":
                list.append(not(HumanIsFirstPlayer))

            loading_board.append(list)
            list=[]
            count = 0

        else:
            if ch == "_":
                list.append(-1)
            elif ch == "X":
                list.append(HumanIsFirstPlayer)
            elif ch == "O":
                list.append(not (HumanIsFirstPlayer))

            count = count + 1

    #print(loading_board)
    drawBoard(loading_board)
    board = loading_board

HumanIsFirstPlayer = input('''Press 1 to play first or 0 to play second,\nor you can press "L" for loading the previous game: ''')
difficulty = input("Please Enter The Difficulty: Easy / Medium / Hard: ")

if HumanIsFirstPlayer == "1" or HumanIsFirstPlayer == "0":
    board = initializeBoard()
    HumanIsFirstPlayer = int(HumanIsFirstPlayer)

elif HumanIsFirstPlayer == "L":
    load()
    HumanIsFirstPlayer = 1

else:
    print("inavalid Entry")
    print("Bye Bye ^^")
    exit()



if difficulty == "Hard":
    depth = 5

elif difficulty == "Medium":
    depth = 2

elif difficulty == "Easy":
    depth = 1

else:
    print("Invalid Entery")
    exit()

def save():
    global board
    f = open("connect4.txt",'w')
    f.write(str(HumanIsFirstPlayer))
    f.write(str(drawBoardForText(board)))
    exit()








##########################################################################





def addPieceToColumn(column,piece):
  global board
  flag = 0
  for row in range(5,-1,-1):
      if board[row][column] == -1 or board[row][column] == "_" :
          board[row][column] = piece
          flag = 1
          break

  if flag == 0:    # it means the col is completly full
      new_col = int(input("Invalid Move, Try another column: "))
      addPieceToColumn(new_col,piece)

  drawBoard(board)

def drawBoardForText(board):
    newBoard=board.copy()
    for row in range(5, -1, -1):
        for columnIndex in range(7):
            if(board[row][columnIndex]==1):
                newBoard[row][columnIndex]="X"
            elif (board[row][columnIndex] == 0):
                newBoard[row][columnIndex] ="O"
            else:
                newBoard[row][columnIndex]="_"

    return (newBoard)

    print("###################################")



def human_Turn():

    col = input('''Enter the column You want to play in or "S" for saving game: ''')
    if col == "S":
        save()

    else:
        col= int(col)
        if col < 0 or col > 6 :
            print("Invalid Index , Try again")
            human_Turn()



    return col


def AI_Turn():
    global depth
    global difficulty
    global HumanIsFirstPlayer
    col, ret = minimax(board, depth, -1000000, 1000000, True,not(HumanIsFirstPlayer),difficulty)
    #print(col)
    return col



while(1):

    if(HumanIsFirstPlayer==1):
        col = human_Turn()
        print("Human Move")
        addPieceToColumn(col,1)
        ret = isTerminal(board)
        if ret:
            print("Congratulations ^^ , You have won\n\n")
            h = input("Press any key to continue . . . ")
            break

        print("AI Move")
        col = AI_Turn()
        addPieceToColumn(col,0)
        ret = isTerminal(board)
        if ret:
            print("OOOOOOOOPPPPPSSS You Lose , our Ai Beats you \n hhhhhhhhhh Cry Now Mr Loser :D\n\n ")
            h = input("Press any key to continue . . . ")
            break
    elif(HumanIsFirstPlayer==0):
        #print(x)
        col = AI_Turn()
        print("AI Move")
        addPieceToColumn(col, +1)
        ret = isTerminal(board)
        if ret:
            print("OOOOOOOOPPPPPSSS You Lose , our Ai Beats you \n hhhhhhhhhh Cry Now Mr Loser :D\n\n ")
            h = input("Press any key to continue . . . ")
            break

        print("Human Move")
        col = human_Turn()
        addPieceToColumn(col,0)
        ret = isTerminal(board)
        if ret:
            print("Congratulations ^^ , You have won\n\n")
            h = input("Press any key to continue . . . ")
            break






