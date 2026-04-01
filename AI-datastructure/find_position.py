def find_positions(board):
    positions = []
    rows, cols = len(board), len(board[0])

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'E':
                if ((i > 0 and board[i-1][j] == 'E') or
                    (i < rows - 1 and board[i+1][j] == 'E') or
                    (j > 0 and board[i][j-1] == 'E') or
                    (j < cols - 1 and board[i][j+1] == 'E')):
                    positions.append((i, j))
        return positions


board = [
    ['P', 'E', 'E', 'P'],
    ['E', 'P', 'E', 'P'],
    ['P', 'E', 'P', 'P'],
    ['P', 'E', 'P', 'E']
]

print(find_positions(board))



# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Function to check if a neighboring position is empty ('E')
def is_empty_neighbor(board, x, y):
    rows, cols = len(board), len(board[0])

    # Check that (x, y) is within board boundaries
    if 0 <= x < rows and 0 <= y < cols:
        return board[x][y] == 'E'
    return False

def main():
    board = [
        ['P', 'E', 'E', 'P'],
        ['E', 'P', 'E', 'P'],
        ['P', 'E', 'P', 'P'],
        ['P', 'E', 'P', 'E']
    ]
    result = []
    rows, cols = len(board), len(board[0])

    for i in range(rows):
        for j in range(cols):
            # Check for empty spot with an empty neighbor on four directions
            if board[i][j] == 'E' and (
                is_empty_neighbor(board, i - 1, j) or
                is_empty_neighbor(board, i + 1, j) or
                is_empty_neighbor(board, i, j - 1) or
                is_empty_neighbor(board, i, j + 1)
            ):
                result.append((i, j))
    print(result)

if __name__ == "__main__":
    main()
