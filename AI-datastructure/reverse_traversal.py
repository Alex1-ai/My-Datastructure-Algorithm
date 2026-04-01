def reverse_traversal(matrix):
    rows, cols = len(matrix), len(matrix[0])
    output = []

    for row in range(rows - 1, -1, -1):
        for col in range(cols - 1, -1, -1):
            output.append(matrix[row][col])

    return output


print(reverse_traversal([
    [1, 2, 3, 'a'],
    [4, 5, 6, 'b'],
    [7, 8, 9, 'c']
]))
