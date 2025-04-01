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


# initialize list of free fields
list_free=[]

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    for i in range(3):
        for j in range(3):
            my_tuple = (i, j,)
            list_free.append(my_tuple)

        
make_list_of_free_fields(board) 
print(list_free)


