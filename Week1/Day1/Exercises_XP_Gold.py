'''Exercise 1 : Hello World-I Love Python
Instructions
Print the following output in one line of code:
Hello world
Hello world
Hello world
Hello world
I love python
I love python
I love python
I love python
'''
####################################################################
#exercise1
print("Hello World!\n"*4,"I love python\n"*4)
####################################################################

'''Exercise 2 : What Is The Season ?
Instructions
Ask the user to input a month (1 to 12).
Display the season of the month received :
Spring runs from March (3) to May (5)
Summer runs from June (6) to August (8)
Autumn runs from September (9) to November (11)
Winter runs from December (12) to February (2)
'''
##################################################################
#exercise2
month_names = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

seasons = {
    "Spring": [3, 4, 5],
    "Summer": [6, 7, 8],
    "Autumn": [9, 10, 11],
    "Winter": [12, 1, 2]
}

month_number = int(input("Please enter a month number (1 to 12): "))

if month_number in month_names:
    month_name = month_names[month_number]
    for season, months in seasons.items():
        if month_number in months:
            print(f"The month of {month_name} is in the {season} season.")
            break
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
#####################################################################
