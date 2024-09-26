# Python Daily Challenge: Factorial Calculation
# Problem:

# Write a Python function that calculates the factorial of a given non-negative integer.
# The factorial of a number n is the product of all positive integers less than or equal to n.


def factorial(n):
    # Check if the input is a non-negative integer
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


number = 5
factorial_result = factorial(number)
print(factorial_result)
