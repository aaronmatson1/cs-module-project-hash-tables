import random
import os.path

#gets the file path relative to the current script
input_txt = os.path.join(os.path.dirname(__file__), 'input.txt')

# Read in all the words in one go
with open(input_txt) as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
nextWordDict = {}
wordList = words.split()

for (i, word) in enumerate(wordList[:-1]):
    if word in nextWordDict:
        nextWordDict[word].append(wordList[i + 1])
    else:
        nextWordDict[word] = [wordList[i + 1]]


# TODO: construct 5 random sentences
# Your code here
def beginsWithStartWord(s):
    firstLetter = s[1] if (s[0] =='\"' and len(s) > 1) else s[0]
    return firstLetter.isupper()

def endsWithStopWord(s):
    lastLetter = s[-2] if (s[-1] == '\"' and len(s) > 1) else s[-1]
    return lastLetter in [".","!","?"]

def printRandomSentences(numberOfSentences):
    print("/n")
    for _ in range(numberOfSentences):

        #Gets a random 'start word'
        word = random.choice(wordList)
        while not beginsWithStartWord(word):
            word = random.choice(wordList)
        sentence = word

        #Adds random words until a 'stop word' is found
        word = random.choice(nextWordDict[word])
        sentence += " " + word
        while not endsWithStopWord(word):
            word = random.choice(nextWordDict[word])
            sentence += " " + word

        #This makes sure that any quotation marks are paired up
        if sentence.count('\"') % 2 != 0:
            if sentence[-1] == '\"':
                sentence = sentence[:-1]
            else:
                sentence += '\"'            

        print(f"{sentence}\n")

printRandomSentences(5)