from random import randrange #import function from random library

# initialize board
board = [[i + j*3 + 1 for i in range(3)] for j in range(3)]


#print a board

# +-------+-------+-------+
# |       |       |       |
# |   1   |   2   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   6   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   8   |   9   |
# |       |       |       |
# +-------+-------+-------+

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print(("+"+"-"*7)*3+"+")
    for i in range(3):
        print(("|"+" "*7)*3+"|")
        for j in range(3):
            print("|"+" "*3, end="")
            print(board[i][j], end="")
            print( " "*3, end="")
        print("|") 
        print(("|"+" "*7)*3+"|")   
        print(("+"+"-"*7)*3+"+")
    print("\n")    


display_board(board)


list_free=[]

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    # initialize list of free fields
    for i in range(3):
        for j in range(3):
            if type(board[i][j]) == int:
                my_tuple = (i, j,)
                list_free.append(my_tuple)
    return list_free                

        
make_list_of_free_fields(board) 


currentPlayer = 'X'
board[1][1] = "X"
del_index = list_free.index((1,1))
del list_free[del_index]
display_board(board)

print(make_list_of_free_fields(board))
currentPlayer = 'O'

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.

    player_num = int(input("Enter your move: "))

    for i in range(3):
        for j in range(3):
            if board[i][j] == player_num:
                print(i, j)
                board[i][j] = "O"
                my_tuple = (i, j,)
                index_tuple = list_free.index(my_tuple)
                print(index_tuple)
                del list_free[index_tuple]
    print (board)
    print(list_free)
