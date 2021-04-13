import json
#import datetime
from difflib import get_close_matches

#start = datetime.datetime.now()

dictionary = json.load(open("data.json"))

def translate(word):

    if word in dictionary:
        return dictionary[word]

    #Get closest match using difflib
    elif len(get_close_matches(word, dictionary.keys())) > 0:

        corrected_word = get_close_matches(word,dictionary.keys())[0]
        
        user_response = input("Did you mean %s instead? Enter Y(Yes) or N(No) : " % corrected_word)

        if user_response == "Y" or user_response == "y":
            #finish = datetime.datetime.now()
            #print finish-start

            return dictionary[corrected_word]
        else:
            return "Sorry try again!"
    else:
        print("That word doesn't exist. Try again!")


word = (input("Enter Word: ")).lower()

print(translate(word))

