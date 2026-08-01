# from random import randrange

# def initialize_board():
#     """ Initialize the board with numbers 1-9 representing empty squares. """
#     return [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

# def print_board(board):
#     """ Print the current state of the board. """
#     print("+-------+-------+-------+")
#     for row in board:
#         print("|       |       |       |")
#         print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
#         print("|       |       |       |")
#         print("+-------+-------+-------+")

# def check_win(board, player):
#     """ Check if the current player has won. """
#     for row in board:
#         if all([cell == player for cell in row]):
#             return True
#     for col in range(3):
#         if all([board[row][col] == player for row in range(3)]):
#             return True
#     if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
#         return True
#     return False

# def check_tie(board):
#     """ Check if the board is full (tie). """
#     for row in board:
#         for cell in row:
#             if cell not in ['O', 'X']:
#                 return False
#     return True

# def user_move(board):
#     """ Ask user for their move and update the board. """
#     while True:
#         try:
#             move = int(input("Enter your move (1-9): "))
#             if move < 1 or move > 9:
#                 print("Please enter a number between 1 and 9.")
#                 continue
#             row = (move - 1) // 3
#             col = (move - 1) % 3
#             if board[row][col] in ['O', 'X']:
#                 print("That square is already taken. Choose another one.")
#                 continue
#             board[row][col] = 'O'
#             break
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#     print_board(board)

# def computer_move(board):
#     """ Implement computer's move (random choice). """
#     while True:
#         move = randrange(1, 10)
#         row = (move - 1) // 3
#         col = (move - 1) % 3
#         if board[row][col] not in ['O', 'X']:
#             board[row][col] = 'X'
#             break

# def tic_tac_toe_game():
#     board = initialize_board()
#     print("Welcome to Tic-Tac-Toe!")
#     print("You are playing as 'O'. Computer is playing as 'X'.")
#     print_board(board)
    
#     current_player = 'O'
#     while True:
#         if current_player == 'O':
#             user_move(board)
#         else:
#             computer_move(board)
        
#         if check_win(board, current_player):
#             if current_player == 'O':
#                 print("You won!")
#             else:
#                 print("Computer won!")
#             break
        
#         if check_tie(board):
#             print("It's a tie!")
#             break
        
#         current_player = 'X' if current_player == 'O' else 'O'

# if __name__ == "__main__":
#     tic_tac_toe_game()

# from random import randint
    
# for i in range(2):
#     print(randint(1, 2), end=',')
    
# import calendar

# calendar.setfirstweekday(calendar.SUNDAY)
# print(calendar.weekheader(3))

# if __name__ == '__main__':
#     n = int(input().strip())

# if(n%2==0 and n>= 2 and n<=5):
#     print(" Not Weird")
# elif(n%2==0 and n>=6 and n<=20):
#     print("Weird")
# elif(n%2==0 and n > 20):
#     print("Not Weird")
# else: 
#     print("Weird")

def func(a):
    return a


print("Example:")
print(func(3))

# These "asserts" are used for self-checking
assert func(3) == 3
assert func("string") == "string"
assert func(True) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")