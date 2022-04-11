import json
from tkinter import Tk, Label, Button
import http.client
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
        # print(data.decode("utf-8"))
        json_object = json.loads(data)    
        all_syn = json_object["typeOf"]
        return all_syn[:2]
    
    def load(self):
        print("Loading...")
        self.word_list = open("words.txt", 'r').read().split("\n")
        print("Loaded.")
        # print(self.word_list)

    def get_exact_word(self):
        today = datetime.date.today()
        firstday = datetime.date(2021, 6, 19)
        diff = today - firstday
        print(diff.days)
        exactword = self.word_list[diff.days]
        print("Exact word: "+exactword)

    def check(self, guess):
        # print("Checking guess: "+guess)
        r = re.compile(guess)
        self.possible_words = list(filter(r.match, self.word_list))
        # print(self.possible_words)
        # print("Checking done")
        for w in self.possible_words:    
            # print("Getting Synonyms for: "+w)
            self.synonyms += self.get_synonyms(w)
        