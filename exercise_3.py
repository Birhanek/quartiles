# Write a program that tells the user whether a letter is a vowel or not.

def exercise1():
   letter = input('Enter a letter: ')

   vowels = set('aeiou')

   if letter in vowels:
       print(f'This is a vowel')
   else:
       print(f'This is not a vowel')
#exercise1()

# Write a program that prints whether an integer is in between 1000 and 2000. If it is not, print
# whether it is lower than 1000 or higher than 2000.
def exercise2():
    num_1 = int(input('Enter an integer: '))

    if num_1 >=1000 and num_1 <=2000:
       print('This number is in between 1000 and 2000')
    elif num_1 < 1000:
       print('This number is lower than 1000')
    else:
       print('This number is higher than 2000')

#exercise2()

# Write a program that prints the sum of 3 given numbers, but if all 3 numbers are the same it
# should print 4 times the sum of the 3 numbers.

def exercise3():
   first_number = float(input('Enter Number-1: '))
   second_number = float(input('Enter Number-2: '))
   third_number = float(input('Enter Number-3: '))

   sum_numbers = 0
   if first_number == second_number == third_number:
       sum_numbers = first_number * 3
       multiplied_number = sum_numbers * 4
       print(f'Those numbers are the same! The sum of the numbers is {sum_numbers} Multiplied by 4 this becomes {multiplied_number}')
   else:
       sum_numbers = first_number + second_number + third_number
       print(f'The sum of these numbers is {sum_numbers}')

#exercise3()

# Write a program that finds the largest of 4 numbers.

def exercise4():
    first_number = float(input('Enter Number-1: '))
    second_number = float(input('Enter Number-2: '))
    third_number = float(input('Enter Number-3: '))
    fourth_number = float(input('Enter Number-4: '))
    largest = first_number
    if second_number > largest and second_number >= third_number and second_number >= fourth_number:
        largest = second_number
    elif third_number >= fourth_number and third_number >= largest and third_number >= second_number:
        largest = third_number
    elif fourth_number > third_number and fourth_number > largest and fourth_number > second_number:
        largest = fourth_number
    print(f'The largest number is {largest}')

#exercise4()

#Write a program that calculates how much money someone has left after taxes, given their income.
def exercise5():
    salary = float(input('Enter your salary and I will tell how much it will left after tax: '))
    salary_after_tax = 0
    if salary < 0:
        print("Salary can't be negative")
    else:
        if salary < 67000:
            salary_after_tax = salary - (salary * 0.24)
            print(f'Your income after taxes is {salary_after_tax} euro’s')
        elif salary < 97000:
            salary_after_tax = salary - (salary * 0.31)
            print(f'Your income after taxes is {salary_after_tax} euro’s')
        else:
            salary_after_tax = salary - (salary * 0.34)
            print(f'Your income after taxes is {salary_after_tax} euro’s')
#exercise5()

#Write a program that takes a string with a maximum size of 5. Do something different
#depending on the size of the string:

def exercise6():
    letter = input('Enter from a single letter to maximum 5 letters of a word: ')
    if len(letter) > 5:
        print("Sorry, I can't process")
    else:
        if len(letter) == 1:
            print(6*letter)
        elif len(letter) == 2:
            temp = letter[1] + letter[0]
            print(temp)
        elif len(letter) == 3:
            temp = letter[2] + letter[0] + letter[1]
            print(temp)
        elif len(letter) == 4:
            temp = letter[::-1]
            print(temp)
        else:
            print(*letter.replace('','t').removeprefix('t').removesuffix('t'))

#exercise6()    
       
# Write a program that gives the user a basic test with three questions. If they have a question
# wrong stop the quiz, if they have it right give them the next question
def exercise7():
    while True:
        answer_1 = int(input('What is 2 * 2? '))
        if answer_1 == 4:
            print('That is correct')
            answer_2 = int(input('What is 6 / 3? '))
            if answer_2 == 2:
                print('That is correct!')
                answer_3 = int(input('What is 9 * 9? '))
                if answer_3 == 81:
                    print('Correct! You passed the test!')
                    break
                else:
                    print('That is false, you failed the test!')
                    break
            else:
                print('That is false, you failed the test!')
      #          break
        else:
            print('That is false, you failed the test!')
            break
#exercise7()


# Arbitrary numbers of arguments: this creates tuples fruits =('Mango','Banana','Appel','Avocado')
def fruiterer(*fruits):
    for fruit in fruits:
        print(fruit)

fruiterer('Mango','Banana','Appel','Avocado')

# Arbitrary numbers of arguments: this creates dictionary => keyword argument is changed to dictionary
def country_capital(**countries):

    print('Countries')
    for key,value in countries.items():
        print('The capital of {0} is {1}.'.format(key,value))

country_capital(Ethiopia='Addis Ababa', Netherlands='Amsterdam',Kenya='Nairobi',Germany='Berlin')


import functools

def comprehension():
    lst = filter(lambda x:x % 2 == 0, range(1,101))
    print(list(lst))

    print()
    #   filtering negative numbers 
    lst = filter((lambda x: x < 0), range(-20,5)) 
    print (list(lst)) 

    lst_2 = [90,46,78,34,56,67,35,12,32,47]

    tpl_1 = tuple(range(1,11))

    my_tuple = ("11",11,[2,"two",("six",6)],(5,"fair"))
    print(my_tuple[-1], type(my_tuple[-1]), sep='\n')
    print(my_tuple[-1][1])
    print(my_tuple[2][2][0])

    my_dict ={'name':'Birhane','born':1996,'gender':'M'}
    my_dict_2 = {'country':'Ethiopia'} | dict(region='Tigray',religion='Orthodox')
    my_dict['city'] = 'Addiss Ababa'

    # my_dict_3 = {**my_dict, **my_dict_2}
    # my_dict.update(my)
    # print(my_dict_3)

    dict1 = {'x': 10, 'y': 8}
    dict2 = {'a': 6, 'b': 4, 'a':45, 'a':78, 'b':56}
    #dict2['a'] = 26
    merged_dict = my_dict | my_dict_2
    print(dict1 | dict2)
    print(merged_dict)
    print(dict2)

    # print(tpl_1)
    # print()
    # print(my_dict)
    lst_2.sort()
    lst_2.reverse()
    print(lst_2)
    
    #  implementing max() function, using 100
    print (functools.reduce(lambda a,b: a+b, [7, 12, 45, 100, 15]))

comprehension()



