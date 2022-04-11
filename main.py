from typing import final
from logic import Logic

def is_empty(string):
    return not string.strip()

class User:
    known_word = ""
    known_letters = ""
    def __init__(self):
        self.master = self
    def get_letters(self):
        print("Enter the 5 letters you know with the correct place, otherwise add '*' in that place:")
        self.known_word = input()       
        self.known_word = self.known_word.replace("*",".*")
        print("Enter any letters that you know but are in the wrong place:")
        self.known_letters = input() 
        print(self.known_word)      
        print(self.known_letters)


def main():
    logic = Logic()
    logic.load()
    user = User()
    user.get_letters()
    print("Checking...")
    logic.check(user.known_word)
    print("Possible words remaining: ",len(logic.possible_words))
    print("Possible Synonyms are: ",logic.synonyms)

if __name__ == "__main__":
    main()