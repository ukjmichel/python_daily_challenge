# Challenge: Reverse Words in a String
# Write a function that takes a string of words and returns the string with the words in reverse order.
# The words are separated by spaces, and there are no leading or trailing spaces.

# Example:
# Input: "Hello world this is Python"
# Output: "Python is this world Hello"

# Instructions:
# Create a function reverse_words(s: str) -> str.
# The input will be a string with words separated by a single space.
# Return a new string where the words appear in reverse order.
# Hints:
# You can use Python string methods like split() and join() to help with this challenge.
# Bonus:
# Handle cases where there are multiple spaces between words. Ensure that the returned string has only single spaces between words.

# Example for Bonus:
# Input: "  Hello   world  this  is  Python  "
# Output: "Python is this world Hello"
import re


def reverse_string(s):
    words = s.split()
    # Reverse the list of words
    reversed_words = words[::-1]
    # Join the reversed list of words into a string with single spaces in between
    reversed_string = " ".join(reversed_words)
    return reversed_string

print(reverse_string("  Hello   world  this  is  Python  "))
