from minimax import *
import numpy as np

HumanIsFirstPlayer = int(input("Press 1 to play first or 0 to play second: "))

difficulty = input("Please Enter The Difficulty: Easy / Medium / Hard: ")

if difficulty == "Hard":
    depth = 5

elif difficulty == "Medium":
    depth = 1

elif difficulty == "Easy":
    depth = 1

else:
    print("Invalid Entery")
    exit()



board = initializeBoard()

############################### depth = 5 ###############################





def addPieceToColumn(column,piece):
  global board
  flag = 0
  for row in range(5,-1,-1):
      if board[row][column] == -1:
          board[row][column] = piece
          flag = 1
          break

  if flag == 0:    # it means the col is completly full
      new_col = int(input("Invalid Move, Try another column: "))
      addPieceToColumn(new_col,piece)

  drawBoard(board)

def drawBoard(board):
    newBoard=list(map(list, board))
    for row in range(5, -1, -1):
        for columnIndex in range(7):
            if(newBoard[row][columnIndex]==1):
                newBoard[row][columnIndex]="X"
            elif (newBoard[row][columnIndex] == 0):
                newBoard[row][columnIndex] ="O"
            else:
                newBoard[row][columnIndex]="_"

    print(np.matrix(newBoard))

    print("###################################")


def human_Turn():
    col = int(input("Enter the column You want to play in: "))
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
            print("Congratulations ^^ , You have won")
            break

        print("AI Move")
        col = AI_Turn()
        addPieceToColumn(col,0)
        ret = isTerminal(board)
        if ret:
            print("OOOOOOOOPPPPPSSS You Lose , our Ai Beats you \n hhhhhhhhhh Cry Now Mr Loser :D ")
            break
    elif(HumanIsFirstPlayer==0):
        #print(x)
        col = AI_Turn()
        print("AI Move")
        addPieceToColumn(col, +1)
        ret = isTerminal(board)
        if ret:
            print("OOOOOOOOPPPPPSSS You Lose , our Ai Beats you \n hhhhhhhhhh Cry Now Mr Loser :D ")
            break

        print("Human Move")
        col = human_Turn()
        addPieceToColumn(col,0)
        ret = isTerminal(board)
        if ret:
            print("Congratulations ^^ , You have won")
            break






