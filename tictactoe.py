import itertools


def win(cg):
    def win_condition(condition):
        if condition.count(condition[0]) == len(condition) and condition[0] != 0:
            return True
        else:
            return False

    # horizontal winner
    for row in cg:
        if win_condition(row):
            print(f"Winner Horizontally is Player {row[0]}")
            return True
        # I have a problem with over engineering simple solutions help me!
        # The below code block is more optimized for cases where it finds unmatching elements with the 1st list element (since it breaks and stops checking)
        # set_flag = True
        # print(row)
        # for item in row:
        #     if row[0] != item:
        #         set_flag = False
        #         break
        # if set_flag == True:
        #     print("Winner")

    # vertical winner
    for i in range(len(cg)):
        col = []
        for row in cg:
            col.append(row[i])
        if win_condition(col):
            print(f"Winner Vertically is Player {col[0]}")
            return True

    # diagonal winner
    def dg_win(current_game):
        dg_val = []
        for i in range(len(current_game)):
            dg_val.append(current_game[i][i])
        if win_condition(dg_val):
            print(f"Winner Diagonally is Player {dg_val[0]}")
            return True

    if dg_win(cg):
        return True
    cg2 = cg[::-1]
    if dg_win(cg2):
        return True

    return False


def game_board(game_map, player=0, row=0, column=0, just_display=True):
    try:
        if game_map[row][column] != 0:
            print("This position has already been played")
            return game_map, False
        print(
            "   " + "  ".join([str(i) for i in range(len(game_map))])
        )  # list comprehension, equivalent to print("   0  1  2")
        if just_display:
            game_map[row][column] = player
        for count, i in enumerate(game):
            print(count, i)
        return game_map, True
    except IndexError as e:
        print("Make sure your input is in between 0, 1 and 2. \n Error:", e)
        return game_map, False
    except Exception as e:
        print("Something went wery wrong \n Error:", e)
        return game_map, False


play = True
while play:
    game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    game_won = False
    game_val, _ = game_board(game, just_display=False)
    player_choice = itertools.cycle(range(1, 3))

    while not game_won:
        current_player = next(player_choice)
        print(f"Current player is {current_player}")
        played = False

        while not played:
            row_choice = int(input("Enter your row position. (0,1,2): "))
            col_choice = int(input("Enter your col position. (0,1,2): "))
            game_val, played = game_board(game, current_player, row_choice, col_choice)

        if win(game):
            game_won = True
            again = input("The game is over, would you like to play again? (y/n) ")
            if again.lower() == "y":
                print("\n \n Restarting")
            elif again.lower() == "n":
                print("Bbye")
                play = False
            else:
                print("Not a valid input... I'm just a computer pls don't torture me")
                play = False