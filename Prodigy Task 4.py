def print_board(board):
    """Prints the Sudoku board."""
    for row in board:
        print(" ".join(str(num) for num in row))

def find_empty_location(board):
    """Finds an empty cell in the Sudoku board. Returns (row, col) or None if full."""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # 0 represents an empty cell
                return row, col
    return None

def is_safe(board, row, col, num):
    """Checks if it's safe to place a number in the specified cell."""
    # Check row
    if num in board[row]:
        return False
    
    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False
    
    # Check 3x3 box
    box_row_start = row - row % 3
    box_col_start = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[box_row_start + i][box_col_start + j] == num:
                return False

    return True

def solve_sudoku(board):
    """Solves the Sudoku puzzle using backtracking."""
    empty_location = find_empty_location(board)
    if not empty_location:
        return True  # Puzzle solved

    row, col = empty_location

    for num in range(1, 10):  # Try numbers 1 to 9
        if is_safe(board, row, col, num):
            board[row][col] = num  # Place the number

            if solve_sudoku(board):  # Recursively try to solve
                return True

            board[row][col] = 0  # Reset if it didn't work (backtrack)

    return False  # Trigger backtracking

def main():
    # Example Sudoku puzzle (0 represents empty cells)
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Original Sudoku Board:")
    print_board(board)

    if solve_sudoku(board):
        print("\nSolved Sudoku Board:")
        print_board(board)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
