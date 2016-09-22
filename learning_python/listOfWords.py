import os
import re

def generateWordList():

    word_list = []

    for filename in os.listdir(os.getcwd()):

        open_file = open(filename)

        for line in open_file:
            for word in line.split():
                clean_word =  re.sub(r'[\W_]+', '', word.lower())
                if clean_word not in word_list:
                    word_list.append(clean_word)

        open_file.close()
    return word_list


l = generateWordList()
sl = sorted(l)
for s in sl:
    print s
