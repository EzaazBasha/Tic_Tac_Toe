def print_board(board):
    for row in board:
        rows = " | ".join(row)
        print(rows)
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        winner = True
        for cell in row:
            if cell != player:
                winner = False
                break
        if winner:
            return True
    
    for col in range(3):
        winner = True
        for row in range(3):
            if board[row][col] != player:
                winner = False
                break
        if winner:
            return True
    
    if (board[0][0] == board[1][1] == board[2][2] == player) or (board[0][2] == board[1][1] == board[2][0] == player):
        return True
    
    return False

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
        col = int(input(f"Player {current_player}, enter column (0, 1, or 2): "))
        
        if board[row][col] == " ":
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"
        else:
            print("That spot is already taken. Try again.")

play_game()
