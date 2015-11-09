from ps4a import *
import time
# last = {}

#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    max_score = 0
    # Create a new variable to store the best word seen so far (initially None)  
    best_word = None
    # For each word in the wordList
    for eachWord in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(eachWord, hand, wordList):
            # Find out how much making that word is worth
            score = getWordScore(eachWord, n)
            # If the score for that word is higher than your best score
            if score > max_score:
                # Update your best score, and best word accordingly
                max_score = score
                best_word = eachWord

    # return the best word you found.
    return best_word


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function
    global total
    if calculateHandlen(hand) > 0:
        print "current hand:",
        displayHand(hand)
        word = compChooseWord(hand, wordList, n)
        if word == None:
            print "Total score: %d points." % total
            print
        else:
            total = total+int(getWordScore(word, n))
            print '"%s" earned %d points. Total: %d points' % (word, int(getWordScore(word, n)), total)
            print
            compPlayHand(updateHand(hand, word), wordList, n)
    else:
        print "Total score: %d points." % total
        print
        total = 0
#       
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    # print "playGame not yet implemented." # <-- Remove this when you code this function
    last = {}
    def prompt(last):
        cmd = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        print
        if cmd == 'r':
            if len(last) == 0:
                print "You have not played a hand yet. Please play a new hand first!"
                prompt(last) #called 'raw_input' more times than necessary
            else:
                repeat(last)
        elif cmd == 'n':
            last = dealHand(HAND_SIZE)
            new(last)
        elif cmd == 'e':
            pass
        else:
            print "Invalid command."
            prompt(last) #Your code called 'dealHand' more times than necessary.
    
    def new(last):
        choice = raw_input("Enter u to have yourself play, c to have the computer play: ")
        # print
        if choice == 'u':
            playHand(last, wordList, HAND_SIZE)
            prompt(last)
        elif choice == 'c':
            compPlayHand(last, wordList, HAND_SIZE)
            prompt(last)
        else:
            print "Invalid command."
            print
            new(last)
    
    def repeat(last):
        choice = raw_input("Enter u to have yourself play, c to have the computer play: ")
        # print
        if choice == 'u':
            playHand(last, wordList, HAND_SIZE)
            prompt(last)
        elif choice == 'c':
            compPlayHand(last, wordList, HAND_SIZE)
            prompt(last)
        else:
            print "Invalid command."
            print
            repeat(last)

    prompt(last)
    
    
        
#
# Build data structures used for entire session and play game
#

if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
    # compPlayHand({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)
    # compPlayHand({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5)
    # compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)
    # compChooseWord({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)
    # compChooseWord({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5)
    # compChooseWord({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)
    # compChooseWord({'x': 2, 'z': 2, 'q': 2, 'n': 2, 't': 2}, wordList, 12)

