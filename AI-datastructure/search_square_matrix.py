def countSubmatricesWithE(board):
    # Initialize a count variable to keep track of how many submatrices meet the criteria
    count = 0
    rows, cols = len(board), len(board[0])

    # Use a nested loop to go through each element that can be the top-left corner of a 3x3 submatrix
    for i in range(rows - 2):
        for j in range(cols - 2):
            # Check if the current 3x3 submatrix has 'E's in all four corners
            if (board[i][j] == 'E' and
                board[i][j + 2] == 'E' and
                board[i + 2][j] == 'E' and
                board[i + 2][j + 2] == 'E'):
                # If it does, increment the count
                count += 1

    # Return the count of submatrices that meet the criteria
    return count


# Define a matrix 'board' with some 'E's and 'P's, representing empty and piece positions respectively
board = [
    ['E', 'P', 'E', 'E'],
    ['P', 'E', 'P', 'E'],
    ['E', 'E', 'E', 'P'],
    ['P', 'P', 'E', 'E']
]

# Call the function to count the submatrices and print the result
result = countSubmatricesWithE(board)
print("Number of 3x3 submatrices with 'E' in all corners:", result)
