
import json


# We are going to ask our user how many African countries can he guess with in a specified time

def guess():
    African_countries : list
    count = 0
    countries = list()
    length = int(input('How many countries do you know in Africa: '))
    while count < length:
        country = input(f'Enter the country {count + 1}: ')
        countries.append(country)
        count+=1

    with open('countries.json','r') as read_file:
        African_countries = json.load(read_file)
    
    count = 0
    for land in countries:        
        if land in African_countries:
            count+=1
             
    print(f'You guess only {count} countries')        
guess()



