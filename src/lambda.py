from functools import reduce
import random

# 1. Square of a Number

# Write a lambda function to find the square of a given number.
print("\n>Square of a Number")
square = lambda x: x**2
number = 5
print(f"square {number} equal {square(number)}")

# 2. Even or Odd
# Write a lambda function that returns True if a number is even, and False otherwise.
print("\n>Even or Odd")
is_even_or_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
number = 2
print(f"{number} is {is_even_or_odd(number)}")

# 3. Find Maximum of Two Numbers
# Write a lambda function to find the maximum of two numbers.
print("\n>Find Maximum of Two Numbers")
max_number = lambda x, y: x if x > y else y
print(f"maximum number is {max_number(10, 20)}")

# 4. Sort a List of Tuples by Second Element
# Given a list of tuples, sort them by the second element using lambda.
print("\n>Sort a List of Tuples by Second Element")
tuples_example = [(1, 2), (3, 1), (5, 4), (2, 3)]
sort_tupple = lambda tuples: sorted(tuples, key=lambda x: x[1])
print(sort_tupple(tuples_example))

# 5. Filter Odd Numbers from a List
# Use lambda and filter() to get all the odd numbers from a list.
print("\n>Filter Odd Numbers from a List")
random_numbers = [random.randint(1, 100) for _ in range(10)]
odd_numbers = lambda numbers: list(filter(lambda x: x % 2 != 0, numbers))
even_numbers = lambda numbers: list(filter(lambda x: x % 2 == 0, numbers))
print(f"Odd numbers: {odd_numbers(random_numbers)}")
print(f"Even numbers: {even_numbers(random_numbers)}")

# 6. Map to Calculate Cube of List Elements
# Use lambda and map() to calculate the cube of each element in a list.
print("\n>Map to Calculate Cube of List Elements")
numbers = [1, 2, 3, 4, 5]
cube_numbers = list(map(lambda x: x**3, numbers))
print(cube_numbers)

# 7. Combine First and Last Name
# Write a lambda function that takes two strings, first_name and last_name,
# and returns a single string in the format "Last, First".
print("\n>Combine First and Last Name")
full_name = lambda first_name, last_name: f"{last_name} {first_name}"
print(full_name("John", "Doe"))

# 8. Filter Words Starting with a Specific Letter
# Use lambda and filter() to return words starting with the letter "A" from a list.
print(">Filter Words Starting with a Specific Letter")
words = ["apple", "banana", "cherry", "date", "elderberry"]
letter = "a"
filtered_words = lambda words, letter: list(
    filter(lambda word: word[0] == letter, words)
)
print(f"words starting with {letter}: {filtered_words(words,letter)}")

# 9. Multiply All Elements in a List
# Write a lambda function to multiply all elements in a list together.
print("\n>Multiply All Elements in a List")
numbers = [1, 2, 3, 4, 5]
multiply_numbers_of_list = lambda numbers: reduce(lambda x, y: x * y, numbers)
print(f"number: {numbers}")
print(f"result: {multiply_numbers_of_list(numbers)}")

# 10. Extract Ages Greater than 18
# Use lambda and filter() to extract ages greater than 18 from a list.
print("\nExtract Ages Greater than 18")
ages = [3,8,15, 20, 25, 30, 35, 40, 99]
filter_age = lambda ages: list(filter(lambda age: age > 18, ages))
print(filter_age(ages))
