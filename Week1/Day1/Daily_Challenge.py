'''Using the input function, ask the user for a string. The string must be 10 characters long.
If it’s less than 10 characters, print a message which states “string not long enough”.
If it’s more than 10 characters, print a message which states “string too long”.
If it’s 10 characters, print a message which states “perfect string” and continue the exercise.
'''

import random

#exercise1#####################################################################################
string = input("Enter your string 10 characters long: ")
if len(string) < 10:
    print('String not long enough')
elif len(string) > 10:
    print('String too long')
elif len(string) == 10:
    print('The perfect string')
##############################################################################################
'''Then, print the first and last characters of the given text
'''
#exercise2#####################################################################################
if len(string) >= 10:
    print("First character:", string[0])
    print("Last character:", string[-1])
###############################################################################################
'''Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
The user enters "HelloWorld"
Then, you have to construct the string character by character
H
He
Hel
... etc
HelloWorld
'''
#exercise3####################################################################################
for i in range(1, len(string) + 1):
    print(string[:i])
##############################################################################################
'''Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example:

Hlrolelwod
'''

#exercise4###################################################################################
text_string = list(string) # Convert the string to a list of characters
random.shuffle(text_string) # Shuffle the list of characters randomly
print("Shuffle text:" + ''.join(text_string)) 
