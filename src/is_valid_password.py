# Password validation Challenge:

# Password Validation Rules:

# Minimum length of 8 characters.
# Must contain at least one uppercase letter.
# Must contain at least one lowercase letter.
# Must contain at least one digit.
# Must contain at least one special character (e.g., @, #, $, %, etc.).
# Task:
# Write a Python function validate_password(password)
# that checks whether a password meets all the above criteria.

import re


def is_valid_password(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(not char.isalnum() for char in password):
        return False
    return True


def is_valid_password_regex(password):
    # Combined regex for all conditions
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^\w]).{8,}$"

    # Use re.fullmatch to ensure the whole password matches the pattern
    return bool(re.fullmatch(pattern, password))

# Explanation of the Regex:
# ^: Asserts the start of the string.
# (?=.*[A-Z]): Asserts that there is at least one uppercase letter.
# (?=.*[a-z]): Asserts that there is at least one lowercase letter.
# (?=.*\d): Asserts that there is at least one digit.
# (?=.*[^\w]): Asserts that there is at least one special character (non-alphanumeric).
# .{8,}: Asserts that the total length of the string is at least 8 characters.
# $: Asserts the end of the string.


# Example of Usage
passwords = [
    "Password123!",
    "pass",
    "PASSWORD123",
    "Pass123",
    "Valid1!",
    "validpassword!",
]

for pwd in passwords:
    print(f"'{pwd}': {is_valid_password_regex(pwd)}")
