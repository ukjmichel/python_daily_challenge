# Rotate Array Challenge:
# the task is to rotate the elements of an array (or list) by a given number of positions.
# You can rotate to the right (clockwise) or to the left (counterclockwise).

# Problem:
# Write a function that takes an array and a number k as inputs.
# The function should rotate the array to the right by k steps.
# If k is larger than the length of the array, it should wrap around.

# Example:
# Input: arr = [1, 2, 3, 4, 5], k = 2
# Output: [4, 5, 1, 2, 3] (rotated 2 positions to the right)

# Plan:
# First, normalize the number of rotations k by using the modulo operator,
# because rotating by more than the length of the array is equivalent to rotating by k % len(arr).
# Split the array into two parts:
# The right part that will move to the front.
# The left part that will shift to the back.
# Recombine the array.


def rotate_array(arr, k):
    # If the array is empty or k is 0, return the array as is
    if not arr or k == 0:
        return arr
    # Normalize k to avoid unnecessary full rotations
    k = k % len(arr)
    # Slice the array and recombine
    return arr[-k:] + arr[:-k]


print(rotate_array([1, 2, 3, 4, 5], 2))
