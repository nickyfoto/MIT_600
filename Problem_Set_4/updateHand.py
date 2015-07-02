# hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
# hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
hand = {'h': 1, 'e': 1, 'l': 2, 'o': 1}

def updateHand(hand, word):
	hand_c = hand.copy()
    for i in word:
        for key in hand_c:
            if i == key:
                hand_c[key] -= 1
    return hand_c

print updateHand(hand, 'hello')
print hand