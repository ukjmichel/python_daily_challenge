# Challenge: Sum of Multiples
# Write a function that takes two integers, n and x,
# and returns the sum of all the multiples of x that are less than n.


def sumOfMultiple(n, x):
    i = 0
    result = 0
    while i < n:
        if i % x == 0:
            result += i
        i += 1

    return result


print(sumOfMultiple(10, 2))
print(sumOfMultiple(10, 3))
print(sumOfMultiple(100, 4))
