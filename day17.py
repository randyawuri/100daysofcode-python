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
    text = str(input("Enter text: "))
    vowels = ["a", "e", "i", "o", "u"]
    count = 0

    for i in text.lower():
        if i in vowels:
            count += 1
    return count

print("Number of vowels: ", vowel_count())