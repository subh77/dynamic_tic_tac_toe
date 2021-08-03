import itertools
from modules.win import win
from modules.board import game_board


def main():
    play = True
    while play:
        game_size = int(input("Enter the grid size for tic-tac-toe:  "))
        game = [[0 for i in range(game_size)] for i in range(game_size)]
        game_won = False
        game_val, _ = game_board(game, just_display=False)
        player_choice = itertools.cycle(range(1, 3))

        while not game_won:
            current_player = next(player_choice)
            print(f"Current player is {current_player}")
            played = False

            while not played:
                row_choice = int(input("Enter your row position : "))
                col_choice = int(input("Enter your col position : "))
                game_val, played = game_board(
                    game, current_player, row_choice, col_choice
                )

            if win(game):
                game_won = True
                again = input("The game is over, would you like to play again? (y/n) ")
                if again.lower() == "y":
                    print("\n \n Restarting")
                elif again.lower() == "n":
                    print("Bbye")
                    play = False
                else:
                    print(
                        "Not a valid input... I'm just a computer pls don't torture me"
                    )
                    play = False


if __name__ == "__main__":
    main()