from colorama import Fore, Back, Style, init

init()


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
        for count, i in enumerate(game_map):
            colored_row = ""
            for item in i:
                if item == 0:
                    colored_row += "   "
                elif item == 1:
                    colored_row += Fore.GREEN + " X " + Style.RESET_ALL
                elif item == 2:
                    colored_row += Fore.RED + " O " + Style.RESET_ALL
            print(count, colored_row)
        return game_map, True

    except IndexError as e:
        print("Make sure your input is in between 0, 1 and 2. \n Error:", e)
        return game_map, False

    except Exception as e:
        print("Something went wery wrong \n Error:", e)
        return game_map, False
