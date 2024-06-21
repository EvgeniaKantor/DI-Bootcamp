#examle1
def calculation(a, b):
    addition = (a + b)
    subtraction = (a - b)
    return (addition, subtraction)
res = calculation(40, 10)
print(res)

#exetcise1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dictionary = dict(zip(keys, values))
print(dictionary)

#exercise2
#how much does each family member have to pay:
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
def your_cost (your_name, age):
    for your_name, age in family.items():
        if age in range(3):
            cost = 0
            print(your_name, 'the ticket is free')
        elif age in range(2, 13):
            cost = 10
            print(your_name, 'the ticket is $10')
        else:
            cost = 15
            print(your_name, 'the ticket is $15')
your_cost (your_name= 'Rick', age = 43)
#How much does each family member have to pay
for name, age in family.items():
    if age < 3:
        family[name] = 0
    elif age <= 12:
        family[name] = 10
    else:
        family[name] = 15
total_sum = sum(family.values())

print("The total sum is:", total_sum)

#bonus
family = {}
num_people = int(input("How many people are in your family? "))
for i in range(num_people):
    name = input("Enter the name of family member: ")
    age = int(input(f"Enter {name}'s age: "))
    family[name] = age
print(family)

#exercise3
brand = {'name': 'Zara',
        'creation_date': 1975,
        'creator_name': 'Amancio Ortega Gaona',
        'type_of_clothes': ['men', 'women', 'children', 'home'],
        'international_competitors': ['Gap', 'H&M', 'Benetton'],
        'number_stores': 7000,
        'major_color':{'France': 'blue', 'Spain': 'red', 'US': ('pink', 'green')}}
#3_Change the number of stores to 2
brand['number_stores'] = 2
#4_Print a sentence that explains who Zaras clients are
client = brand['type_of_clothes']
client.pop()
client_str = ', '.join(client)
print(client_str)
print(brand['name'], 'was created in', brand['creation_date'], 'by', brand['creator_name'], '. Our clients are', client_str, ".")
#5_Add a key called country_creation with a value of Spain
brand['country_creation'] = 'Spain'
print(brand)
#6_Check if the key international_competitors is in the dictionary. If it is, add the store Desigual
if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')
print(brand)
#7_Delete the information about the date of creation
if 'creation_date' in brand:
    brand.pop('creation_date')
print(brand)
#8_Print the last international competitor
brand['international_competitors'].pop()
print(brand)
#9_Print the major clothes colors in the US
major_color_us = brand['major_color'].get('US')
print("Major clothes colors in the US:", ', '.join(major_color_us))
#10_Print the amount of key value pairs (ie. length of the dictionary)
print("The length of the dictionary:", len(brand))
#11_Print the keys of the dictionary
print([k for k, v in brand.items()])
#12_Create another dictionary called more_on_zara with the following details
more_on_zara = brand.copy()

if 'creation_date' not in more_on_zara:
    more_on_zara['creation_date'] = 1975
if 'number_stores' in more_on_zara:
    more_on_zara['number_stores'] = 10000
print(more_on_zara)
#13_Use a method to add the information from the dictionary more_on_zara to the dictionary brand
brand.update(more_on_zara)
print(brand)
#14_Print the value of the key number_stores. What just happened ?
v_number_stores = brand.get('number_stores')
print(v_number_stores) #Printed the new value

#exercise4
#Use a for loop to recreate the 1st result {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
#the first way we have stdied on the lesson
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
values = [0,1,2,3,4,5]
disney_users_A = {}
for key, value in zip(users,values):
    disney_users_A[key] = value
print(disney_users_A)

#second_way
#Use a for loop to recreate the 1st result {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
disney_users_B = {}
for i, user in enumerate(users):
    disney_users_B[i] = user
print(disney_users_B)

#Use a method to recreate the 3rd result {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
sorted_users = sorted(users)
disney_users_C = {}
for i, user in enumerate(sorted_users):
    disney_users_C[user] = i
print(disney_users_C)

#The characters, which names contain the letter “i”
disney_users_A_i = {}
for i, user in enumerate(users):
    if 'i' in user:
        disney_users_A_i[user] = i
print(disney_users_A_i)

#The characters, which names start with the letter “m” or “p”
disney_users_A_mp = {}
for i, user in enumerate(users):
    if user.startswith('M') or user.startswith('P'):
        disney_users_A_mp[user] = i
print(disney_users_A_mp)






