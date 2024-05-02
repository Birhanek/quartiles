# Write a program that checks if a list is empty or not. Use the len() function!

def check_is_empty(lst_1:list) ->str:

    if(len(lst_1) ==0):
        return f'The list is empty!'
    else:
        return f'The list is not empty!'

print(check_is_empty([]))
print()
print(check_is_empty([1,2,3,4,'techno']))

#Write a program that reorders a list and removes the largest and smallest
# number from it.

def reorder_lst(lst_2:list[int])->list:
    # maximum = max(lst_2)
    # minimum = min(lst_2)
    if(len(lst_2) == 0):
        return []
    else:
        lst_2.sort()
        lst_2.pop()
        lst_2.pop(0)
        return lst_2

print(reorder_lst([6,6,3,2,4,5,5]))

#Write a program that converts a list (size of 5) of characters into a string
def lst_to_str(lst_3:list) ->str:
    if len(lst_3) != 5:
        return "This list doesn’t have the right size"
    else:
        lst_characters =''
        for letter in lst_3:
            lst_characters += letter
        return lst_characters
print(lst_to_str( ['h', 'e', 'l', 'l']))

# Someone called Frank has a list containing how many days he was sick each
# quarter of a year. So the first element of the list dictates how many days he was sick in the
# first quarter of the year. Frank usually has dance lessons every day, but when he is sick he
# doesn’t go. Write a program that shows how many days Frank went dancing last year.
def frank_health(lst_4:list) ->str:
    if len(lst_4) !=4:
        return f'No enough data'
    else:
        sum__sick_days = 0
        for day in lst_4:
            if day < 0:
                return f"Frank can't be sick for {day} days!"
            else:
                sum__sick_days += day
        return f'Frank was sick for {sum__sick_days} days. He went dancing for {365 - sum__sick_days} days'
print(frank_health( [0,4,1,-1]))

# Frank now has danced for another year, making another list. He wants to
# check in which quarter of the last two years he got sick the most. Write a program that turns
# the two lists into one list of length 8 and then check which quarter he was sick the most
# often
def analysis_frank_health(lst_1:list, lst_2:list) ->str:
    sickness_days = lst_1 + lst_2
    print(sickness_days)
    maximum = max(sickness_days)
    sickness_quarter = sickness_days.index(maximum)
    quarter = ''
    if(sickness_quarter < len(sickness_days)//2):
        quarter = 'Year one'
        sickness_quarter = lst_1.index(maximum)
    else:
        quarter= 'Year two'
        sickness_quarter = lst_2.index(maximum)
    return f"The full list of frank’s sick days is: {sickness_days}.\nFrank was sick the most in quarter {sickness_quarter + 1} of the {quarter}."
print(analysis_frank_health([10, 4, 5, 7], [19, 8, 2, 12]))
print()
print(analysis_frank_health([0, 3, 1, 2], [4, 4, 0, 0]))     


    
