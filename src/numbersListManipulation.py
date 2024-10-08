# Challenge: Manipulating a List of Numbers
# Problem Statement:
# You are given a list of integers. Your task is to write a Python function that performs the following operations:

# Remove all even numbers from the list.
# Square the remaining odd numbers.
# Sort the list in descending order.
# Return the modified list.
# Example:
# python
# Copier le code
# Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Output: [81, 49, 25, 9, 1]
# Instructions:
# Define a function named process_numbers(numbers) that takes a list of integers as input.
# Remove all even numbers from the list using list comprehension.
# Square the remaining odd numbers.
# Sort the resulting list in descending order.
# Return the modified list.
# Your Task:
# Write the function process_numbers(numbers) that implements the above operations.
# Test the function with various inputs to ensure correctness.


def numbersListManipulation(numbers):
    # Remove all even numbers from the list using list comprehension
    odd_numbers = [num for num in numbers if num % 2 != 0]
    # Square the remaining odd numbers
    squared_odd_numbers = [num**2 for num in odd_numbers]
    # Sort the resulting list in descending order
    sorted_numbers = sorted(squared_odd_numbers, reverse=True)
    # Return the modified list
    return sorted_numbers


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbersListManipulation(numbers=numbers))
