list1 = [1,2,3,4,5,6,7,8]
list2 = [9,10,11,12,13,14]
list1.extend(list2)

print(list1)

for num in range (1500,2501):
    if num % 5 == 0 and num % 7 == 0:
        print(num)
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name = input('Enter your name: ')
if user_name in names:
    index = names.index(user_name)
    print(f'The index of the first occurrence of {user_name} is: {index}')
else:
    print("Name not found in the list.")

user_number1 = int(input("Input the 1st number: "))
user_number2 = int(input("Input the 2nd number: "))
user_number3 = int(input("Input the 3rd number: "))
greatest_number = max(user_number1, user_number2, user_number3)
print("The greatest number is: ", greatest_number)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
vowels = {'a', 'e', 'i', 'o', 'u'}
for letter in alphabet:
    print(f'{letter} is a vowel.')
    else:
    print(f'{letter} is a consonant.')