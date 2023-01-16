import numpy as np
import math
import re

types = ["","Pawn","Castle","Knight","Bishop","Queen","King"]


def evaluateBoard(board):
    return 0

def movePiece(board,player,S,E):
    position = (int(S[1])-1,(ord(S[0])-ord('A')))
    target = (int(E[1])-1,(ord(E[0])-ord('A')))
    piece = board[position]
    type = int(math.fabs(piece)%10)
    print(position)
    print(target)
    print(piece)
    print(type)
    playerpiece = -1 if piece < 0 else 1
    targetPiece = board[target]
    targetPlayer = 0
    print("Moving",'White' if player == 1 else 'Black',types[type],"from",str(chr(ord('A')+position[0])+str(position[1]+1)),"to",str(chr(ord('A')+target[0])+str(target[1]+1)))
    line = []
    if(position[0] == target[0]):
        line = board[:, position[0]][(min(target[1],position[1])+1):(max(target[1],position[1])-1)]
    elif position[1] == target[1]:
        line = board[(min(target[0],position[0])+1):(max(target[0],position[0])-1)]
    elif math.fabs(position[0]-target[0]) == math.fabs(position[1]-target[1]):
        for i in range(min(position[0],target[0])+1,max(position[0],target[0])-1):
            for j in range(min(position[1],target[1])+1,max(position[1],target[1])-1):
                if i - min(position[0],target[0]) == j - min(position[1],target[1]):
                    line.append(board[i][j])
    print(line)
    print(len(line))
    if targetPiece > 0:
        targetPlayer = 1
    elif targetPiece < 0:
        targetPlayer = -1
    if playerpiece != player:
        print("ERROR: You may only move your own pieces")
    elif position[0] < 0 | position[1] < 0 | position[0] > 7 | position[1] > 7:
        print("ERROR: Invalid position")
    elif target[0] < 0 | target[1] < 0 | target[0] > 7 | target[1] > 7:
        print("ERROR: Invalid end position")
    elif (not np.array(line).any()) & len(line) != 0:
        print("ERROR: Attempting to move through a piece while not a knight")
    elif targetPlayer == player:
        print("ERROR: Attemping to move ontop of your own piece")
    else:
        if type == 1: #Moving Pawn
            if(position[1] == target[1]):
                board[target] = board[position]
                board[position] = 0
            else:
                print("ERROR! Invalid Move. A pawn can only move straight or diagonally")
        elif type == 2: #Moving Castle
            if position[0] == target[0] | position[1] == target[1]:
                board[target] = board[position]
                board[position] = 0
            else:
                print("ERROR! Invalid Move. A castle may only move straight")
        elif type == 3:
            if math.fabs(position[0]-target[0]) == 1 & math.fabs(position[1]-target[1]) == 2:
                board[target] = board[position]
                board[position] = 0
            elif math.fabs(position[0]-target[0]) == 2 & math.fabs(position[1]-target[1]) == 1:
                board[target] = board[position]
                board[position] = 0
            else:
                print("ERROR! Invalid Move")
        elif type == 4:
            if math.fabs(position[0]-target[0]) == math.fabs(position[1]-target[1]):
                board[target] = board[position]
            else:
                print("ERROR! Invalid Move")
        elif type == 5:
            if math.fabs(position[0]-target[0]) == math.fabs(position[1]-target[1]):
                board[target] = board[position]
            elif position[0] == target[0]:
                board[target] = board[position]
            elif position[1] == target[1]:
                board[target] = board[position]
            else:
                print("ERROR! Invalid Move")
        elif type == 6:
            if math.fabs(position[0]-target[0]) <= 1 & math.fabs(position[1]-target[1]) <= 1:
                board[target] = board[position]
            else:
                print("ERROR! Invalid Move")
    return  board

def setBoard(board):
    board[0] = [-2,-3,-4,-5,-6,-4,-3,-2]
    board[1] = [-1]*8
    board[6] = [11]*8
    board[7] = [12,13,14,15,16,14,13,12]
    return board

def printBoard(board):
    print("",end=" ")
    for i in range(8):
        print("|",chr(i+ord('A')),end=" ")
    print("|")
    print(" ","-"*31)
    for i,r in enumerate(board):
        print(str(i+1),end="")
        for j,p in enumerate(r):
            print("|",("%02d" % (p,)),end="")
        print("|"+str(i+1))
        print(" ","-"*31)
    print("",end=" ")
    for i in range(8):
        print("|",chr(i+ord('A')),end=" ")
    print("|")

board = np.zeros((8,8),dtype=int)
board = setBoard(board)
while True:
    printBoard(board)
    m = input(">>> ")
    if re.match(r"[A-Z][0-9]\-\>[A-Z][0-9]",m):
        movePiece(board,m.split("->")[0],m.split("->")[1])