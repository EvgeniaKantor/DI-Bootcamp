#Exercise 1 Write code that concatenates two lists together without using the + sign.
list1 = [1,2,3,4,5,6,7,8]
list2 = [9,10,11,12,13,14]
list1.extend(list2)

print(list1)

#Exercise 2 Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.
for num in range (1500,2501):
    if num % 5 == 0 and num % 7 == 0:
        print(num)
        
#Exercise 3 Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name = input('Enter your name: ')
if user_name in names:
    index = names.index(user_name)
    print(f'The index of the first occurrence of {user_name} is: {index}')
else:
    print("Name not found in the list.")

#Exercise 4 Ask the user for 3 numbers and print the greatest number.
user_number1 = int(input("Input the 1st number: "))
user_number2 = int(input("Input the 2nd number: "))
user_number3 = int(input("Input the 3rd number: "))
greatest_number = max(user_number1, user_number2, user_number3)
print("The greatest number is: ", greatest_number)

#Exercise 5 Create a string of all the letters in the alphabet
#Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.
alphabet = 'abcdefghijklmnopqrstuvwxyz'
vowels = {'a', 'e', 'i', 'o', 'u'}
for letter in alphabet:
    print(f'{letter} is a vowel.')
    else:
    print(f'{letter} is a consonant.')
