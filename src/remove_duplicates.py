# Challenge: Remove Duplicates from a List
# Write a Python function that removes all duplicates from a given list while preserving the original order of elements.

# Task:

# Your function should take a list as input and return a new list with the duplicates removed.
# The original order of the elements should be maintained.

# Example:
# remove_duplicates([1, 2, 2, 3, 4, 4, 5])
# Output: [1, 2, 3, 4, 5]

# Example:
# remove_duplicates(['a', 'b', 'a', 'c', 'b'])
# Output: ['a', 'b', 'c']


# Starter Code:
def remove_duplicates(lst):
    unique_elements = []

    for item in lst:
        if item not in unique_elements:
            unique_elements.append(item)

    return unique_elements

# Test
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Should return [1, 2, 3, 4, 5]
print(remove_duplicates(["a", "b", "a", "c", "b"]))  # Should return ['a', 'b', 'c']
