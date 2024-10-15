# Challenge: Merge Two Sorted Lists
# Task: Write a function that takes two sorted lists of integers
# and merges them into a single sorted list.
# The merged list should maintain the order of the elements.

# Input:

# Two lists of integers, list1 and list2, both of which are sorted in ascending order.
# Output:

# A new list that contains all elements from list1 and list2, sorted in ascending order.
# Example
# Input:

# list1 = [1, 3, 5, 7]
# list2 = [2, 4, 6, 8]
# Output:
# [1, 2, 3, 4, 5, 6, 7, 8]

# Input:
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# Copier le code
# [1, 2, 3, 4, 5, 6]


# Constraints
# The input lists may have different lengths, including empty lists.
# The function should have a time complexity of O(n + m), where n and m are the lengths of the two lists.


def merge_sorted_lists(list1, list2):
    # Initialize an empty list to store the merged result
    merged_list = []
    i, j = 0, 0

    # Traverse both lists and merge them
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    # Append any remaining elements from list1

    # If there are remaining elements in list1, add them
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    # If there are remaining elements in list2, add them
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list


print(merge_sorted_lists([1, 2, 3], [4, 5, 6]))


# one approch to sorted a merged list coulb be to concatenate then sorte the list:

# def merge_sorted_lists(list1, list2):
#     # Initialize an empty list to store the merged result
#     merged_list = list1 + list2  # Step 1
#     return sorted(merged_list)  # Step 2

# but the Overall Time Complexity would be:
# Concatenation: O(n + m)
# Sorting: O((n + m) log(n + m))
# Thus, the overall time complexity of the function merge_sorted_lists is O((𝑛+𝑚)log(𝑛+𝑚))O((n+m)log(n+m))

# When merging two sorted lists, the best approach is
# one that takes advantage of the fact that both input lists are already sorted.
# This allows us to merge the lists in a single pass with a time complexity of O(n + m),
# where n is the length of the first list and m is the length of the second list.
