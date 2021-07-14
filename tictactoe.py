game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def game_board(game_map, player=0, row=0, column=0, just_display=True):
    try:
        print("   a  b  c")
        if just_display:
            game_map[row][column] = player
        for count, i in enumerate(game):
            print(count, i)
        return game_map
    except IndexError as e:
        print("Make sure your input is in between 0, 1 and 2. \n Error:", e)
    except Exception as e:
        print("Something went wery wrong \n Error:", e)


game = game_board(game, just_display=False)
game = game_board(game, player=1, row=2, column=1)