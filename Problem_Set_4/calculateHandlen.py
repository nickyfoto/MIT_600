def calculateHandlen(hand):
    length = 0
    for key in hand:
        length += hand[key]
    return length