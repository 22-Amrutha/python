import time
import os
import copy

# Size of the grid
WIDTH = 20
HEIGHT = 10

# Initial pattern (glider)
grid = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
grid[1][2] = 1
grid[2][3] = 1
grid[3][1] = 1
grid[3][2] = 1
grid[3][3] = 1

# Function to print the grid
def print_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print(''.join(['O' if cell else '.' for cell in row]))
    print()

# Count live neighbors
def count_neighbors(grid, x, y):
    neighbors = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < HEIGHT and 0 <= ny < WIDTH:
                neighbors += grid[nx][ny]
    return neighbors

# Update grid based on rules
def update_grid(grid):
    new_grid = copy.deepcopy(grid)
    for i in range(HEIGHT):
        for j in range(WIDTH):
            neighbors = count_neighbors(grid, i, j)
            if grid[i][j] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[i][j] = 0
            elif grid[i][j] == 0 and neighbors == 3:
                new_grid[i][j] = 1
    return new_grid

# Run the game loop
def run_game(steps=100, delay=0.3):
    global grid
    for _ in range(steps):
        print_grid(grid)
        grid = update_grid(grid)
        time.sleep(delay)

run_game()