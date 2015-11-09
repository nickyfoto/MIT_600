import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

WORDLIST_FILENAME = "words.txt"
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
total = 0
# last = {}


def loadWords():
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList
def displayHand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print
    return #letter
        

def getWordScore(word, n):
    result = 0
    for i in word:
        result += SCRABBLE_LETTER_VALUES[i]
    if len(word) != n:
        return result*len(word)
    else:
        return result*len(word)+50

def updateHand(hand, word):
    hand_c = hand.copy()
    for i in word:
        for key in hand_c:
            if i == key:
                hand_c[key] -= 1
    return hand_c

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

def calculateHandlen(hand):
    length = 0
    for key in hand:
        length += hand[key]
    return length

def playHand(hand, wordList, n):
    global total
    print "current hand: ",
    displayHand(hand)
    word = raw_input('Enter word, or a "." to indicate that you are finished: ')
    if word == '.':
        print "Goodbye! Total score: %d points." % total
        total = 0
        print
    else:
        if isValidWord(word, hand, wordList): 
            score = getWordScore(word, n)
            total += score
            print "%s earned %d points. Total: %d points" % (word, score, total)
            print 
            # print hand
            # print updateHand(hand, word)
            hand = updateHand(hand, word)
            if calculateHandlen(hand) == 0:
                print "Run out of letters. Total score: %d points." % total
                total = 0
            else:
                playHand(hand, wordList, n)
        else:
            print "Invalid word, please try again."
            print
            playHand(hand, wordList, n)

def dealHand(n):
    hand={}
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

def playGame(wordList):
    last = {}
    def prompt(last):
        result = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if result == 'r':
            if len(last) == 0:
                print "You have not played a hand yet. Please play a new hand first!"
                print
                prompt(last)
            else:
                playHand(last, wordList, HAND_SIZE)
                prompt(last)
        elif result == 'n':
            last = dealHand(HAND_SIZE)
            playHand(last, wordList, HAND_SIZE)
            prompt(last)
        elif result == 'e':
            pass
        else:
            print "Invalid command."
            print
            prompt(last)
    prompt(last)

wordList = loadWords()
# playHand({'a': 1, 'z': 1}, wordList, 2)
playGame(wordList)
