"""
# define a set with multiple values including duplicates #
myset = {"Shola", "Tony", "Shola", "Tobe", "David", "Nonso", "Nonso"}
print(myset)

myset.add("Hassan") # add item set #
print(myset)

myset.remove("Hassan") # delete item from set #
print(myset)

# set operators #
set_a = {20, 45, 15, 90, 30, 35}
set_b = {25, 18, 90, 85, 70, 20, 45, 62, 50}

print("Union: ", set_a | set_b) # union of two sets #
print("Intersection: ", set_a & set_b) # intersection of two sets #
print("Difference (A - B): ", set_a - set_b) 
print("Difference (B - A): ", set_b - set_a) 
print("Symmetric difference: ", set_a ^ set_b)
print("Is A a subset of B? ", set_a <= set_b)
print("Is B a subset of A? ", set_b <= set_a)
print("Are A and B disjoint? ", set_a.isdisjoint(set_b))

# get set values from user input #
chem = input("Enter students names for Chemistry  separated by comma: ") 
bio = input("Enter students names for Biology separated by comma: ")

# convert to sets #
chem_set = set(chem.split(","))
bio_set = set(bio.split(","))
# remove extra spaces #
chem_set = {item.strip() for item in chem_set}
bio_set = {item.strip() for item in bio_set}
students = chem_set | bio_set

print("Chemistry: ", chem_set)
print("Biology: ", bio_set)
print("All students: ", students)

# students who take both courses #
print("Students who take both courses: ", chem_set & bio_set)
# print only chemistry students #
print("Chemistry students:  ", chem_set - bio_set)
# Biology students only #
print("Biology students: ", bio_set - chem_set)
print("Students who are in either of the courses but not both: ", chem_set ^ bio_set)

# iterate over elements of the set #
for student in students:
    if student.startswith("S"):
        print(f"{student}")
"""
car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2010
}
print(type(car))

# define a dictionary that consists of data from a small e-commerce product catalogue #
prod_log = {
    "P001": {"name": "Wireless Mouse", "price": 25.99, "stock": 34},
    "P002": {"name": "Keyboard", "price": 45.00, "stock": 20},
    "P003": {"name": "USB-C Cable", "price": 9.99, "stock": 100},
    "P004": {"name": "Monitor", "price": 159.49, "stock": 10},
}
print(prod_log)