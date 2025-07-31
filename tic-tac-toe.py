def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if 0 <= row <= 2 and 0 <= col <= 2:
                    if board[row][col] == " ":
                        break
                    else:
                        print("Position already taken!")
                else:
                    print("Invalid input! Enter numbers between 0-2.")
            except ValueError:
                print("Invalid input! Enter numbers only.")

        board[row][col] = current_player
        winner = check_winner(board)
        
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
            
        if all(all(cell != " " for cell in row) for row in board):
            print_board(board)
            print("It's a tie!")
            break
            
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
