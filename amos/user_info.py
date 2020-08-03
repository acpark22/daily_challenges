"""Easy Challenge:
    1. Create a program that will ask the user's name, age, and reddit username. 2. have it tell the info back, in the format: your name is (blank), you are (blank) years old, and your username is (blank). 3. For EC, have the program log this info in a file to be accessed later."""

import json

def user_info():
    
    name= input("What is your name? ")
    age= input("What is your age? ")
    username= input("What is your username? ")

    print(f"\nYour name is {name}, you are {age} years old, and your username is {username}.")

    info= {
        'name': name,
        'age': age,
        'username': username,
    }
    

    filename= 'reddit_user.json'
    with open(filename, 'w') as f:
        json.dump(info, f)


user_info()





