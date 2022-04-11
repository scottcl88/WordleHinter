from typing import final
from logic import Logic


def is_empty(string):
    return not string.strip()


class User:
    known_word = ""
    known_correct_letters = ""
    known_wrong_letters = ""
    logic: Logic

    def __init__(self, logic):
        self.master = self
        self.logic = logic

    def get_letters(self):
        count: int = 0
        while count != 5:
            print("Enter the 5 letters you know with the correct place, otherwise add '*' in that place:")
            self.known_word = input().lower()        
            self.known_word = self.known_word.replace("*", ".")
            count = len(self.known_word)
            if count != 5:
                print("You must enter 5 characters")

    def get_known_letters(self):
        print("Enter any other letters that you know ARE in the word but in the wrong place:")
        self.known_correct_letters = input().lower()
        print("Enter any letters that you know are NOT in the word:")
        self.known_wrong_letters = input().lower()

    def get_more_help(self):
        print("Need more help? Show synonyms of correct word only?")
        more_help = input("1 for yes, anything else for no: ")
        if more_help == "1":
            exact_word = self.logic.get_exact_word()
            self.logic.synonyms = []
            new_synonyms = self.logic.get_synonyms(exact_word)
            print("\n\nPossible synonyms are: ", new_synonyms)

    def get_exact_word(self):
        print("Give up? Want to know the answer?")
        find_exact_word = input("1 for yes, anything else for no: ")
        if find_exact_word == "1":
            exact_word = self.logic.get_exact_word()
            print("\nAnswer is: ", exact_word)

def main():
    logic = Logic()
    logic.load()
    print("\n")
    user = User(logic)
    user.get_letters()
    user.get_known_letters()
    print("\nChecking...\n\n")
    logic.check(user.known_word, user.known_correct_letters, user.known_wrong_letters)
    print("\n")
    user.get_more_help()
    print("\n")
    user.get_exact_word()


if __name__ == "__main__":
    main()
