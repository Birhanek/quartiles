# Write a program that calculates the sum of all numbers from 1 to a certain number.

def exercise1():
    controller = True
    while controller:
        number = input(' Enter a number: ')
        if number.isnumeric():
            number_2 = int(number)
            summation = number_2 * (number_2 + 1) // 2
            print(summation)
        else:
            print(" You entered non numeric value and i can't process it.")
            controller = False

# exercise1()

# Write a program that puts the multiplication table from 1-10 of a number into a
# list and prints it.

def exercise_2():
    
    num = input(' Enter a number and i will give you the multiplication table of that number: ')
    if num.isnumeric():
        lst_multiplication = []
        numeric_number = int(num)
        for num in range(1,11):
            lst_multiplication.append(num * numeric_number)
        return lst_multiplication
    else:
        return f'Your input value is not number. Try again'
# print(exercise_2())

# Write a program that finds all of the numbers between 2950 and 5210 and are
# multiples of 13 and 9

def exercise_3() -> list | str:
    num_1 = input(' Enter number 1: ')
    num_2 = input(' Enter number 2: ')

    if num_1.isnumeric() and num_2.isnumeric():
        num_3 = int(num_1)
        num_4 = int(num_2)
        multiples = []
        for num in range(num_3, num_4+1):
            if num % 13 == 0 and num % 9 == 0:
                multiples.append(num)
        return multiples
    else:
        return f' Either the first number or second number you entered is not a number.'

#print(exercise_3())

# Write a program that counts the even and odd digits in a number.

def exercise_4():
    num_1 = input(' Enter integer number: ')

    if num_1.isnumeric():
        odd_count = 0
        even_count = 0
        nums = int(num_1)
        while nums > 0:
            rem_num = nums % 10
            nums = nums // 10
            if rem_num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        return "{0} has {1} odd digits and {2} even digits.".format(num_1,odd_count,even_count)
    else:
        return "You entered string not an integer number"

#print(exercise_4())

# Write a program that asks the user to create a password until they create a valid one. Then
# ask the user to put in their password until they get it correct. (Use the Input() function)

def exercise_51():
    while True:

        password = input('Create password: ')
        if len(password) <= 4 or len(password) > 6 or not password.isalpha():
            print('That does not fulfill the requirements, try again')
        else:
            print('Valid password!')
            break
    while True:
        enter_password = input('Enter your password: ')
        if password == enter_password:
            print('That is correct')
            break
        else:
            print('That is incorrect, try again')

#exercise_51()

# Write a program that encrypts the user password with a given shift

def encryption(shift:int):
    phrases = input('Enter any word you want to encrypt: ')
    encrypted = ''
    for letter in phrases:
        ascii_number = ord(letter)
        shifted_ascii = (ascii_number + shift) % 128
        character = chr(shifted_ascii)
        encrypted += character
    return encrypted
print(encryption(3))

def decryption(shift : int, cipher : str):
    
    decrypted = ''
    for symbol in cipher:
        ascii_number = ord(symbol)
        shifted_ascii = (ascii_number - shift) % 128
        character = chr(shifted_ascii)
        decrypted += character
    return decrypted

print(decryption(3,"Xvhuv#dqg#]heudv"))




    



