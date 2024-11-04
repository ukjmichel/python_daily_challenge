# Check if Prime Challenge
# Challenge: Write a function that checks if a given number is a prime number.
# A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers.
# In other words, it has no positive divisors other than 1 and itself.

# Requirements
# The function should take an integer as input.
# It should return True if the number is prime and False otherwise.
# Handle edge cases (e.g., numbers less than 2).


def is_prime(n):
    # Edge case: Numbers less than 2 are not prime
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Test cases
print(is_prime(2))  # Output: True
print(is_prime(10))  # Output: False
print(is_prime(13))  # Output: True
print(is_prime(1))  # Output: False
print(is_prime(17))  # Output: True
print(is_prime(25))  # Output: False
