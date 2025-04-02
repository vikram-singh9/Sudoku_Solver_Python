def find_empty(board):
    """Finds the first empty cell (represented by 0) in the board."""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)  # row, col
    return None

def is_valid(board, num, pos):
    """Checks if placing 'num' at 'pos' is a valid move."""
    # Check row
    for col in range(len(board[0])):
        if board[pos[0]][col] == num and pos[1] != col:
            return False

    # Check column
    for row in range(len(board)):
        if board[row][pos[1]] == num and pos[0] != row:
            return False

    # Check 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for row in range(box_y * 3, box_y * 3 + 3):
        for col in range(box_x * 3, box_x * 3 + 3):
            if board[row][col] == num and (row, col) != pos:
                return False

    return True

def solve(board):
    """Solves the Sudoku board using backtracking."""
    find = find_empty(board)
    if not find:
        return True  # Board is full, solution found
    else:
        row, col = find

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0  # Backtrack

    return False

def print_board(board):
    """Prints the Sudoku board in a readable format."""
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

# Example Sudoku puzzle
example_board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

print("Original Board:")
print_board(example_board)

solve(example_board)

print("\nSolved Board:")
print_board(example_board)