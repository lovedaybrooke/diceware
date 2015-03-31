import os
import string
import random

from wordlist import wordlist as word_dict

def randomDiceRoll():
    random_generator = random.SystemRandom()
    random_list = [str(random_generator.randint(1,6)) for i in range(0,5)]
    return string.join(random_list,"")

def makePassphrase():
    return [
        word_dict[randomDiceRoll()] + " " +
        word_dict[randomDiceRoll()] + " " +
        word_dict[randomDiceRoll()] + " " +
        word_dict[randomDiceRoll()] + " " +
        word_dict[randomDiceRoll()] + " " +
        word_dict[randomDiceRoll()]
        ][0]