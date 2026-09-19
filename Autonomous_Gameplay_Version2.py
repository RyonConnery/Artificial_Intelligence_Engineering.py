# Step 1: Define the CSP problem - N-Queens
def is_safe(board, row, col, n):
    """
    Check if placing a queen at (row, col) is safe.
    """

    # Check this row on the left
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left
    for i, j in zip(
        range(row, -1, -1),
        range(col, -1, -1)
    ):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left
    for i, j in zip(
        range(row, n),
        range(col, -1, -1)
    ):
        if board[i][j] == 1:
            return False

    return True


# Step 2: Implement backtracking search
def solve_n_queens(board, col, n):
    """
    Solve N-Queens problem using backtracking.
    """

    if col >= n:  # All queens are placed
        return True

    for row in range(n):
        if is_safe(board, row, col, n):

            # Place the queen
            board[row][col] = 1

            # Recur for the next column
            if solve_n_queens(board, col + 1, n):
                return True

            # Backtrack
            board[row][col] = 0

    return False


# Step 3: Add forward checking for constraint propagation
def forward_checking(board, current_col, n):
    """
    Apply forward checking to ensure future columns
    still have possible queen positions.
    """

    for col in range(current_col + 1, n):
        possible_positions = [
            row
            for row in range(n)
            if is_safe(board, row, col, n)
        ]

        if not possible_positions:
            return False

    return True


# Step 4: Integrate forward checking with backtracking
def solve_n_queens_with_forward_checking(board, col, n):
    if col >= n:  # All queens are placed
        return True

    for row in range(n):
        if is_safe(board, row, col, n):

            board[row][col] = 1  # Place the queen

            if forward_checking(board, col, n):
                if solve_n_queens_with_forward_checking(
                    board,
                    col + 1,
                    n
                ):
                    return True

            board[row][col] = 0  # Backtrack

    return False


# Step 5: Execute and visualize the solution
def print_solution(board):
    for row in board:
        print(
            " ".join(
                "Q" if x == 1 else "."
                for x in row
            )
        )


# Input: N
n = 8  # Example: 8-Queens problem

board = [
    [0 for _ in range(n)]
    for _ in range(n)
]


# Solve using backtracking with forward checking
if solve_n_queens_with_forward_checking(
    board,
    0,
    n
):
    print("Solution found:")
    print_solution(board)

else:
    print("No solution exists.")
