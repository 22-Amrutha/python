#chessdictionary
print("Amrutha, USN:1AY24AI007, SEC:M")
# Initialize chess board
def init_board():
    board = {
        'a1': 'wR', 'b1': 'wN', 'c1': 'wB', 'd1': 'wQ', 'e1': 'wK', 'f1': 'wB', 'g1': 'wN', 'h1': 'wR',
        'a2': 'wP', 'b2': 'wP', 'c2': 'wP', 'd2': 'wP', 'e2': 'wP', 'f2': 'wP', 'g2': 'wP', 'h2': 'wP',
        'a7': 'bP', 'b7': 'bP', 'c7': 'bP', 'd7': 'bP', 'e7': 'bP', 'f7': 'bP', 'g7': 'bP', 'h7': 'bP',
        'a8': 'bR', 'b8': 'bN', 'c8': 'bB', 'd8': 'bQ', 'e8': 'bK', 'f8': 'bB', 'g8': 'bN', 'h8': 'bR',
    }

    # Empty squares
    for row in range(3, 7):
        for col in 'abcdefgh':
            board[f"{col}{row}"] = '  '
    return board

# Print board
def print_board(board):
    for row in range(8, 0, -1):
        for col in 'abcdefgh':
            print(board[f"{col}{row}"], end=' ')
        print()
    print()

# Validate and make move
def make_move(board, move, turn):
    try:
        start, end = move.split()
    except ValueError:
        print("Invalid format. Use 'e2 e4'.")
        return False

    if start not in board or end not in board:
        print("Invalid square.")
        return False

    piece = board[start]
    if piece == '  ':
        print("No piece at starting square.")
        return False

    if not piece.startswith(turn):
        print(f"It's {turn.upper()}'s turn.")
        return False

    # Move (no real rules applied here)
    board[end] = piece
    board[start] = '  '
    return True

# Main loop
def play_game():
    board = init_board()
    turn = 'w'  # white starts
    while True:
        print_board(board)
        move = input(f"{'White' if turn == 'w' else 'Black'} to move (e.g. e2 e4): ").strip().lower()
        if move == "exit":
            break
        if make_move(board, move, turn):
            turn = 'b' if turn == 'w' else 'w'  # switch turns

play_game()