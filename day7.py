# create a list of 5 elements #
mylist = ["Apple", 30, 5.5, "Grapes", True, ]
print(mylist) # display list #
print(mylist[0:3]) # print the first 3 items on the list #
print(mylist[-3:]) # print the last three items

# iterate through the list using the for loop #
for item in mylist:
    print(item)

# iterate through the list and print the index position of each item on the list #
for index, item in enumerate(mylist):
    print(f"Index {index}: {item}")

# iterate through the list using a while loop #
i = 0
while i < len(mylist):
    print(mylist[i])
    i += 1

# filter through the list to print specific types #
for item in mylist:
    if isinstance(item, str):
        print(f"String item: {item}")
    elif isinstance(item, bool):
        print(f"Boolean item: {item}")
    elif isinstance(item, int):
        print(f"Integer item: {item}")
    elif isinstance(item, float):
        print(f"Float item: {item}")

# change items on the list #
mylist[2] = "bannanas"
print(mylist)

#add item to the list #
mylist.append(4.5)
print(mylist)

### list comprehension ###
# take only string items from mylist and print them in a new list #
string_list = [item for item in mylist if isinstance(item, str)]
print(string_list)
string_list.sort() # sort string_list alhpabetically #
numbers = sorted([x for x in mylist if isinstance(x, (int, float))]) # sort a numbers only list #
print(numbers)
sorted_list = numbers + string_list # combine both sorted lists #
print(sorted_list)