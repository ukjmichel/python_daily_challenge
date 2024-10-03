# Problem: Unique Character Finder
# Write a function called find_unique_characters that takes a string as input
# and returns a list of characters that appear only once in the string.
# The characters should be returned in the order they appear in the input string.

# Example:

# find_unique_characters("programming")
# # Output: ['p', 'o', 'g', 'a', 'm', 'i', 'n']

# find_unique_characters("hello world")
# # Output: ['h', 'e', 'w', 'r', 'd']

# Constraints:
# Ignore spaces.
# The function should be case-sensitive (i.e., 'A' and 'a' are considered different characters).


def find_unique_characters(s):
    # Create a dictionary to count occurrences of each character
    char_count = {}

    # Count each character in the string
    for char in s:
        if char != " ":  # Ignore spaces
            char_count[char] = char_count.get(char, 0) + 1

    # Collect characters that appear only once
    unique_chars = [char for char in s if char_count.get(char, 0) == 1 and char != " "]

    return print(unique_chars)


find_unique_characters("programming")
find_unique_characters("hello")
