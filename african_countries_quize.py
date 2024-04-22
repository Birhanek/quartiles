
import json


# We are going to ask our user how many African countries can he guess with in a specified time

def guess():
    African_countries : list
    score = 0
    lives = 3
    print('You have 3 lives and if you make incorrect guess there is a reduction in life!')
    with open('countries.json','r') as read_file:
        African_countries = json.load(read_file)
    while True:
        if lives > 0 and len(African_countries) > 0:
            country = input(f'Enter the country: ')
            if country in African_countries:
                print(f'Good guess!')
                score +=1
                African_countries.remove(country)
            else:
                print('You missed it!')
                lives -=1
        else:
            break


           
    print(f'You guess only {score} countries')        
guess()



