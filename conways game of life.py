import time

def print_board(board):
    for row in board:
        print(''.join(['█' if cell else ' ' for cell in row]))
    print()

def get_neighbors(board, x, y):
    neighbors = 0
    rows, cols = len(board), len(board[0])
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if (i == x and j == y) or i < 0 or j < 0 or i >= rows or j >= cols:
                continue
            neighbors += board[i][j]
    return neighbors

def next_generation(board):
    rows, cols = len(board), len(board[0])
    new_board = [[0]*cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            neighbors = get_neighbors(board, i, j)
            if board[i][j] == 1 and neighbors in [2, 3]:
                new_board[i][j] = 1
            elif board[i][j] == 0 and neighbors == 3:
                new_board[i][j] = 1
    return new_board

# Example: glider pattern
board = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
]

for _ in range(10):
    print_board(board)
    board = next_generation(board)
    time.sleep(0.5)


