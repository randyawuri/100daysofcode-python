# import random module #
import random

rand_num = random.randint(1, 100) # generate a random number between 1 and 100 #
print("Here's your random number! ", rand_num)

# random number generator  using user input #
lower_int = int(input("Enter lower bound number: "))
upper_int = int(input("Enter upper bound number: "))

if lower_int >= upper_int:
    print("Invalid range! Lower bound must be greater than upper bound.")
else:
    rand_num = random.randint(lower_int, upper_int)
    print(rand_num)