#________________________________________Challeng_1
# usually method:
def change_input():
    user_input = input("Print your phrase: ")
    words = user_input.split()
    words.sort()  # Sort the list of words
    output_string = ", ".join(words)
    print(output_string)

change_input()


# Accept input from the user
user_input_new = input("Print your phrase: ")

# Split the input string into words, strip whitespace from each word, and sort them alphabetically using list comprehension
sorted_words = sorted([word.strip() for word in user_input_new.split(' ')])

# Join the sorted words with commas and print the result
output_string_new = ", ".join(sorted_words)

print("Sorted words with commas:", output_string_new)

#________________________________________Challeng_2

def longest_word(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Initialize variables to store the longest word and its length
    longest = ''
    max_length = 0

    for word in words:
        if len(word) > max_length:
            longest = word
            max_length = len(word)

    return longest


# Test cases
print(longest_word("Margaret's toy is a pretty doll."))  # ➞ "Margaret's"
print(longest_word("A thing of beauty is a joy forever."))  # ➞ "forever."
print(longest_word("Forgetfulness is by all means powerless!"))  # ➞ "Forgetfulness"