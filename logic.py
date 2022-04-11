import json
import http.client
from posixpath import split
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
        conn = http.client.HTTPSConnection("wordsapiv1.p.rapidapi.com")
        headers = {
            'X-RapidAPI-Host': "wordsapiv1.p.rapidapi.com",
            'X-RapidAPI-Key': "0fdf58d79cmshe4a721e7dc6a96fp18ce0cjsna339775e39bf"
        }
        conn.request("GET", "/words/"+word+"/typeOf", headers=headers)
        res = conn.getresponse()
        data = res.read()
        # print(data.decode("utf-8"))#prints results
        json_object = json.loads(data)
        all_syn = json_object["typeOf"]
        if len(all_syn) > 0:
            return random.sample(all_syn, 2 if len(all_syn) >= 2 else 1)
        else:
            return all_syn

    def load(self):
        print("Loading...")
        self.word_list = open("words.txt", 'r').read().split("\n")
        print("Loaded.")

    def get_exact_word(self):
        today = datetime.date.today()
        firstday = datetime.date(2021, 6, 19)  # first day of wordle
        diff = today - firstday
        return self.word_list[diff.days]

    def check(self, guess: str, known_correct_letters: str, known_wrong_letters: str):
        r = re.compile(guess)
        cur_possible_words = list(filter(r.match, self.word_list))
        new_possible_words: list[str] = []
        for w in cur_possible_words:
            if re.search("(["+known_correct_letters+"])+", w) and not re.search("(["+known_wrong_letters+"])+", w):
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
