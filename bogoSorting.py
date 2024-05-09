#Bogosort algorithm is called also stupid or monkey sort algorithm 

#Reshuffle at random and checking is it sorted 

import random
import math

# To check whether the given list is in sorted manner or not, if it is already sorted it returns true

def check(nums:list) -> bool:
    for num in range(len(nums)):
        if nums[num] > nums[num + 1]:
            return False
    return True

def shuffle(nums:list) -> None:
    for num in range(len(nums)-2,0,-1):
        random_num = math.floor(random.random() * (num + 1))
        [nums[num],nums[random_num]] = [nums[random_num],nums[num]]

def bogo_sort(lst:list):
    iteration = 0
    while not check(lst):
        iteration +=1
        shuffle(lst)
    return lst

numbers = [5, 3, 1, 8, 2, 0]

print(bogo_sort(numbers))


