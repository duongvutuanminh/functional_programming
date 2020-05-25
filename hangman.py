# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 16:50:19 2020

@author: Duong Vu Tuan Minh
@content: Hangman Game
"""
import urllib.request
import json

# url = "https://xkubist-random-word-v1.p.rapidapi.com/run.cgi"

# headers = {
#     'x-rapidapi-host': "xkubist-random-word-v1.p.rapidapi.com",
#     'x-rapidapi-key': "dde5fd022bmshf1fbb10fef3cdeep12adc6jsn0d8bff707d68",
#     'authorization': "Basic ZHVvbmd2dXR1YW5taW5oMjgxMTptaW5oamsyODEx",
#     'probability_selection': "50",
#     'length_selection': "10",
#     'word_selection': "1",
#     'language_selection': "English"
#     }

# response = requests.request("GET", url, headers=headers)

# print(response.text)
#Just to try an API that generate random word


url = "http://random-word-api.herokuapp.com/word?number=1"
response = urllib.request.urlopen(url)
data = json.load(response)

#creating a Hangman Game

import random
#from colorama import Fore #pretty a good way to specialize the word


easy = ["dog","cake","bear"]
average = ["bangcok","creating","module"]
hard = ["stich","microusb","curtains","philanthropism"]
hardest = data #this feature require connection to the Internet

print("Welcome to the hangman game!")
print("Choose your level:\n 1.Easy\n 2.Average\n 3.Hard\n 4.Legendary") 
level = input()
word = ""

if level == "1":
    word += random.choice(easy)
elif level == "2":
    word += random.choice(average)
elif level == "3":
    word += random.choice(hard)
else:
    word += random.choice(hardest)
word_length = len(word)
bracket = ["_"]*len(word)
print(f"Your guessing word has {word_length} characters and you have 6 tries")
print(" ".join(bracket))
game_on = True
times_of_try = 0
while "_" in bracket and game_on:
    print("Guessing a letter!")
    player_input = input()
    if player_input in word:
        #itemindpos = 0  
        # for character in list(word):
        #     if player_input == character:
        #         bracket[word.index(character, itemindpos)] = player_input
        #         itemindpos += 1

        # This way 
        print("Good guess!")

        #bracket[word.index(player_input)] = player_input

        #THIS way is now working because using index() will only return the first value
        for i in range(len(word)):
            if word[i] == player_input:
                bracket[i] = player_input
        print(" ".join(bracket))
        if "".join(bracket) == word:
            print("You won! Endgame")
            game_on = False
    else:
        times_of_try += 1 
        print(f"You will have {6-times_of_try} tries left")
        if times_of_try == 6:
            print("Out of tries\n\n")
            print(f"The word is : {word}")
            game_on = False
    