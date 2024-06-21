#challenge1
first_number = int(input("Enter the first number: "))
length = int(input("Enter the length of the list: "))

my_list = [first_number * (i+1) for i in range(length)]
print(my_list)

#challenge2
user_word = input("Enter a word: ")
new_word = ''
previous_char = ''
for char in user_word:
    if char != previous_char:
        new_word += char
        previous_char = char
print("New word:", new_word)