import os #provides a portable way of using operating system-dependt functionality
import requests #allows making HTTP requesrs in Py
import random

dir_path = os.path.dirname(os.path.realpath(__file__))
url = 'http://norvig.com/ngrams/sowpods.txt' #Retrieves the directory path of the current script file
response = requests.get(url)

# Check if the request was successful (status code 200)
def download_word_list():
    if response.status_code == 200:
        with open(os.path.join(dir_path, 'words.txt'), 'w') as file_obj:
            file_obj.write(response.text)
        print("Content downloaded and saved successfully.")
    else:
        print("Failed to download content. Status code:", response.status_code)

def get_words_from_file(file_path):
    with open(file_path, 'r') as file_obj:
        words = file_obj.read().split()
    return words

def get_random_sentence(length, words):
    random_words = random.sample(words, length)
    sentence = ' '.join(word.lower() for word in random_words)
    return sentence

def main():
    print("Welcome to Random Sentence Generator!")
    print("This program generates a random sentence of a specified length.")

    # Download word list
    download_word_list()

    # Get words from the file
    file_path = 'words.txt'
    if os.path.exists(file_path):
        words = get_words_from_file(file_path)

        # Ask the user for the length of the sentence
        while True:
            try:
                length = int(input("Enter the length of the sentence (2-20): "))
                if length < 2 or length > 20:
                    raise ValueError("Invalid length")
                break
            except ValueError as e:
                print("Invalid input. Please enter a number between 2 and 20")

        # Generate and print the random sentence
        sentence = get_random_sentence(length, words)
        print("Random sentence:", sentence)

if __name__ == "__main__": #Checks if the script is being run directly (not imported as a module)
    main()

