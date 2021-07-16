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