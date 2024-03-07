#exercise1:
my_fav_numbers = set({5, 7})
my_fav_numbers.add(13)
my_fav_numbers.add(100)
my_fav_numbers.remove(100)

friend_fav_numbers = set({6, 4})
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

#exercise2:
#False

#exercise3:
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
print(basket)
basket.remove("Blueberries")
print(basket)
basket.append("Kiwi")
print(basket)
basket.insert(0,"Apples")
print(basket)
count_apples = basket.count("Apples")
print(count_apples)
basket.clear()
print(basket)

#exercise4:
#An integer (more commonly called an int) is a number without a decimal point. A float is a floating-point number, which means it is a number that has a decimal place.
first = 1.5
my_list = [first]
while first<=5:
    first = first + 0.5
    my_list.append(first)
print(my_list)

#exercise5:
numbers = range(1,21)
for i in numbers:
    print(i)

for index, value in enumerate(range(1, 21)):
    if index % 2 == 0:
        print(index)

#exercise6:
my_name = "Evgenia"
while True:
    user_name = input("Please enter your name: ")
    if user_name == my_name:
        print("It's true!")
        break
    else:
        print(user_name)
#v2_new
my_name = "Evgenia"
user_name = ""

while user_name != my_name:
    user_name = input("Please enter your name: ")
    if user_name != my_name:
        print(user_name)
    else:
        print("It's true!")

#exercise7:
fruits = input('Please enter your favorite fruits, you need to separate the fruits with a single space, eg. "apple mango cherry": ')
favorite_fruits = fruits.split()
while True:
    ask_fruit = input('Please enter one fruit: ')
    if ask_fruit in favorite_fruits:
        print("Enjoy your favorite fruit!")
        break
    else:
        print("You chose a new fruit. I hope you enjoy!")

#v2_new
fruits = input('Please enter your favorite fruits, separated by a single space, e.g., "apple mango cherry": ')
favorite_fruits = fruits.split()
ask_fruit = ""
while ask_fruit not in favorite_fruits:
    ask_fruit = input('Please enter one fruit: ')
    if ask_fruit in favorite_fruits:
        print("Enjoy your favorite fruit!")
    else:
        print("You chose a new fruit. I hope you enjoy!")

#exercise8:
tops = ['cheese', 'veggies', 'sauces', 'pesto']
price = 10.0
toppings_list = []

while True:
    ask = input('Please enter the extra topping for pizza using this list: Cheese, Veggies, Sauces, Pesto or type "done": ')

    if ask.lower() == "done":
        print("Thank you for your order!")
        break

    if ask in tops:
        toppings_list.append(ask)
        print('We have', ask, ', choose another one')
    else:
        print('Invalid topping, please choose from the list.')

your_price = price + 2.5 * len(toppings_list)
print("Your order:", toppings_list, "Total price is:", your_price)

#exercise9:
little_kids = range(3)
kids = range(3,13)
adults = range(13,120)
total_cost = 0
while True:
    age = input("What is your age? (type 'done' to finish)")
    if age.lower() == 'done':
        break
    if int(age) in little_kids:
        print("Your ticket costs free")
    elif int(age) in kids:
        print("Your ticket costs 10")
        total_cost += 10
    elif int(age) in adults:
        print("Your ticket costs 15")
        total_cost += 15
print("Total cost for the family's tickets: $" + str(total_cost))

names = ["Andru", "Tom", "Alice", "Yan"]
new_list = []
film_for = range (16,21)
for name in names:
     age = int(input(f"Please enter {name}'s age: "))
     if age in film_for:
        new_list.append(name)
print("The following teenagers are allowed to watch the movie:")
print(new_list)

#exersise10:
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
print(sandwich_orders)

finished_sandwiches = []
for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)
    print("I made your", sandwich)

print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)


