#Bogosort algorithm is called also stupid or monkey sort algorithm 

#Reshuffle at random and checking is it sorted 

import random

# To check whether the given list is in sorted manner or not, if it is already sorted it returns true

def check(nums:list) -> bool:
    for num in range(len(nums) - 1):
        if nums[num] > nums[num + 1]:
            return False
    return True

def shuffle(nums:list) -> None:
    for num in range(len(nums)):
        random_num = random.randint(0,len(nums) - 1)
        nums[num],nums[random_num] = nums[random_num],nums[num]

def bogo_sort(lst:list):
    iteration = 0
    while not check(lst):
        iteration +=1
        shuffle(lst)
        print(iteration)
    return lst

numbers = [5, 3, 1, 8, 2, 0,9,78,90,56,23]

print(bogo_sort(numbers))


