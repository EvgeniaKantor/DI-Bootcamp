print("---ex1---")
print("Hello World!\n"*4)
print("---ex2---")
print((99**3)*8)
print("---ex3---")
# 5 < 3
print("False")
# 3 == 3
print("True")
# 3 == "3"
print("False")
# "3" > 3
print("False")
# "Hello" == "hello"
print("False")
print("---ex4---")
computer_brand = "Asus"
print(f"I have a {computer_brand} computer")
print("---ex5---")
name = 'Evgenia'
age = "39"
shoe_size = "39"
info = f'{name} is {age} years and has {shoe_size} shoe-size'
print(info)
print("---ex6---")
a = 5
b = 3
if a>b:
    print("Hello World")
print("---ex7---")
num = int(input("Write a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
print("---ex8---")
name = str(input("Write a name: "))
if name == "Evgenia":
    print("Hello, I miss you!")
your_height = int(input("Write a height in cm: "))
if your_height > 145:
    print("You are welcome!")
else:
    print("You are not tall enough")
