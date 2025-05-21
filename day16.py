# A function that checks if a given string is a palindrome #
"""
Logic:
1.  Get string input.
2.  Reverse string.
3.  Compare original and reversed versions (case-sensitive).
4.  Return True if they match, else return False.
"""

def is_palindrome():
    mystring = str(input("Enter a word: "))
    cleaned = ''.join(char.lower() for char in mystring if char.isalnum()) # clean the input to ensure for accuracy #
    """
    ''.join() joins all the cleaned characters back into a single string.
    char.lower() converts all characters to lowercase
    if char.isalnum() ignore spaces and punctuation, include only letters and numbers
    """
    return cleaned == cleaned[::-1] # compares the cleaned string with the reversed string and return True or False

print(is_palindrome())