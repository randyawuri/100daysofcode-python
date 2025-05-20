def factorial_of_a_number():
    num = int(input("Enter a number: "))
    factorial = 1

    for i in range(1, num + 1):
        factorial *= i
    print(f"{num}! is: {factorial}")

factorial_of_a_number()
