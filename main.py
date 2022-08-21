# This program allows for 2 players to play tic tac toe against each other or provides the user the option to play against a CPU

row_one = ["1", "2", "3"]
row_two = ["4", "5", "6"]
row_three = ["7", "8", "9"]
rows = [row_one, row_two, row_three]
spacing_row = "---------"
available_spots = [i for i in range(1, 10)]
game_over = False
winning_combos = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7], [1, 4, 7], [2, 5, 8], [3, 6, 9]]
player_one_owned = []
player_two_owned = []


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
        elif placement > 9:
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
    if placement == 0:
        pass
    elif 1 <= placement <= 3:
        row_one[list_index] = symbol
    elif 4 <= placement <= 6:
        row_two[list_index] = symbol
    elif 7 <= placement <= 9:
        row_three[list_index] = symbol

    for i in range(3):
        print(*rows[i], sep=" | ")
        if i < 2:
            print(spacing_row)


refresh_board("", 0)
turn = 1
while not game_over:
    player_move((turn % 2))
    turn += 1
    for winners in winning_combos:
        player_one_check = all(item in player_one_owned for item in winners)
        player_two_check = all(item in player_two_owned for item in winners)
        if player_one_check:
            print("player one wins")
            game_over = True
        if player_two_check:
            print("player two wins")
            game_over = True
        else:
            pass
    if not available_spots:
        game_over = True
        print("It's a tie!")