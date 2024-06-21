from anagram_checker import AnagramChecker

class Anagrams(AnagramChecker):
    def __init__(self, url):
        super().__init__(url)

def menu(anagram_instance):
    while True:
        print("Input any word to continue or type 'exit' to quit")
        user_input = input('Your choice: ').strip()

        if user_input.lower() == 'exit':
            print('Goodbye!')
            break

        if len(user_input.split()) != 1:
            print("Error: Only one word is allowed.")
            continue

        if user_input.lower() in anagram_instance.wordlist:
            print(f"{user_input} is an anagram!")
        else:
            print(f"{user_input} is not an anagram.")

# Assuming you have instantiated Anagrams somewhere
anagrams_instance = Anagrams('http://norvig.com/ngrams/sowpods.txt')

# Call the menu function with the instantiated Anagrams object
menu(anagrams_instance)

