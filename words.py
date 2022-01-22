
# import readline
import string
import random

WORDLIST_FILENAME = "words.txt"
def load_words():
    # """
    # Ye function kaafi jayada words ko load karne mai help karega
    # """
    # word_list = ["navgurukul", "learning", "kindness","loose","happiness","wishes","cooking",
    # "empathy","movie","celebration","craziness","powerful","amazing"]
    # return word_list
    print("loading word list from file.....")
    infile =  open(WORDLIST_FILENAME,"r")
    line = infile.readline()
    word_list = line.split()
    print(" ",len(word_list),"words loaded.\n\n")
    return word_list



def choose_word():
    """
    word_list (list): list of words (strings)
    ye function ek word randomly return karega
    """
    return random.choice(word_list)
word_list = load_words()