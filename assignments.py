
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
        
print(majority_element([3,1,3,3,1,1,2],7))
    
