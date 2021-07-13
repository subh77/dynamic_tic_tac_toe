game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def game_board(game_map, player=0, row=0, column=0, just_display=True):
    print("   a  b  c")
    if just_display:
        game_map[row][column] = player
    for count, i in enumerate(game):
        print(count, i)
    return game_map


game = game_board(game, just_display=False)
game = game_board(game, player=1, row=2, column=1)