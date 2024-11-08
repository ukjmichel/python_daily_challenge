# Power Calculation Challenge:
# Write a Python function to calculate the power of a number x raised to the power y (i.e., x^y) using a loop.

# python
# Copier le code


# def power(x, y):
#     return x**y if y >= 0 else 1 / (x ** abs(y))


# def power(x, y):
#     return (
#         1
#         if y == 0
#         else x * power(x, y - 1) if y > 0 else 1 / (x * power(x, abs(y) - 1))
#     )


# def power(x, y):
#     result = 1
#     for _ in range(abs(y)):
#         result *= x
#     return result if y >= 0 else 1 / result


power = lambda x, y: (
    1 if y == 0 else x * power(x, y - 1) if y > 0 else 1 / (x * power(x, abs(y) - 1))
)

print(power(5, 3))
