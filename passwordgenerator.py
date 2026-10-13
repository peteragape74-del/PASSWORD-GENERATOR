#PASSWORD CHECKER PYTHON CODE

import random
import string

lower = False
upper = False
digit = False
special_char = False

while True:
    correct_password = 'Dadswork123@#'
    password = input('Enter your password: ')
    for char in password:
        if char.islower():
            lower = True
        if char.isupper():
            upper = True
        if char.isdigit():
            digit = True
        if char in '!@#$%':
            special_char = True

    if password == correct_password and lower and upper and digit and special_char:
        print('password is strong and correct')
        break
    else:
        if password != correct_password:
            print('incorrect password')
        if not lower:
            print('no lower case')
        if not upper:
            print('no upper case')
        if not digit:
            print('no digit')
        if not special_char:
            print('no special character')

        character = string.ascii_letters + string.digits + '#@!$#&'
        strong_password = ''.join(random.choice(character)for _ in range(12))
        print(f'suggested password: {strong_password}')
    
