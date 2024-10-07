# Challenge: Product of All Elements Except Itself
# Given an integer list nums, return a new list where each element
# at index i is the product of all the numbers in the original list
# except nums[i]. You cannot use division to solve this problem.

# Example 1:
# python
# Copier le code
# Input: nums = [1, 2, 3, 4]
# Output: [24, 12, 8, 6]
# Example 2:
# python
# Copier le code
# Input: nums = [5, 3, 4, 2]
# Output: [24, 40, 30, 60]
# Example 3:
# python
# Copier le code
# Input: nums = [1, 0, 3, 0]
# Output: [0, 0, 0, 0]
# Constraints:
# The length of nums will be at least 1.
# Each element of nums can be positive, negative, or zero.
# Your Task:
# Write a function product_except_self(nums: List[int]) -> List[int]
# to solve this problem without using division.


def productWithException(numbers):
    # Initialize the output list with 1's
    length = len(numbers)
    result = [1] * length

    # Calculate the left product for each element using a for loop
    left = 1
    for i, num in enumerate(numbers):
        result[i] = left
        left *= num

    # Calculate the right product and multiply it with the left product using a reversed for loop
    right = 1
    for i, num in enumerate(reversed(numbers)):
        result[length - 1 - i] *= right
        right *= num

    return result


def productWithExceptionWithRange(numbers):
    # Initialize the output list with 1's
    length = len(numbers)
    result = [1] * length

    # Calculate the left product for each element
    for i in range(1, length):
        result[i] = result[i - 1] * numbers[i - 1]

    # Calculate the right product and multiply it with the left product
    right = 1
    for i in range(length - 1, -1, -1):
        result[i] = result[i] * right
        right *= numbers[i]

    return result


print(productWithException([1, 2, 3, 4]))
# print(productWithException([5, 3, 4, 2]))
# print(productWithException([11, 0, 3, 0]))

# print(productWithExceptionWithRange([1, 2, 3, 4]))
# print(productWithExceptionWithRange([5, 3, 4, 2]))
# print(productWithExceptionWithRange([11, 0, 3, 0]))
