# Challenge: Flatten a Nested List
# Objective: Write a function that takes a nested list
# (a list that may contain other lists as elements)
# and flattens it into a single list containing all the elements.

# Requirements:
# The function should handle nested lists of arbitrary depth.
# The output should be a flat list containing all the elements from the nested lists.
# Example Input and Output:
# Input:

# python
# Copier le code
# nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
# Output:

# python
# Copier le code
# flattened_list = [1, 2, 3, 4, 5, 6, 7, 8]
# Steps to Solve:
# Define a function that takes a nested list as an argument.
# Initialize an empty list to store the flattened elements.
# Iterate through each element in the nested list:
# If the element is a list, recursively flatten it.
# If it's not a list, append it directly to the flattened list.
# Return the flattened list.

# Sample Implementation:
# Here’s a sample implementation of the function:

# def flatten(nested_list):
#     flat_list = []

#     for element in nested_list:
#         if isinstance(element, list):
#             # If the element is a list, recursively flatten it
#             flat_list.extend(flatten(element))
#         else:
#             # If not a list, append the element to the flat list
#             flat_list.append(element)

#     return flat_list

# # Test the function

# nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
# flattened_list = flatten(nested_list)
# print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# Additional Test Cases:

# Empty List
# print(flatten([]))  # Output: []

# Single-Level Nesting
# print(flatten([1, 2, 3, 4]))  # Output: [1, 2, 3, 4]

# Multiple Levels of Nesting
# print(flatten([1, [2, [3, [4, 5]], 6], 7]))  # Output: [1, 2, 3, 4, 5, 6, 7]

# Different Data Types
# print(flatten([1, "text", [2.5, [True, None]], 3]))  # Output: [1, "text", 2.5, True, None,


def flatten(nested_list):
    flat_list = []
    # Loop over each element in the nested list
    for element in nested_list:
        # If the element is a list, recursively call the flatten function
        if isinstance(element, list):
            flat_list.extend(flatten(element))
        else:
            flat_list.append(element)

    return flat_list


# Test the function with various examples
nested_list_1 = [1, [2, [3, 4], 5], 6, [7, 8]]
flattened_list_1 = flatten(nested_list_1)
print(flattened_list_1)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

nested_list_2 = []
flattened_list_2 = flatten(nested_list_2)
print(flattened_list_2)  # Output: []

nested_list_3 = [1, 2, 3, 4]
flattened_list_3 = flatten(nested_list_3)
print(flattened_list_3)  # Output: [1, 2, 3, 4]

nested_list_4 = [1, [2, [3, [4, 5]], 6], 7]
flattened_list_4 = flatten(nested_list_4)
print(flattened_list_4)  # Output: [1, 2, 3, 4, 5, 6, 7]

nested_list_5 = [1, "text", [2.5, [True, None]], 3]
flattened_list_5 = flatten(nested_list_5)
print(flattened_list_5)  # Output: [1, "text", 2.5, True, None, 3]
