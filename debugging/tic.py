def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        row = input("Enter row (0, 1, or 2) for player " + player + ": ")
        col = input("Enter column (0, 1, or 2) for player " + player + ": ")
        if row.isdigit() and col.isdigit() and 0 <= int(row) <= 2 and 0 <= int(col) <= 2:
            row = int(row)
            col = int(col)
            if board[row][col] == " ":
                board[row][col] = player
                if check_winner(board):
                    print_board(board)
                    print("Player " + player + " wins!")
                    break
                elif check_draw(board):
                    print_board(board)
                    print("It's a draw!")
                    break
                else:
                    if player == "X":
                        player = "O"
                    else:
                        player = "X"
            else:
                print("That spot is already taken! Try again.")
        else:
            print("Invalid input. Please enter numbers only between 0 and 2.")

if __name__ == "__main__":
    tic_tac_toe()
