# the exercise from "Lambda, Map, Reduce & Filter Functions"

people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]

# Filter names with lengths less than or equal to 4, then map to add "Hello, " prefix
greetings = map(lambda name: "Hello, " + name + "!", filter(lambda name: len(name) <= 4, people))

""" Print the greetings """

for greeting in greetings:
    print(greeting)

#______________________________________________Exercise 1

def display_message():
    """A function that tells everyone what I am learning in this course"""
    print("I am learning Python")

display_message()

#______________________________________________Exercise 2

def favorite_book(title):
    """A function that tells everyone my favorite book through the arg title"""
    print("One of my favorite books is " + title)

favorite_book("Alice in Wonderland")

#_______________________________________________Exercise 3

def describe_city(city, country = "Israel"):
    """A function that tells everyone a simple sentence, such as "<city> is in <country>"""
    print(city + " is in " + country)

describe_city("Reykjavik", "Iceland")

#due to the country parameter a default value we can input only city:
describe_city("Tel-Aviv")

#_______________________________________________Exercise 4

import random as rd

def random_number(s):
    """A function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100"""
    # check that the number is in the required range
    if s <= 0 or s >= 100:
        print(f"Error! Your number is {s} not between 1 and 100")
        return False
    #if number is in the range then generate a random number and make a comparison
    else:
        r_n = rd.randint(1, 101)
        if s!=r_n:
            print("Error numbers are different")
            print(f"The numbers are : {s} and {r_n}")
        else:
            print("Numbers are equal")
            return True

s = int(input("Enter a number: "))
random_number(s)


#_______________________________________________Exercise 5

def make_shirt(size = "Large", text = "I love Python"):
    """ A function that accepts a size and the text of a message that should be printed on the shirt """
    size_list = ["large", "medium", "small"]
    #check that the input data are correct
    if size.lower() not in size_list:
        print("Size is not recognized")
        return False
    return f"The size of the shirt is {size.capitalize()} and the text is {text.capitalize()}"


# Make a shirt with any size with a different message
size = input("Enter a size: ")
text = input("Enter your text: ")
# Call the function
result3 = make_shirt(size, text)
print(result3)
#Large by default with a message that reads “I love Python” by default
result4 = make_shirt()
print(result4)
#Large shirt with the default message
result5 = make_shirt(size = "large")
print(result5)
#Medium shirt with the default message
result6 = make_shirt(size = "medium")
print(result6)
#Make a shirt of any size with a different message.
result7 = make_shirt(size = "small", text = "I love developer institute")
print(result7)
#Call the function make_shirt() using keyword arguments
print("-----Bonus----")
result_bonus = make_shirt(**{"size": "Large", "text": "I love developer institute"})
print(result_bonus)


#_______________________________________________Exercise 6

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magician(magician_name):
    """ A function that prints the name of the magician """
    [print(name) for name in magician_name]

show_magician(magician_names)

def make_great(magician_names):
    '''A function that modifies the original list of magicians'''
    for i in range(len(magician_names)):
        magician_names[i] = "the Great "+magician_names[i]
    return magician_names

make_great(magician_names)
show_magician(magician_names)

#_______________________________________________Exercise 7

import random as rd
def get_random_temp(season):
    """This function should return an integer between -10 and 40 degrees (Celsius)"""
    seasons_temps = {'spring': (16., 24.), 'summer': (24., 40.), 'autumn': (16., 24.), 'winter': (-10., 16.)}
    r_deg = rd.uniform(seasons_temps[season][0], seasons_temps[season][1])
#    if r_deg not in range(-10, 41):
#        print("Invalid temperature")
#        return False
    return r_deg
#print(get_random_temp())

def main():
    """Informs the user of the temperature"""
    #dictionary of Months
    months = {1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring', 6: 'Summer', 7: 'Summer', 8: "Summer",
              9: 'Autumn', 10: "Autumn", 11: 'Autumn', 12: "Winter"}
    month_num = int(input('Enter the month number'))
    if month_num > 12 or month_num < 1:
        print('Invalid month number')
    season = months[month_num]
    temp_deg = get_random_temp(season.lower())
    print(f"The temperature right now is {temp_deg} degrees Celsius")
    if temp_deg<0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif 0<=temp_deg<16:
        print("Quite chilly! Don’t forget your coat")
    elif 16<=temp_deg<=23:
        print("Good weather!")
    elif 24<=temp_deg<=32:
        print("Sunny day")
    elif 32<temp_deg<=40:
        print("Drink more water")
main()

#_______________________________________________Exercise 8
data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def take_quiz():
    """ A function that asks the questions to the user, and check his answers"""
    correct_answers = 0
    incorrect_answers = 0
    wrong_answers = []

    for question_dict in data:
        question = question_dict["question"]
        correct_answer = question_dict["answer"]
        user_answer = input(question + " ")

        if user_answer.lower() == correct_answer.lower():
            correct_answers += 1
        else:
            incorrect_answers += 1
            wrong_answers.append({"question": question, "user_answer": user_answer, "correct_answer": correct_answer})

    return correct_answers, incorrect_answers, wrong_answers

def inform_user(correct_answers, incorrect_answers, wrong_answers):
    """ A function that informs the user of his number of correct/incorrect answers"""
    print(f"\nYou got {correct_answers} correct answer(s) and {incorrect_answers} incorrect answer(s).")

    if incorrect_answers > 0:
        print("\nQuestions you answered incorrectly:")
        for wrong_answer in wrong_answers:
            print(f"\nQuestion: {wrong_answer['question']}")
            print(f"Your Answer: {wrong_answer['user_answer']}")
            print(f"Correct Answer: {wrong_answer['correct_answer']}")

    if incorrect_answers > 3:
        print("\nYou had more than 3 wrong answers. Please play again.")

# Main program
def main():
    correct_answers, incorrect_answers, wrong_answers = take_quiz()
    inform_user(correct_answers, incorrect_answers, wrong_answers)

if __name__ == "__main__":
    main()




