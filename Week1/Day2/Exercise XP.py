#exercise1:
my_fav_numbers = set({5, 7})
my_fav_numbers.add(13)
my_fav_numbers.add(100)
my_fav_numbers.remove(100)

friend_fav_numbers = set({6, 4})
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

#exercise_plus:
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
keys_to_remove = set({"name", "salary"})
for key in keys_to_remove:
    sample_dict.pop(key, None)

print(sample_dict)

#exercise3:
#False

#exercise4:
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
print(basket)
basket.remove("Blueberries")
print(basket)
basket.append("Kiwi")
print(basket)
basket.append("Apples")
print(basket)
count_apples = basket.count("Apples")
print(count_apples)
basket.clear()
print(basket)

#exercise4:
#An integer (more commonly called an int) is a number without a decimal point. A float is a floating-point number, which means it is a number that has a decimal place.
first = float(1.5)
my_list = [first]
while first<=5:
    first = first + 0.5
    my_list.append(first)
print(my_list)

#exercise5:
numbers = range(1,21)
for number in numbers:
    print(number)
for number in numbers:
    if number % 2 == 0:
        print(number)

#exercise6:
my_name = "Evgenia"
while True:
    user_name = input("Please enter your name: ")
    if user_name == my_name:
        print("It's true!")
        break
    else:
        print(user_name)
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
#exercise8:
tops = [1,2,3,4]
price = float(10)
toppings_list = []
while True:
    ask = input('Please enter the number of extra tops for pizza using this list: Cheese 1, Veggies 2, Sauces 3, Pesto 4 or type done:')

    if ask.lower() == "done":
        print("Thank you for your order!")
        break

    if int(ask) in tops:
        toppings_list.append(int(ask))
        print('We have ', ask, 'choose another one')

    else:
        print('Invalid')
your_price = price + 2.5 * len(toppings_list)
print("total price is: ", your_price)

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

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
print(sandwich_orders)
finished_sandwiches = []
for sandwiches in sandwich_orders:
    finished_sandwiches.append(sandwiches) and sandwich_orders.remove(sandwiches)
    print(finished_sandwiches)
    print("I made your", sandwiches)

