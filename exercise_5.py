import math
#Write a program that removes the first, third and fourth number from a list if they
#are there.

def remove_elements(nums:list)->list:
    n=0
    if len(nums) <= 2:
        nums.remove(nums[n])
        return nums
    if len(nums) <= 3:
        nums.remove(nums[n])
        nums.remove(nums[n+1])
        return nums
    if len(nums) >= 4:
        nums.remove(nums[n])
        nums.remove(nums[n+1])
        nums.remove(nums[n+1])
        return nums

print(f'The new list is: {remove_elements([1,2,3,4,5,6])}')
print(f'The new list is: {remove_elements([1,2,3])}')

#Write a program that combines two tuples into one tuple.
def combine_tuples(tuple_1:tuple, tuple_2:tuple)->tuple:
    return tuple_1 + tuple_2

tuple_1 = (1,2,3)
tuple_2 = (4,5,6)
print(combine_tuples(tuple_1,tuple_2))

#Write a program that takes a list and split it into two tuples of the same size.
def split_list(lst:list)->None:
    part_1 = len(lst)
    tuple_0 = tuple(lst)
    if len(lst) % 2 !=0:
        part_2 = math.ceil(len(lst)/2)
        print(f'Tuple 1 is: {tuple_0[0:part_2]}',f'Tuple 2 is: {tuple_0[part_2 : part_1+1]}', sep='\n')
    else:
        part_2 = len(lst)//2
        print(f'Tuple 1 is: {tuple_0[0:part_2]}',f'Tuple 2 is: {tuple_0[part_2 : part_1+1]}', sep='\n')
    

        
split_list([6,2,7,4,3])
split_list(['a', 'b', 'c', 1, 2, 3, 4, 'd', 5, "hello"])

# Alternate the elements between the two tuples(tuple 1 has elements with
# index (0,2,4,6,8, etc.) tuple 2 has elements with index (1,3,5,7,9, etc.))
def alternate_tuple(lst:list)->tuple:
    part_1 = len(lst)
    tuple_0 = tuple(lst)
    print(f'Tuple 1 is: {tuple_0[0:part_1:2]}',f'Tuple 2 is: {tuple_0[1: part_1:2]}', sep='\n')

alternate_tuple(['a', 'b', 'c', 1, 2, 3, 4, 'd', 5, "hello"])

# Write a program that has a list containing 5 tuples that each have 2 numbers.
# Sort the list in ascending order of the last number in each tuple.
def ordering_tuple(lst:list) -> list:
    sorted_list = sorted(lst, key=lambda x:x[1])
    return sorted_list

print(ordering_tuple([(3,2), (3,1), (4,3), (3,4), (3,5)]))

#Write a program that calculates the average of a list containing 5 elements.
def calculate_average(lst:list)->float:
    length = len(lst)
    summation = sum(lst)
    return round(summation / length,2)
print(calculate_average([2, 2, 3, 3, 4]))

# Add a number to the list that turns the average into 5.

def calculate_average_5(lst:list):
    length = len(lst)
    summation = sum(lst)
    average_1 = summation / length
    if average_1 == 5.0:
        print(f'The average was {average_1}. and No need for calibration')
    else:
        add_value = 5 * (length+1)  - summation    
        lst.append(add_value)
        summation = sum(lst)
        length = len(lst)
        average_2 = summation / length
        print(f'The average is: {average_1}',f'Added {add_value}, new list is {lst}',f'The average is now {average_2}',sep='\n')

calculate_average_5([2, 2, 3, 3, 4])

#Create a 2D list of size 6 by 6 containing only 3’s in 2 lines of code. Don’t use for-loops and
#keep to the PEP 8. Print the list.
# def two_D():
