def transformMatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    result = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
    return result


def transposeMatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    transpose = [[0 for _ in range(rows)] for _ in range(cols)]
    print(transpose)

    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = matrix[i][j]
    return transpose

matrix = [    [1, 2, 3],
    [4, 5, 6]]
transformed_matrix = transformMatrix(matrix)
transpose_matrix = transposeMatrix(matrix)
print(transpose_matrix)
print(transformed_matrix)  # Output: [[1, 4], [2, 5], [3, 6]]



# Given a constant matrix that represents tables in a restaurant
seating_chart = [
    [101, 102, 103, 104],
    [201, 202, 203, 204],
    [301, 302, 303, 304]
]

# Function to transpose the seating chart (Matrix) for new arrangement
def transpose(chart):
    return [[chart[j][i] for j in range(len(chart))] for i in reversed(range(len(chart[0])))]

# Example usage:
transposed_seating = transpose(seating_chart)
print(transposed_seating)  # Output will be the transposed matrix
# The expected output - [[104, 204, 304], [103, 203, 303], [102, 202, 302], [101, 201, 301



#---------------------------------------------------------------------------------------------------








def reflectOverSecondaryDiagonal(matrix):
    size = len(matrix)
    new_matrix = [[0 for _ in range(size)] for _ in range(size)]
    for i in reversed(range(size)):
        # TODO: Complete the code to obtain the reflected square matrix in new_matrix.
        for j in range(size):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix

# Example square matrix to reflect over the secondary diagonal
square_matrix = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]

# Call the function and print the transformed matrix
transformed_matrix = reflectOverSecondaryDiagonal(square_matrix)
# TODO: Call the function on square_matrix and store the result in transformed_matrix.
print(transformed_matrix)
# Output should be:
# [
#  [9, 6, 3],
#  [8, 5, 2],
#  [7, 4, 1]
# ]
