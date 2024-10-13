# Challenge: Caesar Cipher Encryption and Decryption
# Problem Statement:

# The Caesar cipher is an encryption technique where each letter in the input text is shifted
# by a fixed number of positions in the alphabet. When the end of the alphabet is reached,
# it wraps around to the beginning. For example, with a shift of 3, 'A' becomes 'D', 'B' becomes 'E',
# and so on. Non-letter characters remain unchanged.

# Write two functions:

# encrypt_caesar_cipher(text, shift):
# Encrypts the given text by shifting each letter by the provided shift value.
# decrypt_caesar_cipher(text, shift):
# Decrypts the given text by shifting each letter back by the provided shift value.

# Requirements:
# The functions should work for both uppercase and lowercase letters.
# Non-alphabetical characters (like spaces, punctuation, numbers) should remain unchanged.
# The functions should handle both positive and negative shift values.

# Example:

# # Encryption
# Input: "Hello, World!", shift = 3
# Output: "Khoor, Zruog!"

# # Decryption
# Input: "Khoor, Zruog!", shift = -3
# Output: "Hello, World!"

# Function Signature:

# def encrypt_caesar_cipher(text: str, shift: int) -> str:
#     # Your code here

# def decrypt_caesar_cipher(text: str, shift: int) -> str:
#     # Your code here

# Constraints:
# The shift value can be any integer (positive or negative).
# The input string can contain any characters (letters, digits, symbols, etc.).

# Challenge:
# Implement both encryption and decryption using the Caesar cipher.
# Test the functions with different shift values and ensure they work for a variety of input strings.


def encrypt_caesar_cipher(text: str, shift: int = 1) -> str:
    result = ""
    for char in text:
        shift_base = 65 if char.isupper() else 97
        # 65-> 91 uppercaes, 97 -> 113 lowercase
        if char.isalpha():
            shift_base = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result += shift_base
        else:
            result += char
    return result


def decrypt_caesar_cipher(text: str, shift: int = 1) -> str:
    result = ""
    for char in text:
        shift_base = 65 if char.isupper() else 97
        if char.isalpha():
            shift_base = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            result += shift_base
        else:
            result += char
    return result


print(encrypt_caesar_cipher("hello, World!", 3))
print(decrypt_caesar_cipher("khoor, Zruog!", 3))
