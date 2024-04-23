
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
           
    print(f' Game Over! You guess only {score} countries')        
#guess()


class caesar:

    """
    In cryptography, a Caesar cipher, also known as shift cipher, is one of the simplest and most widely known encryption techniques.
    It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.
    For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.
    The method is named after Julius Caesar, who used it in his private correspondence.
    
    """

    def __init__(self,key:int) -> None:
        self.key = key
    # To  encrypt a given message based on a specified key
    def encrypt(self,plain_text:str):
        alphabets ="ABCDEFGHIJKLMNOPQRSTUVWXYZ ,."
        alphabets = alphabets.lower()
        list_alphabets = list(alphabets)

        cipher_text =''
        sequence = 0

        plain_text = plain_text.lower()
        list_plain_text = list(plain_text)
        for letter in list_plain_text:  
            if letter in list_alphabets:
                index = alphabets.index(letter)
                sequence = (index + self.key) % 29
                cipher_text += alphabets[sequence]
        return cipher_text
    
    # To decrypt a give secret message in to a human understandable language
    def decrypt(self,cipher_text:str):
        alphabets ="ABCDEFGHIJKLMNOPQRSTUVWXYZ ,."
        alphabets = alphabets.lower()
        list_alphabets = list(alphabets)
        list_cipher = list(cipher_text)

        plain_text =''
        sequence = 0
        for letter in list_cipher:
            if letter in list_alphabets:
                index = alphabets.index(letter)
                sequence = (index - self.key) % 29
                plain_text += alphabets[sequence]
        return plain_text



caesar_cipher = caesar(5)

encrypted = caesar_cipher.encrypt(" Het kan ook betekenen dat je iemand te veel toegeeft of te veel toegeeflijkheid toont, wat kan leiden tot het ontwikkelen van ongezonde gewoonten of attitudes. Bijvoorbeeld, ouders kunnen hun kinderen verwennen met cadeaus of privileges, of iemand kan zichzelf verwennen met een spa-dag of een luxe vakantie.")
print(encrypted)

print()

plain_text = caesar_cipher.decrypt(encrypted)
print(plain_text)

print()

print(caesar_cipher.decrypt('N qtaj uwtlwfrrnsl zxnsl Udymts'))

        





