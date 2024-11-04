# Problem Statement
# Write a function find_divisors that takes an integer n as input
# and returns a list of all divisors of n. A divisor of n
# is a number that divides n without leaving a remainder.

# Steps to Solve
# Loop through numbers from 1 to n.
# For each number, check if it divides n evenly.
# If it does, add it to a list of divisors.
# Return the list of divisors.


def find_divisors(n):
    # Initialize an empty list to store divisors
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    return divisors


# Test cases
print(find_divisors(10))  # Output: [1, 2, 5, 10]
print(find_divisors(15))  # Output: [1, 3, 5, 15]
print(find_divisors(21))  # Output: [1, 3, 7, 21]
