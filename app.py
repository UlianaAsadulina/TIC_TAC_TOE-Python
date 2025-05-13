from random import randrange, choice #import function from random library

# initialize board
board = [[i + j*3 + 1 for i in range(3)] for j in range(3)]


# print a board

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

        
list_free = make_list_of_free_fields(board) 

winner= None
currentPlayer = 'X'
board[1][1] = "X"
del_index = list_free.index((1,1))
del list_free[del_index]
display_board(board)

my_turn = True



def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.

    player_num = int(input("Enter your move: "))
    currentPlayer = 'O'
    for i in range(3):
        for j in range(3):
            if board[i][j] == player_num:
                # print(i, j)
                board[i][j] = currentPlayer
                my_tuple = (i, j,)
                index_tuple = list_free.index(my_tuple)
                # print(index_tuple)
                del list_free[index_tuple]
    display_board(board)



def check_num(board, num, player):
    number_isFree = False
    for i in range(3):
        for j in range(3):
            if board[i][j] == num:
                number_isFree = True
                print(i, j)
                board[i][j] = player
                my_tuple = (i, j,)
                index_tuple = list_free.index(my_tuple)
                print(index_tuple)
                del list_free[index_tuple]
    if number_isFree:
        print("Move ", num)   
        display_board(board)     
    else:
        print("This number already taken")
        print("Select another number")
        draw_move(board)



def draw_move(board):
    # The function draws the computer's move and updates the board.
    currentPlayer = 'X'
    player_num = randrange(1, 10)
    check_num(board, player_num, currentPlayer)



print(list_free)
# random_pair = choice(list_free)
# print(random_pair)

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    winner = None
    if board[0][0] == board [1][1] == board [2][2] == sign:
        winner = sign
    elif board [0][2] == board[1][1] == board[2][0] == sign:
        winner = sign
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == sign:
            winner = sign
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == sign:
            winner = sign   
    return winner

winner = victory_for(board, currentPlayer)    
print(winner)



while len(list_free):
	display_board(board)
	if my_turn:
		enter_move(board)
		winner = victory_for(board,'O')
	else:	
		draw_move(board)
		winner = victory_for(board,'X')
	if winner != None:
		break
	my_turn = not my_turn		
	free = make_list_of_free_fields(board)

display_board(board)
if winner == 'O':
	print("You won!")
elif winner == 'X':
	print("Computer won")
else:
	print("Tie!")