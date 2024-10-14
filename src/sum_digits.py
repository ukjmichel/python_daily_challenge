# Task: Sum of Digits in a Number
# Write a Python function called sum_of_digits
# that takes an integer as input and returns the sum of its digits.
# The function should be able to handle both positive and negative numbers.
# Ignore the sign of the number.

# Example:
# python
# Copier le code
# sum_of_digits(1234)
# # Output: 10

# sum_of_digits(-567)
# # Output: 18
# Instructions:
# Convert the number to its absolute value (ignore the negative sign).
# Convert the number into a string or split its digits in some way.
# Sum all the individual digits.
# Return the sum as an integer.
# Hint:
# You can use the abs() function to get the absolute value of a number.


def sum_of_digits(n):
    # Convert the number to its absolute value
    n = abs(n)

    # Convert the number to a string and sum its digits
    return sum(int(digit) for digit in str(n))


# Test the function
print(sum_of_digits(1234))  # Output: 10
print(sum_of_digits(-567))  # Output: 18
print(sum_of_digits(0))  # Output: 0
