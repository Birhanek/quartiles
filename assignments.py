
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
            elif r_summer == l_summer:
                return half_index
            else:
                return -1

def summer(integer_list:list) -> int:
    sum = 0

    for num in integer_list:
        sum += num
    return sum


print(equilibriumPoint([8,4,8,8],4))

    

# Create a script that defines and manipulates various data types:
    # - Define an integer `x` with a value of 25.
    # - Define a float `y` with a value of 3.14.
    # - Define a string `z` with the value "Advanced Python".
    # - Define a boolean `is_active` with a value of False.
# Perform and print the results of the following operations:
    # - Compute and print the result of `x` divided by `y`.
    # - Convert the integer `x` to a string and concatenate it with the string `z`.
    # - Toggle the boolean value of `is_active`.

def task_1():
    x = 25
    y = 3.14
    z = "Advanced Python"
    is_active = False

    # compute and print the result of x divided by y
    print(x/y)

    # Convert the integer `x` to a string and concatenate it with the string `z`
    concatenated = str(x) + " " + z
    print(f'{concatenated}')

    # Toggle the boolean value of `is_active`
    print(not is_active)
task_1()


# String Manipulations and Lists
# Use list comprehension to create a new list `squares` containing the squares of each
# element in `numbers`
def task_2():
    n = 0
    text = "Python programming is powerful and versatile."

    # Extract and print the substring "programming" using slicing
    print(text[n+7:n+18])

    # Split the string into a list of words.
    list_of_words = text.split()
    print(list_of_words)

    #Join the list of words back into a single string using a hyphen `-` as a separator.
    print("-".join(list_of_words))

    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    squares = [i**2 for i in numbers]

    print(squares)
task_2()

# Tuples, Dictionaries, and Sets
def task_3():

    # Tuples operation
    coordinates = (34.0522, -118.2437)

    print(coordinates[0], coordinates[1])

    # dictionary operation like addition, update and creation of dictionary
    student = { 'name': 'Alice', 'age': 24, 'courses': ['Math', 'Science', 'English']}

    student['graduated'] = False

    student['age'] = 25

    print(student)

    # set operations 
    unique_numbers = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
    unique_numbers.add(6)
    unique_numbers.remove(2)

    if 3 in unique_numbers:
        print(unique_numbers)

task_3()

# ============== TASK 4 ===================================
# Write a program that checks if a number is prime:
# that returns True if `n` is a prime number and False otherwise
def is_prime(n:int) -> bool:
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        count = 0
        for num in range(2,n//2+1):
            if n % num == 0:
                count += 1
        if count > 0:
            return False
        else:
            return True

# Use this is_prime function to print all prime numbers between 1 and 50
prime_numbers = [num for num in range(1,51) if is_prime(num)]

print(prime_numbers)

# Create a list of integers from 1 to 15. Iterate through the list and perform the following
# to play the Fizz Buzz game
def fizzBuzz( lst : list):
    for num in lst:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")   
        elif num % 3 == 0:
            print('Fizz')     
        elif num % 5 == 0:
            
            print('Buzz')
        else:
            print(num)

lst_numbers = [num for num in range(1,16)]

fizzBuzz(lst_numbers)

# =================== END OF TASK 4 ======================
