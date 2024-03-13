import requests
import string

class Text:
    def __init__(self, text):
        self.text = text.lower()  # Convert text to lowercase

    def create_word_frequency_dict(self):
        words = self.text.split()
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        return word_count

    def word_frequency(self, word):
        word_count = self.create_word_frequency_dict()
        frequency = word_count.get(word.lower(), 0)  # Convert word to lowercase
        if frequency == 0:
            return f"The word '{word}' does not appear in the text."
        else:
            return f"The word '{word}' appears {frequency} times in the text."

    def most_common_word(self):
        word_count = self.create_word_frequency_dict()
        max_frequency = max(word_count.values())
        most_common_words = [word for word, freq in word_count.items() if freq == max_frequency]
        return most_common_words

    def unique_words(self):
        word_count = self.create_word_frequency_dict()
        unique_words = [word for word, freq in word_count.items() if freq == 1]
        return unique_words

    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as file:
            text = file.read()
        return cls(text)

# Download the text file from the URL
url = 'https://raw.githubusercontent.com/devtlv/theStranger_text_W5D4PY/main/the_stranger.txt'
response = requests.get(url)
if response.status_code == 200:
    with open("the_stranger.txt", "w") as file:
        file.write(response.text)
    print("File downloaded successfully.")
else:
    print("Failed to download the file. Status code:", response.status_code)

# Example usage:
text_instance = Text.from_file('the_stranger.txt')

# Use methods of the Text instance
print(text_instance.word_frequency("stranger"))
print("Most common word(s):", text_instance.most_common_word())
print("Unique words:", text_instance.unique_words())

class TextModification(Text):
    def __init__(self, text):
        super().__init__(text)

    def remove_punctuation(self):
        translator = str.maketrans('', '', string.punctuation)
        text_without_punctuation = self.text.translate(translator)
        return text_without_punctuation

    def remove_special_characters(self):
        # Define a translation table to remove special characters
        special_chars = string.punctuation + string.whitespace
        translator = str.maketrans('', '', special_chars)
        # Remove special characters using translate method
        text_without_special_chars = self.text.translate(translator)
        return text_without_special_chars

# Instantiate TextModification class
text_mod_instance = TextModification(text_instance.text)

# Use the remove_punctuation method
text_without_punctuation = text_mod_instance.remove_punctuation()
print("Text without punctuation:", text_without_punctuation)

# Use the remove_special_characters method
text_without_special_chars = text_mod_instance.remove_special_characters()
print("Text without special characters:", text_without_special_chars)