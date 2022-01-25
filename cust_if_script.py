#!/usr/bin/env python3
"""My first PY program using
   if, elif, else - A simple program using conditionals to make a decision."""


message = '--- Future personalized advise for you  ---\n '

# wrap connection in a float() to accept decimals as numbers
age = float(input("What is your age?"))

# if input value was higher or equal to 25
if age >= 85 and age <= 115 :
    message = message + 'Start looking for a Cementery'
elif age >= 65 and age <= 85 :
    message = message + 'Remember to take your pills'
elif age >= 18 and age <= 65 :
    message = message + 'Safe some money for retirement'
elif age >= 0 and age <=18 :
    message = message + 'Have fun & ask your daddy for some money'
else:
    message = message + 'you must be from MARS or just learned to code'
print(message)

