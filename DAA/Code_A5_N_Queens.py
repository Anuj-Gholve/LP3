# Experiment A5: N-Queens using backtracking
# Time complexity: O(n!) upper-bound estimate for the search.
# Space complexity: O(n^2) for the board, plus O(n) recursion stack.

def solve_n_queens(n):
    if n <= 0:
        raise ValueError("Number of queens must be a positive integer.")

    board = [[0] * n for _ in range(n)]
    solutions = []
    used_columns = set()
    used_diagonals_down = set()  # row - column
    used_diagonals_up = set()    # row + column

    def backtrack(row):
        if row == n:
            solutions.append([line[:] for line in board])
            return

        for col in range(n):
            if (col in used_columns or
                (row - col) in used_diagonals_down or
                (row + col) in used_diagonals_up):
                continue

            board[row][col] = 1
            used_columns.add(col)
            used_diagonals_down.add(row - col)
            used_diagonals_up.add(row + col)

            backtrack(row + 1)

            board[row][col] = 0
            used_columns.remove(col)
            used_diagonals_down.remove(row - col)
            used_diagonals_up.remove(row + col)

    backtrack(0)
    return solutions


def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()


def main():
    try:
        n = int(input("Enter number of queens: "))
        solutions = solve_n_queens(n)
    except ValueError as error:
        print("Invalid input:", error)
        return

    if not solutions:
        print(f"No solution exists for {n}-Queens.")
        return

    print(f"\nNumber of solutions for {n}-Queens: {len(solutions)}\n")
    for index, board in enumerate(solutions, start=1):
        print(f"Solution {index}:")
        print_board(board)


if __name__ == "__main__":
    main()
