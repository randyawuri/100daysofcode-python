# even  or odd using if-esle statement#

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is an even number!")
else:
    print(f"{num} is an odd number!")

# check for largest number nested if-esle statement #
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2:
    if num1 >= num3:
        print (f"{num1} is the greatest!")
    else:
        print (f"{num3} is the greatest!")
else:
    if num2 > num3:
        print (f"{num2} is the greatest!")
    else:
        print (f"{num3} is the greatest!")


# calculate the sum of all numbers up to the given input number #
num = int(input("Give me a number!: "))
total = 0

for n in range(1, num + 1):
    total += n

print (f"the sum of all the numbers from  1 to {num} is {total} ")

# calculate the factorial of a given number using while loop #
num = int(input("Give me a number: "))
a = 1
b = 1

while b <= num:
    a *= b
    b += 1

print(f"the factorial of {num} is {a}")