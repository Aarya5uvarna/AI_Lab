# Tic Tac Toe

def print_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def check_winner(board, player):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


def tic_tac_toe():
    board = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]

    player = "X"

    for turn in range(9):
        print_board(board)

        position = int(input("Player " + player + ", enter position (1-9): ")) - 1

        if board[position] in ["X", "O"]:
            print("Position already occupied. Try again.")
            continue

        board[position] = player

        if check_winner(board, player):
            print_board(board)
            print("Player", player, "wins!")
            return

        if player == "X":
            player = "O"
        else:
            player = "X"

    print_board(board)
    print("It's a draw!")


tic_tac_toe()