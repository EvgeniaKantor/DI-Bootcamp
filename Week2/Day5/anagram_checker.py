import requests

class AnagramChecker:
    # import the requests module, which is used for making HTTP requests
    def __init__(self, url):
        self.wordlist_file = "wordlist_file.txt"
        self.create_wordlist_file(url)
        self.wordlist = self.load_wordlist(self.wordlist_file)

    # Downloads the word list from the provided URL and saves it to a file.
    def create_wordlist_file(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            with open(self.wordlist_file, "w") as file:
                file.write(response.text)
            return True
        else:
            return False

    # Loads words from the word list file into memory as a set
    def load_wordlist(self, wordlist_file):
        with open(wordlist_file, 'r') as file:
            wordlist = set(word.strip().lower() for word in file)
        return wordlist

    # Checks if a given word is a valid word in the loaded word list
    def is_valid_word(self, given_word):
        return given_word.lower() in self.wordlist

    # Checks if two given words are anagrams of each other
    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    # Finds all anagrams of a given word from the loaded word list
    def get_anagrams(self, word):
        return [w for w in self.wordlist if self.is_anagram(word, w) and word.lower() != w]

url = 'http://norvig.com/ngrams/sowpods.txt'
anagram_checker = AnagramChecker(url)

# Example usage
given_word = input('Enter a word: ')
while not anagram_checker.is_valid_word(given_word):
    given_word = input('Enter another word: ')

anagrams = anagram_checker.get_anagrams(given_word)
print(f"Anagrams of '{given_word}': {anagrams}")
