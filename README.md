# WordleHinter

A simple python script intended to give you a hint for the [Wordle](https://www.nytimes.com/games/wordle/index.html) game.

A command line tool where you enter the information you know in Wordle. Then it finds all the possible words remaining from the Wordle list of words, and gives you 2 random synonyms of those remaining words. Assumes you narrowed it down to 5 remaining words, and the API has synonyms available. If you need more help, you can get synonyms for just the right word. Or if you give up, you can find the answer too.

### SPOILER WARNING ###
The `alpabetical_words.txt` are the Wordle words alphabetized. The `words.txt` are the Wordle words in order. The `main.js` is the source code of Wordle.

# Run Executable
Download `main.exe` from `./dist/main`
You will need to add a new file called `api_key.txt` in the same folder of the executable. The txt file should contain the API Key from RapidAPI, and nothing else.
You will also need to make sure the `words.txt` file is in the same folder of the executable.

# Run Python
You will need to add a new file called `api_key.txt` in the same folder of `main.py`. The txt file should contain the API Key from RapidAPI, and nothing else.
In command line, run: `python main.py`

# Building
To build exe run: `pyinstaller main.py --add-data "words.txt;."`
Note: This excludes the API key, that will need to be added manually to run executable.

# Technology
- Python v3.9.6
- [WordsAPI via RapidAPI](https://rapidapi.com/dpventures/api/wordsapi/)
