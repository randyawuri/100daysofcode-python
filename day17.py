# a function that counts the number of vowels in a string #
"""
1.  Get string input from user
2.  Define a list or set of vowels.
3.  Loop through each character in the string.
4.  Check if character (in lowercase) is a vowel.
5.  If yes, increase a counter.
6.  Return or print the count.
"""

def vowel_count():
    text = str(input("Enter word/sentence/paragraph: ")) # get text input from user #
    vowels = ["a", "e", "i", "o", "u"] # creates a list of vowels #
    text_lower = text.lower() # converts all characters from user's text to lowercase

    vowels_found = {char for char in text_lower if char in vowels} # creates a dictionary of unique vowels found in text #
    total_unique_vowels = len(vowels_found) # counts and records total number of unique vowels

    print("Total unique vowels found: ", total_unique_vowels) # prints total unique vowels found #
    print("Vowels found: ") # loops through text and prints vowels found
    for vowel in vowels_found:
        print(f" {vowel}")

vowel_count() # calls  the function