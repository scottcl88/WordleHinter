import json
import http.client
import random
import re
import datetime


class Logic:
    word_list = []
    possible_words = []
    synonyms = []

    def __init__(self):
        self.master = self

    def get_synonyms(self, word):
        api_key = open("api_key.txt", 'r').read()
        conn = http.client.HTTPSConnection("wordsapiv1.p.rapidapi.com")
        headers = {
            'X-RapidAPI-Host': "wordsapiv1.p.rapidapi.com",
            'X-RapidAPI-Key': api_key
        }
        conn.request("GET", "/words/" + word + "/synonyms", headers=headers)
        res = conn.getresponse()
        data = res.read()
        # print(data.decode("utf-8"))#prints results
        json_object = json.loads(data)
        all_syn = json_object["synonyms"]
        visible_syn = []
        for w in all_syn:
            if not re.search(word, w):
                visible_syn.append(w)
        if len(visible_syn) > 0:
            return random.sample(visible_syn, 2 if len(visible_syn) >= 2 else 1)
        else:
            return visible_syn

    def load(self):
        print("Loading...")
        self.word_list = open("words.txt", 'r').read().split("\n")
        print("Loaded.")

    def get_exact_word(self):
        today = datetime.date.today()
        firstday = datetime.date(2021, 6, 19)  # first day of wordle
        diff = today - firstday
        return self.word_list[diff.days]
    
    def do_letters_exist(self, letters_to_check: str, letters_in_str: str):
        if letters_to_check == "" or letters_in_str == "":
            return False
        else:
            return re.search("([" + letters_to_check + "])+", letters_in_str)

    def check(self, guess: str, known_correct_letters: str, known_wrong_letters: str):
        r = re.compile(guess)
        cur_possible_words = list(filter(r.match, self.word_list))
        new_possible_words: list[str] = []
        for w in cur_possible_words:
            if (known_correct_letters == "" or re.search("([" + known_correct_letters + "])+", w)) and (known_wrong_letters == "" or not re.search("([" + known_wrong_letters + "])+", w)):
                new_possible_words.append(w)
        self.possible_words = new_possible_words
        print("Possible words remaining: ", len(self.possible_words))
        if len(self.possible_words) <= 5:
            unknown_syn: int = 0
            for w in self.possible_words:
                result = self.get_synonyms(w)
                if len(result) > 0:
                    self.synonyms += result
                else:
                    unknown_syn += 1
            print("Words without synonyms found: ", unknown_syn)
            print("Possible synonyms are: ", self.synonyms)
        else:
            print("Need to narrow it down further to get help")
