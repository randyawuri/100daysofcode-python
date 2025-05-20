# a program that checks if given year is a leap year #
# get user input #
year = int(input("Enter year: "))

"""
logic:
A year is a leap year if:
It's divisible by 4, and
Not divisible by 100, unless
It's also divisible by 400
"""
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year!")
else:
    print(f"{year} is not a leap year.")