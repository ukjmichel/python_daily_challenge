# Challenge: Validate an Email Address
# Objective
# Write a function that validates whether a given email address
# is in a valid format according to specific criteria.

# Criteria for a Valid Email Address
#     The email address must contain exactly one @ symbol.

#     The local part (the part before the @) can contain letters (both uppercase and lowercase),
#     numbers, and special characters such as . and -.

#     The domain part (the part after the @) must contain letters, numbers, hyphens, and dots.

#     The domain must have at least one dot,
#     and the last segment after the last dot must be at least two characters long (e.g., .com, .org, etc.).

#     The local part should not start or end with a dot,
#     and there should not be two consecutive dots in the local part.

# Function Signature

# def is_valid_email(email: str) -> bool:

# Input
# A string email that represents the email address to validate.

# Output
# Return True if the email address is valid according to the above criteria; otherwise, return False.


import re


def is_valid_email(email):
    regex = r"^[a-zA-Z0-9][a-zA-Z0-9.-]*[a-zA-Z0-9]@[a-zA-Z0-9]([a-zA-Z0-9.-]*[a-zA-Z0-9])?\.[a-zA-Z]{2,}$"

    return re.match(regex, email) is not None


# Test cases
print(is_valid_email("example@test.com"))  # True
print(is_valid_email("user.@domain.com"))  # False
print(is_valid_email("user.test@domain.com"))  # True
print(is_valid_email("user-test@domain.com"))  # True
print(is_valid_email("email.test@email.com"))  # True
print(is_valid_email("email.@email.com"))  # False
print(is_valid_email(".email@email.com"))  # False
print(is_valid_email("invalid-email@.com"))  # False
print(is_valid_email("user@domain@com"))  # False
print(is_valid_email("user@domain.com."))  # False
print(is_valid_email("user@domain..com"))  # False
print(is_valid_email("user@-domain.com"))  # False
print(is_valid_email("user@domain.com.com"))  # False
print(is_valid_email("user@domain.com"))  # True
print(is_valid_email("user@test@domain.com"))  # False
print(is_valid_email("user_test@domain.com"))  # False
