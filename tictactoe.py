game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def game_board():
    print("   a  b  c")
    for count, row in enumerate(game):
        print(count, row)


game_board()