# Challenge: Transpose a Matrix
# Objective:
# Write a function that transposes a given matrix (converts rows into columns and vice versa).

# A matrix is represented as a list of lists, where each inner list represents a row in the matrix.

# Example Input:
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# Example Output (Transpose):
# [
#     [1, 4, 7],
#     [2, 5, 8],
#     [3, 6, 9]
# ]

# Instructions:
# Write a function transpose_matrix(matrix) that takes a 2D list (matrix) as an argument.
# The function should return a new matrix where the rows become columns and the columns become rows.
# Approach:
# You can transpose a matrix by swapping the elements at position [i][j] with [j][i].
# In Python, you can use a list comprehension to simplify this process.


def transpose_matrix(matrix):
    # Use zip and * to transpose the matrix
    return [list(row) for row in zip(*matrix)]


# Example matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Transposing the matrix
transposed = transpose_matrix(matrix)

# Output the transposed matrix
for row in transposed:
    print(row)


# The * operator (called the "unpacking" operator) unpacks the rows of the matrix, effectively passing each row as a separate argument to the zip function.
# For example, given the matrix:

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# *matrix becomes:
# zip([1, 2, 3], [4, 5, 6], [7, 8, 9])

# The zip function takes multiple iterables (lists, tuples, etc.)
# and groups elements by their index. In this case, it groups elements from each row of the matrix based on their positions.
# So,
# zip([1, 2, 3], [4, 5, 6], [7, 8, 9])
# will result in:
# (1, 4, 7), (2, 5, 8), (3, 6, 9)
# This effectively transposes the matrix because the first element from each row is grouped into the first tuple,
# the second element into the second tuple, and so on.
