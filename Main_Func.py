from minimax import *
import numpy as np


depth = 2
gameFinished=False
board = initializeBoard()


x = int(input("please 1 to play first or 0 to play second: "))

def addPieceToColumn(column,piece):
  global board
  for row in range(5,-1,-1):
      if board[row][column] == -1:
          board[row][column] = piece
          break

  drawBoard(board)

def drawBoard(board):
    newBoard=list(map(list, board))
    for row in range(5, -1, -1):
        for columnIndex in range(7):
            if(newBoard[row][columnIndex]==1):
                newBoard[row][columnIndex]="★"
            elif (newBoard[row][columnIndex] == 0):
                newBoard[row][columnIndex] ="☆"
            else:
                newBoard[row][columnIndex]="_"

    print(np.matrix(newBoard))

    print("###################################")


def human_Turn():
    col = int(input("Enter the column You want to play in: "))
    return col


def AI_Turn():
    global depth
    col, ret = minimax(board, depth, -1000000, 1000000, True)
    #print(col)
    return col






while(not(gameFinished)):
    if(x==1):
        col = human_Turn()
        addPieceToColumn(col,+1)
        col = AI_Turn()
        addPieceToColumn(col,0)
    elif(x==0):
        #print(x)
        col = AI_Turn()
        print("AI Move")
        addPieceToColumn(col, +1)
        print("Human Move")
        col = human_Turn()
        addPieceToColumn(col,0)





