# A simple function, greet_user() #
def greet_user(name):
    print(f"Hello, {name} ")

greet_user("Randy")
print()

# greet_user() with default value as argument
def greet_user(name="Guest"):
    print(f"Hello, {name} ")

greet_user()
greet_user("Randy")
print()

# a function that calculates and  returns the area of a rectangle #

def area_of_a_rectangle(l, b):
    return round(l * b, 2)

length = float(input("Length: "))
breadth = float(input("Breadth: "))

area = area_of_a_rectangle(length, breadth)
print("Area: ", area)