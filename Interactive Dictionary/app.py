import json
import difflib
from difflib import get_close_matches as gcm

data = json.load(open("data.json", "r"))

def translate(word):
	
	if word in data:
		return data[word]
	else:
		keys = data.keys()
		suggestion = gcm(word, keys, 1, 0.8) # 1 means to return the top 1 result. however it is still of type list. 0.8 is the minimum ratio
		
		if len(suggestion) > 0:
			choice = input("Do you mean " + suggestion[0] + " (Y/N): ").casefold()
		
			if choice == "y":
				return data[suggestion[0]]
			elif choice != "n":
				return "We do not understand your input"
			
	return "No such word exist"
	
word = input("Enter word to search for: ")
output = translate(word.casefold())

if type(output) == str:
	print(output)
else:
	for item in output:
		print(item)