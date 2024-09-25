# Challenge: Palindrome Checker

# Write a function is_palindrome(s) that takes a string s as input
# and returns True if the string is a palindrome, and False otherwise.
# A palindrome is a string that reads the same forward
# and backward, ignoring spaces, punctuation, and case differences.


# Define a function to check if a word is a palindrome
def isPalindrome(word):
    # Check if the word is the same when reversed
    if word == word[::-1]:  # word[::-1] reverses the string
        return f"{word} is a palindrome "  # If true, return this message
    else:
        return f"{word} is not a palindrome "  # If false, return this message


# Test the function with the word "hello"
print(isPalindrome("hello"))  # Expected output: "hello is not a palindrome"

# Test the function with the word "racecar"
print(isPalindrome("racecar"))  # Expected output: "racecar is a palindrome"
