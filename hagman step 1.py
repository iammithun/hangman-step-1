# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 16:36:00 2024

@author: iamrs
"""

#Step 1 

word_list = ["preethi", "saravanan", "mithun", "omkar"]

import random
chosen_word = random.choice(word_list)

guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

        
        
        