# My solution to JetBrains Academy Last Pencil Project
# Made by github.com/tukarp


# getting the number of pencils
def get_pencils():
    print("How many pencils would you like to use: ")
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
def get_first_player(players):
    print(f"Who will be the first ({players[0]}, {players[1]}): ")
    while True:
        first_player = input()
        if first_player not in players:
            print(f"Choose between' {players[0]}' and '{players[1]}'")
        else:
            # returning player1 or player2
            if first_player == players[0]:
                return 0
            elif first_player == players[1]:
                return 1


# checking if player move is correct
def move(pencils, players, turn):
    # player move
    if turn == 0:
        print(f"{players[turn]}'s turn: ")
        while True:
            player_move = input()
            # if number of pencils is digit
            if player_move.isdigit():
                # if number of pencils is 1 or 2 or 3
                if player_move in ("1", "2", "3"):
                    # if number of pencils taken isn't bigger than pencils left
                    if pencils - int(player_move) >= 0:
                        return int(player_move)
                    else:
                        print("Too many pencils were taken")
                else:
                    print("Possible values: '1', '2' or '3'")
            else:
                print("Possible values: '1', '2' or '3'")
    # bot move
    else:
        # bot strategies for winning
        print(f"{players[turn]}'s turn: ")
        if pencils % 4 == 0:
            bot_move = 3
        elif pencils % 4 == 3:
            bot_move = 2
        elif pencils % 4 == 2:
            bot_move = 1
        else:
            bot_move = 1
        print(bot_move)
        return bot_move


# game loop
def game(pencils, players, turn):
    while pencils > 0:
        print("|" * pencils)
        pencils -= move(pencils, players, turn)
        turn ^= 1
    print(f"{players[turn]} won!")


# start game
def start_game():
    # declaring players
    player_name = input("What's your name? \n")
    bot_name = "Bot"
    players = [player_name, bot_name]

    # getting the number of pencils
    pencils = get_pencils()

    # declaring the starting player
    turn = get_first_player(players)

    # game
    game(pencils, players, turn)


# starting game
start_game()
