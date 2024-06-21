#exercise1
print("Hello World!\n"*4,"I love python\n"*4)
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


