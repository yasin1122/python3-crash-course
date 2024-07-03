# This is a classic tic tac toe game

# Ask the first player X or O and choose position
# Print the board
# Ask the 2nd player to choose position

# print the board
positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player_X_choices = []
player_Y_choices = []
choices = ['X', 'Y']
horizontal_line = ' 1 | 2 | 3 '
vertical_line = '-----------------'
winning_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                     (0, 3, 6), (1, 4, 7), (2, 5, 8),
                     (0, 4, 8), (2, 4, 6)]

# print the current board
def print_board():
    for i in range(len(positions)):
        if i==2 or i==5:
            print(' ', positions[i], '  ')
            print(vertical_line)
        elif i==8:
            print(' ', positions[i], '  ')
        else:
            print(' ', positions[i], end='  |')

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

# get user input and fill player choices
def fill_choices(player_choices, ch):
    user_input = None
    prompt = "Enter an integer 1 through 9 (if not taken): "
    while not user_input:
        try:
            print_board()
            user_input = input(prompt)
            user_input = int(user_input)
            if user_input not in positions:
                print(prompt)
                user_input = None
            else:
                player_choices.append(user_input)
                if ch == 'X':
                    positions[user_input - 1] = 'X'
                elif ch == 'Y':
                    positions[user_input - 1] = 'Y'
        except Exception as error:
            print(error, prompt)
            user_input = None

fill_choices(player_X_choices, 'X')
fill_choices(player_Y_choices, 'Y')
print(player_X_choices, player_Y_choices)