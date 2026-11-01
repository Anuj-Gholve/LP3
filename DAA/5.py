def safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

        if col - (row - i) >= 0 and board[i][col - (row - i)] == 1:
            return False

        if col + (row - i) < n and board[i][col + (row - i)] == 1:
            return False

    return True

def solve(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if safe(board, row, col, n):
            board[row][col] = 1

            if solve(board, row + 1, n):
                return True

            board[row][col] = 0

    return False

n = int(input("Enter N: "))
board = [[0] * n for _ in range(n)]

board[0][0] = 1

if solve(board, 1, n):
    for row in board:
        print(row)
else:
    print("No solution exists")