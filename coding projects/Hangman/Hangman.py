import random
from words import data

def get_words(data):
    choose = random.choice(data)
    # userletter = input("Type the name").upper()
    while '-' in data or ' ' in data:
        choose = random.choice(data)
        

get_words(data)