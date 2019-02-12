# Python3 Code for implementing
# dictionary
 
# importing json library
import json
 
# importing get_close_matches fuction from difflib library
from difflib import get_close_matches
 
# loading data
data = json.load(open("data.txt"))
 
# defining function meaning
def meaning(w):
 
    # converting all the letters of "w" to lower case
    w = w.lower()
 
    # checking if "w" is in data
    if w in data:
        return data[w]
 
    # if word is not in data then get close match of the word
    elif len(get_close_matches(w, data.keys())) > 0:
 
        # asking user for his feedback
        # get_close_matches returns a list of the best 
        # “good enough” matches choosing first close 
        # match "get_close_matches(w, data.keys())[0]"
        yn = input("Did you mean % s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
         
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist in our data."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist in our data."
 
# asking word from user to get the meaning
word = input("Enter word: ")
 
# storing return value in "output"
output = meaning(word)
 
# if output type is list then print all element of the list
if type(output) == list:
    for item in output:
        print(item)
 
# if output type is not "list" then print output only
else:
    print(output)
