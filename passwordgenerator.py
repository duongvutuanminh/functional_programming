# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 16:50:18 2020

@author: Duong Vu Tuan Minh
@content: Hangman Game
"""

#making a password generator

import string
import random

all_the_letter = list(string.ascii_letters)
nums = list(string.digits)
punctuation = list(string.punctuation)

include_special = all_the_letter + nums + punctuation
not_include_special = all_the_letter + nums

print("How long do you want your password to be?")
player_input = input()
  
special_wanted = input("Do you want your password to have special characters? Y/N")
res = ""
if special_wanted.lower() == "y":
    for i in range(1,int(player_input)+1):
        res += random.choice(include_special)
else:
    for i in range(1,int(player_input)+1):
        res += random.choice(not_include_special)
print(res)