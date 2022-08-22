# This program allows for 2 players to play tic tac toe against each other or provides the user the option to play against a CPU
import random

row_one = ["1", "2", "3"]
row_two = ["4", "5", "6"]
row_three = ["7", "8", "9"]
rows = [row_one, row_two, row_three]
blank_row = [" ", " ", " "]
spacing_row = "---------"
game_over = False
winning_combos = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7], [1, 4, 7], [2, 5, 8], [3, 6, 9]]
player_one_wins = 0
player_two_wins = 0
computer_wins = 0





def player_placement(symbol):
    valid_choice = False
    while not valid_choice:
        placement = int(input("Which spot would you like to pick: "))
        if placement in available_spots:
            valid_choice = True
            available_spots.remove(placement)
            if symbol == 'X':
                player_one_owned.append(placement)
            elif symbol == "O":
                player_two_owned.append(placement)
            refresh_board(symbol, placement)
        elif 1 > placement > 9:
            print("Invalid space chosen, Please pick another space")
        else:
            print("That spot is already taken, please chose another spot")


def player_move(player):
    if player == 1:
        symbol = 'X'
    else:
        symbol = "O"
    player_placement(symbol)


def refresh_board(symbol, placement):
    list_index = (placement - 1) % 3
    if 1 <= placement <= 3:
        row_one[list_index] = symbol
    elif 4 <= placement <= 6:
        row_two[list_index] = symbol
    elif 7 <= placement <= 9:
        row_three[list_index] = symbol

    for i in range(3):
        print(*rows[i], sep=" | ")
        if i < 2:
            print(spacing_row)


def get_play_type():
    valid_play_type = False
    while not valid_play_type:
        option = input(
            "Would you like to play with another person or against the computer? (P for person and C for computer): ")
        if option.upper() == "P" or option.upper() == "C":
            valid_play_type = True
            return option.upper()
        else:
            print("That is not a valid option. Please choose P for player or C for computer)")

def computer_move(mode):
    symbol = "O"
    if mode == 1:
        placement = random.choice(available_spots)
        available_spots.remove(placement)
        computer_owned.append(placement)
        refresh_board(symbol, placement)



print("Welcome to tic-tac-toe!")
play_style = get_play_type()
start_new_game = True
while not game_over:
    if start_new_game:
        turn = 1
        start_new_game = False
        row_one = ["1", "2", "3"]
        row_two = ["4", "5", "6"]
        row_three = ["7", "8", "9"]
        rows = [row_one, row_two, row_three]
        player_one_owned = []
        player_two_owned = []
        computer_owned = []
        available_spots = [i for i in range(1, 10)]
        refresh_board("", 0)
    if play_style == "P":
        if turn % 2 == 1:
            print("It is player one's Turn")
        else:
            print("It is player two's turn")
        player_move((turn % 2))
    elif play_style == "C":
        if turn % 2 == 1:
            print("It is player one's Turn")
            player_move(1)
        else:
            print("It is the computers turn")
            computer_move(1)


    turn += 1
    for winners in winning_combos:
        player_one_check = all(item in player_one_owned for item in winners)
        player_two_check = all(item in player_two_owned for item in winners)
        computer_check = all(item in computer_owned for item in winners)

        if player_one_check:
            print("player one wins")
            game_over = True
            player_one_wins += 1
        elif player_two_check:
            print("player two wins")
            game_over = True
            player_two_wins += 1
        elif computer_check:
            print("The computer wins")
            game_over = True
            computer_wins += 1

        else:
            pass
    if not available_spots:
        game_over = True
        print("It's a tie!")
    if game_over:
        play_again = input("Would you like to play another game?(Y or N): ")
        if play_again.upper() == "Y":
            game_over = False
            start_new_game = True
        else:
            continue


print(f"Thanks for playing! Player 1 has {player_one_wins} win(s), Player 2 has {player_two_wins} win(s), and the computer has {computer_wins} win(s)")