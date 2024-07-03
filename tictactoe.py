# This is a classic tic tac toe game

# Ask the first player X or O and choose position
# Print the board
# Ask the 2nd player to choose position

# print the board
positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player1_choices = []
player2_choices = []
choices = ['X', 'O']
horizontal_line = ' 1 | 2 | 3 '
vertical_line = '-----------------'
winning_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                     (0, 3, 6), (1, 4, 7), (2, 5, 8),
                     (0, 4, 8), (2, 4, 6)]

# print the current board
def print_board(choice):
    positions[choice-1] = 'X'
    for i in range(len(positions)):
        if i==2 or i==5:
            print(' ', positions[i], '  ')
            print(vertical_line)
        elif i==8:
            print(' ', positions[i], '  \n\n')
        else:
            print(' ', positions[i], end='  |')

print_board(1)
print_board(2)

# import random
# print(random.choice([1,2]))

# check if a player won
def win_check(player_choices):
    for winning_tuple in winning_positions:
        if (winning_tuple[0] in player_choices and
            winning_tuple[1] in player_choices and
            winning_tuple[2] in player_choices):
            return True
    return False

win_check([8, 3, 4, 0, 7])

print((1, 2, 3) not in [0, 1, 2, 3])