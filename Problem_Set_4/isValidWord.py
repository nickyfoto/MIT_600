WORDLIST_FILENAME = "words.txt"

def loadWords():
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    return wordList

def getFrequencyDict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def isValidWord(word, hand, wordList):
    word_dict = getFrequencyDict(word)
    valid = []
    if word not in wordList:
        return False
    else:
        for key in word_dict:
            if key in hand.keys():
                if word_dict[key] <= hand[key]:
                    valid.append(True)
                else:
                    valid.append(False)
            else:
                valid.append(False)
        if all(valid) == True:
            return True
        else:
            return False


hand = {'b': 1, 'i': 2, 'k': 1, 'j': 1, 'o': 1, 'w': 1}
word = "kwijibo"
wordList = loadWords()
print getFrequencyDict(word)
print hand
# print getFrequencyDict(word)['r']
# print hand['r']
print isValidWord(word, hand, wordList)
print word in wordList
