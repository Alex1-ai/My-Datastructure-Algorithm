def column_traversal(matrix):
    rows, cols = len(matrix), len(matrix[0])
    direction = "up"
    row, col = rows - 1, cols - 1
    output = []

    while len(output) < rows * cols:
        output.append(matrix[row][col])

        if direction == "up":
            if row - 1 < 0:
                direction = "down"
                col -= 1
            else:
                row -= 1
        else:
            if row + 1 == rows:
                direction = "up"
                col -= 1
            else:
                row += 1

    return output


print(column_traversal([
    [1, 2, 3, 'a'],
    [4, 5, 6, 'b'],
    [7, 8, 9, 'c']]))
