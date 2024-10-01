# Challenge: "Valid Anagram"
# Problem Statement:
# Given two strings s and t, return True if t is an anagram of s,
# and False otherwise. An anagram is a word
# or phrase formed by rearranging the letters of a different word
# or phrase, typically using all the original letters exactly once.

# Example:

# Input: s = "anagram", t = "nagaram"
# Output: True

# Input: s = "rat", t = "car"
# Output: False

# Constraints:
# The input strings consist of lowercase English letters.
# The lengths of s and t can be at most 5 × 10^4.

# Task:
# Write a function that takes two strings as input
# and returns True if the second string is an anagram of the first string,
# and False otherwise.

s = "anagram"
t = "nagaram"


def is_anagram(s, t):
    # Convert both strings to lists of characters
    s_list = list(s)
    t_list = list(t)
    # Sort both lists
    s_list.sort()
    t_list.sort()
    # Compare the sorted lists
    return s_list == t_list


if is_anagram(s, t):
    print(f"{s} is an anagram of {t}")
else:
    print(f"{s} is not an anagram of {t}")
