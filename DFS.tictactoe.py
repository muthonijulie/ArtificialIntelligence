def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def is_moves_left(board):
    for row in board:
        if " " in row:
            return True
    return False

def evaluate(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return 10 if row[0] == "X" else -10
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return 10 if board[0][col] == "X" else -10
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return 10 if board[0][0] == "X" else -10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return 10 if board[0][2] == "X" else -10
    return 0

def dfs(board, is_X_turn):
    if not is_moves_left(board) or evaluate(board) in [10, -10]:
        return board
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X" if is_X_turn else "O"
                result = dfs(board, not is_X_turn)
                if evaluate(result) in [10, -10]:
                    return result
                board[i][j] = " "
    return board

def is_winner(board, player):
    return evaluate(board) == (10 if player == "X" else -10)

def is_draw(board):
    return not is_moves_left(board) and evaluate(board) == 0

def user_vs_computer():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("User vs Computer")
    user_turn = input("Do you want to be X or O? ").upper()
    computer_turn = "O" if user_turn == "X" else "X"
    
    current_turn = "X"

    while is_moves_left(board):
        print_board(board)
        if current_turn == user_turn:
            print("Your turn")
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if board[row][col] == " ":
                board[row][col] = user_turn
                if is_winner(board, user_turn):
                    print_board(board)
                    print("You win!")
                    return
                current_turn = computer_turn
            else:
                print("Invalid move. Try again.")
        else:
            print("Computer's turn")
            new_board = dfs(board, False)
            if new_board:
                board = new_board
                if is_winner(board, computer_turn):
                    print_board(board)
                    print("Computer wins!")
                    return
            current_turn = user_turn

    if is_draw(board):
        print_board(board)
        print("It's a draw!")

def two_player():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Two Player Game")

    current_turn = "X"

    while is_moves_left(board):
        print_board(board)
        print(f"{current_turn}'s turn")
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))
        if board[row][col] == " ":
            board[row][col] = current_turn
            if is_winner(board, current_turn):
                print_board(board)
                print(f"{current_turn} wins!")
                return
            current_turn = "O" if current_turn == "X" else "X"
        else:
            print("Invalid move. Try again.")

    if is_draw(board):
        print_board(board)
        print("It's a draw!")

def main():
    mode = input("Enter 1 for User vs Computer or 2 for Two Player: ")
    if mode == "1":
        user_vs_computer()
    elif mode == "2":
        two_player()
    else:
        print("Invalid input. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
