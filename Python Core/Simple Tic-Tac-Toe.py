# My solution to JetBrains Academy Simple Tic-Tac-Toe Project


# building grid
def build_grid(grid):
    print("---------")
    print(f"| {grid[0]} {grid[1]} {grid[2]} |")
    print(f"| {grid[3]} {grid[4]} {grid[5]} |")
    print(f"| {grid[6]} {grid[7]} {grid[8]} |")
    print("---------")


# checking winning conditions
def win_conditions_check(grid, symbol):
    # symbol horizontally top
    if grid[0] == symbol and grid[1] == symbol and grid[2] == symbol:
        return 1

    # symbol horizontally middle
    elif grid[1] == symbol and grid[4] == symbol and grid[7] == symbol:
        return 1

    # symbol horizontally down
    elif grid[6] == symbol and grid[7] == symbol and grid[8] == symbol:
        return 1

    # symbol vertically left
    elif grid[0] == symbol and grid[3] == symbol and grid[6] == symbol:
        return 1

    # symbol vertically middle
    elif grid[3] == symbol and grid[4] == symbol and grid[5] == symbol:
        return 1

    # symbol vertically right
    elif grid[2] == symbol and grid[5] == symbol and grid[8] == symbol:
        return 1

    # symbol diagonally from top left
    elif grid[0] == symbol and grid[4] == symbol and grid[8] == symbol:
        return 1

    # symbol diagonally from top right
    elif grid[2] == symbol and grid[4] == symbol and grid[6] == symbol:
        return 1

    # symbol doesn't match any winning conditions
    else:
        return 0


# getting the game result
def checking_game_result(grid):
    # checking X
    x_status = win_conditions_check(grid, "X")
    # checking O
    o_status = win_conditions_check(grid, "O")

    # checking game results
    # x won
    if (x_status == 1) and (o_status == 0):
        print("X wins")
        quit()
    # o won
    elif (o_status == 1) and (x_status == 0):
        print("O wins")
        quit()
    # draw
    elif ((x_status == 0) and (o_status == 0)) and (has_empty_cells(grid) is False):
        print("Draw")
        quit()
    # game is not finished
    else:
        return False


# game loop
def game_loop(grid, symbol):
    while True:
        try:
            # getting input
            row, column = input().split()
            # checking if row and column are numbers
            if row.isdigit() and column.isdigit():
                # checking if row and column are in rage 1 to 3
                if row in ["1", "2", "3"] and column in ["1", "2", "3"]:
                    # calculating move
                    move = ((((int(row) - 1) * 3) + (int(column) + 2)) - 3)
                    if grid[move] == "_":
                        grid = replace_str_index(grid, move, symbol)
                        build_grid(grid)
                        checking_game_result(grid)
                        return grid
                    else:
                        print("This cell is occupied! Choose another one!")
                else:
                    print("Coordinates should be from 1 to 3!")
            else:
                print("You should enter numbers!")
        except ValueError:
            print("You should enter numbers!")


# checking if grid has empty cells
def has_empty_cells(grid):
    if (grid[0] == "_") or (grid[1] == "_") or (grid[2] == "_") or (grid[3] == "_") or (grid[4] == "_") \
            or (grid[5] == "_") or (grid[6] == "_") or (grid[7] == "_") or (grid[8] == "_"):
        return True
    else:
        return False


# replacing character at given index
def replace_str_index(text, index=0, replacement=''):
    return '%s%s%s' % (text[:index], replacement, text[index + 1:])


# starting game
def start_game():
    # symbols
    symbols_list = ["X", "O"]
    symbol_counter = 1

    # building empty grid
    grid = "_________"
    build_grid(grid)

    # game loop
    while checking_game_result(grid) is False:
        symbol_counter ^= 1
        print(f"{symbols_list[symbol_counter]} move:")
        grid = game_loop(grid, symbols_list[symbol_counter])


# starting game
start_game()
