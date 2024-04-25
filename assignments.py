
# a function that searches the majority number in a list
# A majority element in a list A of size N is an element that appears strictly more than N/2 times in the list.
def majority_element(number_list:list,size:int):
    temp = 0
    count = 0 
    index = 0
    for num in range(0,size):
        temp = 1
        for num_j in range(num+1,size):
            if number_list[num] == number_list[num_j]:
                temp +=1
        if count < temp:
            count = temp
            index = num
    if count > size //2:
        return number_list[index]
    else:
        return -1
        
print(majority_element([3,1,4,3,4,1,1,4,4,4,4,4],12))

#Given an array A of n non negative numbers. 
#The task is to find the first equilibrium point in an array. 
#Equilibrium point in an array is an index (or position) such that the sum of all elements before that index is same as sum of elements after it.

def equilibriumPoint(positive_integer_list:list, size:int) -> int:

    if size == 1:
        return 0
    else:
        half_index = size //2
        while True:
            l_summer = summer(positive_integer_list[0:half_index])
            r_summer = summer(positive_integer_list[half_index+1:size])

            if(l_summer > r_summer):
                half_index -= 1
            elif r_summer > l_summer:
                half_index += 1
            else:
                return half_index

def summer(integer_list:list) -> int:
    sum = 0

    for num in integer_list:
        sum += num
    return sum


print(equilibriumPoint([8],1))

    
