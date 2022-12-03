# My solution to JetBrains Academy Last Pencil Project


# getting the number of pencils
def get_pencils():
    while True:
        number_of_pencils = input()
        # if number of pencils is digit
        if number_of_pencils.isdigit():
            # if number of pencils is positive
            if int(number_of_pencils) > 0:
                return int(number_of_pencils)
            else:
                print("The number of pencils should be positive")
        else:
            print("The number of pencils should be numeric")


# getting the first player
def get_first_player(players_list):
    while True:
        first_player = input()
        if first_player not in players_list:
            print(f"Choose between' {players_list[0]}' and '{players_list[1]}'")
        # returning player1 or player2
        elif first_player == players_list[0]:
            return 0
        elif first_player == players_list[1]:
            return 1


# checking if player move is correct
def move(number_of_pencils):
    while True:
        player_move = input()
        # if number of pencils is digit
        if player_move.isdigit():
            # if number of pencils is 1 or 2 or 3
            if player_move in ("1", "2", "3"):
                # if number of pencils taken isn't bigger than pencils left
                if number_of_pencils - int(player_move) >= 0:
                    return int(player_move)
                else:
                    print("Too many pencils were taken")
            else:
                print("Possible values: '1', '2' or '3'")
        else:
            print("Possible values: '1', '2' or '3'")


# game loop
def game(number_of_pencils, player_turn, players_list):
    while number_of_pencils > 0:
        print("|" * number_of_pencils)
        print(f"{players_list[player_turn]}'s turn: ")
        number_of_pencils -= min(number_of_pencils, move(number_of_pencils))
        player_turn ^= 1
    print(f"{players_list[player_turn]} won!")


# declaring players
player_name = input("What's your name? \n")
players = [player_name, "Bot"]

# getting the number of pencils
print("How many pencils would you like to use: ")
pencils = get_pencils()

# declaring the starting player
print(f"Who will be the first ({players[0]}, {players[1]}): ")
turn = get_first_player(players)

# game
game(pencils, turn, players)