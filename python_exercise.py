# Printing a single poem with multiple lines
def output():
    print('''Twinkle, twinkle, little star,\n\tHow I wonder what you are!
      \t\tUp above the world so high,\n\t\t Like a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are!
          ''')

output()

# determining a given number is odd or even
def even_odd(n):
    print(f'{n} is even number') if(n % 2 == 0) else print(f'{n} is odd number')

even_odd(8)

# Write a program that has two integers, print their product(multiplication) only if the product is
# equal to or lower than 1000. Otherwise, print their sum(addition).

def calculate(num_1, num_2):
    print(f'The result is {num_1 * num_2}') if((num_1 * num_2) <= 1000) else print(f'The result is {num_1 + num_2}')
calculate(20,30)

# Write a program that reverses a number between 100-999.
def reverse_number(num):
    if(num > 100 and num < 1000):
        reverse =''
        while(num > 0):
            remainder = num % 10
            reverse += str(remainder)
            num = num // 10
        print(f'The reverse is {int(reverse)}')
    else:
        print(f'{num} is below the threshold')if(num < 100) else print(f'{num} is above the threshold')

reverse_number(18)