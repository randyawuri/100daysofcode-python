# the parse_item() funtion does the type conversion, as well as error and  exception handling
def parse_item(item):
    item = item.strip() # removes trailing whitespaces from the string 
    if item.isdigit(): # checks if the cleaned string contains only digits
        return int(item) # returns an integer if true
    try:
        return float(item) # converts and returns a float if not an integer
    except ValueError:
        if item.lower() == "true": # converts "true" to Boolean True
            return True
        elif item.lower() == "false": # converts "false" to Boolean False
            return False
        else:
            return item  # treat as string if all else fails
        
def list_sum():
    user_input = input("Enter data separated by comma: ") # prompts user for input
    user_list = [parse_item(x) for x in user_input.split(',')] # convert user's input to  a list using commas, and convert each element to appropriate type by applying the parse_item() funtion

    for item in user_list: # loop through the list and print each item and its data type
        print(f"{item} {type(item).__name__}")
    print("Total number of elements in the list: ", len(user_list)) # print total number of elements in the list

list_sum() # function call