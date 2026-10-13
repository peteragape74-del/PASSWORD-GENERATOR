# PASSWORD-GENERATOR
A python code that generates passwords when the password inputted by the user is weak

## Description of the code

This program is a simple password checker and password strength validator.

It does the following:

- Asks the user to enter a password
- Checks whether the password contains:
  - a lowercase letter
  - an uppercase letter
  - a digit
  - a special character like !, @, #, $, %
- Compares the entered password to a fixed correct password: `Dadswork123@#`
- If the password matches the correct one and includes all required character types, it prints that the password is strong and correct
- If not, it tells the user what is missing and whether the password is incorrect
- It also generates a random suggested password to help the user create a stronger one

In short, this code tests whether a password is both correct and secure, and gives feedback if it is not.
