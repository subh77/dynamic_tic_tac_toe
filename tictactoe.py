# game = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]


# def game_board(game_map, player=0, row=0, column=0, just_display=True):
#     try:
#         print("   a  b  c")
#         if just_display:
#             game_map[row][column] = player
#         for count, i in enumerate(game):
#             print(count, i)
#         return game_map
#     except IndexError as e:
#         print("Make sure your input is in between 0, 1 and 2. \n Error:", e)
#     except Exception as e:
#         print("Something went wery wrong \n Error:", e)


# game = game_board(game, just_display=False)
# game = game_board(game, player=1, row=2, column=1)


game = [[0, 1, 2], [1, 2, 2], [2, 0, 1]]


def win(cg):
    # horizontal winner
    for row in cg:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print("Winner Horizontally")
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
        print(col)
        if col.count(col[0]) == len(col) and col[0] != 0:
            print("Winner Vertically")

    # diagonal winner
    def dg_win(current_game):
        dg_val = []
        for i in range(len(current_game)):
            dg_val.append(current_game[i][i])
        print(dg_val)
        if dg_val.count(dg_val[0]) == len(dg_val) and dg_val[0] != 0:
            print("Winner Diagonally")

    dg_win(cg)
    cg2 = cg[::-1]
    dg_win(cg2)


win(game)
