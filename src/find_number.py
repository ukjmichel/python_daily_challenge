# Define a list of numbers that may contain duplicates
my_numbers_list = [2, 3, 4, 5, 6, 8, 7, 9, 2, 12, 23, 56, 78, 98, 45, 23]


def find_number(numbers_list):
    # Create a list of unique numbers by converting the input list to a set and back to a list
    unique_numbers_list = list(set(numbers_list))

    # Calculate the number of unique numbers
    unique_number_count = len(unique_numbers_list)

    # Print the count of unique numbers
    print(f"There are {unique_number_count} unique numbers.")

    # Ask the user for a valid position
    position = int(input("Which position in the list do you want? "))

    # Keep asking for a valid position while the input is invalid
    while position >= unique_number_count or position < 0:
        print(
            f"Invalid position! Please choose a number between 0 and {unique_number_count - 1}."
        )
        # Prompt the user again for a valid position
        position = int(input("Which position in the list do you want? "))

    # Print the element at the valid position in the unique numbers list
    print(f"The element at position {position} is {unique_numbers_list[position]}")


# Call the numberFinder function with the predefined list of numbers
find_number(my_numbers_list)
