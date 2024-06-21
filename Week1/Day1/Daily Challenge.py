import random

#exercise1
string = input("Enter your string")
if len(string) < 10:
    print('string not long enough')
elif len(string) > 10:
    print('string too long')
elif len(string) == 10:
    print('perfect string')
#exercise2
if len(string) >= 10:
    print("First character:", string[0])
    print("Last character:", string[-1])
#exercise3
for i in range(1, len(string) + 1):
    print(string[:i])
#exercise4
text_string = list(string)
random.shuffle(text_string)
print("Shuffle text:" + ''.join(text_string))