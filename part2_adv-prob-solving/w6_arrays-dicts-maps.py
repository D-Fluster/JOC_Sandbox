# 2024 Danielle K. Fluster
# Joy of Coding Academy
# Part 2 - Advanced Problem Solving
# Week 6 - Arrays, Dictionaries & Maps

from danimo import *

spacing(1, "*", 55)
problem1 = "Import Text File Line by Line; Return Certain Lines; Count Total Lines"
print(problem1)
spacing(1, "=", len(problem1)//2)

# Basic In-Line Program

# turingText = open("turing.txt", "r")
#
# turingRead = []
#
# for line in turingText:
#     turingRead.append(line)
# turingText.close()
#
# # print(turingRead)
#     # Works as expected!
#
# print("The first 2 elements are: \n", turingRead[:2], "\n")
# print("The last 2 elements are: \n", turingRead[-2:], "\n")
# print("The file has the following number of lines: \n", len(turingRead))



# DRYer, More Generalizable Program with Comments

def file_readLines(file):
    fileText = open(file, "r")
    fileRead = []                       # Initialize an empty set to store each line of the file
    for line in fileText:               # Read each line of the file into an element of the array
        fileRead.append(line)
    fileText.close()                    # Close the file
    first2Lines = fileRead[:2]          # Identify the first & last 2 lines of the file
    last2Lines  = fileRead[-2:]             # (i.e., first & last 2 elements of the array)
    totalLines  = len(fileRead)         # Calculate the total number of lines in the file
    print(f"The first 2 lines in this file are: \n {first2Lines} \n")
    print(f"The last 2 lines in this file are: \n {last2Lines} \n")
    print(f"The file has the following number of lines: \n {totalLines}")

def main():
    file_readLines("turing.txt")

main()





spacing(1, "*", 55)
problem2 = "2D Arrays & Tic-Tac-Toe"
print(problem2)
spacing(1, "=", -(-len(problem2)//2))
    # Can use ceil() for ceiling divison, or equivalently double negation of floor division

# testList = ["A", 2, "C"]        # ["A", 2, "C", "A", 2, "C", "A", 2, "C"]
# testList = [["A", 2, "C"]]      # [['A', 2, 'C'], ['A', 2, 'C'], ['A', 2, 'C']]
# print(testList * 3)



# Basic Function

# def didIwin_colRight(player, board):
#     if board[0][2] == board[1][2] == board[2][2] == player:
#         return True
#     else:
#         return False
#
#     # for i in range(3):
#     # return X



# DRYer-ish, More Generalizable Function

def didIwin_colRight(player, board):
    winner = False
    matches = []
    for i in range(len(board)):
        if board[i][2] == player:
            matches.append(True)
        else:
            matches.append(False)
    if False not in matches:
        winner = True
    return winner



# Dr. Emily's Solution

def didIwin_colRight_DrEm(player, board):
    winner = True
    for i in range(len(board)):
        winner &= board[i][2] == player
    return winner

def main2():
    board1_2 = [['O', 'O', 'X'], \
            ['O', 'X', 'O'], \
            ['X', 'O', 'O']]
    player1 = "X"
    expRes1 = False

    player2 = "O"
    expRes2 = False

    board3_4 = [['O', 'O', 'X'], \
            ['O', 'O', 'X'], \
            ['O', 'O', 'X']]
    player3 = "X"
    expRes3 = True

    player4 = "O"
    expRes4 = False

    print(didIwin_colRight(player1, board1_2), expRes1)
    print(didIwin_colRight(player2, board1_2), expRes2)
    print(didIwin_colRight(player3, board3_4), expRes3)
    print(didIwin_colRight(player4, board3_4), expRes4)
    spacing(0, "-", 11)
    print(didIwin_colRight_DrEm(player1, board1_2), expRes1)
    print(didIwin_colRight_DrEm(player2, board1_2), expRes2)
    print(didIwin_colRight_DrEm(player3, board3_4), expRes3)
    print(didIwin_colRight_DrEm(player4, board3_4), expRes4)

# main2()



def didIwin_cols(player, board):
    winner_col0 = True
    winner_col1 = True
    winner_col2 = True
    for i in range(len(board)):
        winner_col0 &= board[i][0] == player
        winner_col1 &= board[i][1] == player
        winner_col2 &= board[i][2] == player
        # for j in range(len(board)):
        #     winner &= board[i][j] == player
    winner = winner_col0 or winner_col1 or winner_col2
    return winner

    # winner = True
    # for i in range(len(board)):
    #     winner &= (board[i][0] == player) \
    #             or (board[i][1] == player) \
    #             or (board[i][2] == player)
    #         # for j in range(len(board)):
    #     #     winner &= board[i][j] == player
    # return winner



# Dr. Emily's Solution

def didIwin_cols_DrEm(player, board):
    did_win = False
    for i in range(len(board)):
        col_win = True
        for j in range(len(board[i])):
            col_win &= player == board[j][i]    # Why not [i][j]? Seems to be the same when run, but why?
        did_win |= col_win
    return did_win

def main3():
    board1 = [['O', 'O', 'X'], \
              ['O', 'X', 'O'], \
              ['X', 'O', 'O']]

    board2 = [['O', 'O', 'X'], \
              ['O', 'O', 'X'], \
              ['O', 'O', 'X']]

    board3 = [["X", "O", "O"], \
              ["X", "O", "X"], \
              ["X", "X", "X"]]

    player1 = "X"
    player2 = "O"

    expRes1 = False     # Board 1, Player 1
    expRes2 = False     # Board 1, Player 2
    expRes3 = True      # Board 2, Player 1
    expRes4 = True     # Board 2, Player 2

    print(didIwin_cols(player1, board1), expRes1)
    print(didIwin_cols(player2, board1), expRes2)
    print(didIwin_cols(player1, board2), expRes3)
    print(didIwin_cols(player2, board2), expRes4)
    spacing(0, "-", 11)
    print(didIwin_cols_DrEm(player1, board1), expRes1)
    print(didIwin_cols_DrEm(player2, board1), expRes2)
    print(didIwin_cols_DrEm(player1, board2), expRes3)
    print(didIwin_cols_DrEm(player2, board2), expRes4)
    spacing(0, "-", 11)
    print(didIwin_cols(player1, board3))
    print(didIwin_cols_DrEm(player1, board3))
    print(didIwin_cols(player2, board3))
    print(didIwin_cols_DrEm(player2, board3))


main3()