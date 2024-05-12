# Write a program that turns two sets into one dictionary.
def exercise1(lst_1:list, lst_2:list):
    numbers_dict ={}
    num_length = len(lst_1)
    if len(lst_1) !=  len(lst_2):
        return "Making dictionary with invalid key or value leads to corrupted data."
    for i in range(num_length):
        numbers_dict[lst_1[i]] = lst_2[i]

    return numbers_dict
print(exercise1(["one", "two", "three", "four"], [7, 8, 9, 10]))



# Write a program that checks if a key is already 
# in a dictionary. If it is not, add it
# to the dictionary with a value of “empty”.
def check_key(dict_1:dict, key:any) ->str:
    if key in dict_1:
        return f'{key} is in dictionary!'
    else:
        print(f'{key} is not in the dictionary')
        dict_1[key] = "empty"
        return f'The new dictionary is: {dict_1}'

my_dict = {"dad": "Eise", "sister_1": "Iris",
"sister_2": "Nicky"}
print(check_key(my_dict,key='dad'))

my_dict1 = {"fruit": "Apple", "vegetable":
"Capsicum"}
print(check_key(my_dict1,'meat'))

# Write a program that compares the fruits set with the red set
def compare_sets(red_objects:set, fruits:set) -> str:
    only_redFruits = red_objects.intersection(fruits)

    allFruits_noneRed = fruits.difference(red_objects)

    return f'Only red objects : {only_redFruits} and all fruits without red: {allFruits_noneRed}'

red_objects = {'apple', 'crab', 'rose', 'strawberry'}
fruits = {'orange', 'apple', 'strawberry', 'grape', 'kiwi', 'mandarin'}
print(compare_sets(red_objects, fruits))







