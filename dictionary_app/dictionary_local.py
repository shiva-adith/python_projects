import os
import json
from difflib import get_close_matches

if os.path.exists("dictionary.json"):
	dictionary = json.load(open("dictionary.json", "r"))

# a function that returns the meaning of a word :
	def meaning(word):
		if word in dictionary:
			return (dictionary[word])
		elif word.title() in dictionary:
			return dictionary[word.title()]
		elif word.upper() in dictionary:
			return (dictionary[word.upper()])
		elif matches(word) == True:
			return (dictionary[get_close_matches(word,dictionary.keys())[0]])
		else:
			return "Word does not exist! Enter again"


	def matches(word):
			if len(get_close_matches(word, dictionary.keys())) > 0:
				if input("\nDid you mean {}. If yes press y else press n? ".format(get_close_matches(word, dictionary.keys())[0])) == "y":
					return True
			else:
				return False


# Main body of the code :

	while True:
		word = input("\nEnter a word: ")
		if not word == "/end":
			print(meaning(word.lower()))
		else:
			break
else:
	print("No such file exists!")
