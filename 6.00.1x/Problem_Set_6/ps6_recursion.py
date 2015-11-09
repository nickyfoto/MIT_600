# 6.00x Problem Set 6
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    ### TODO.
    if len(aStr) == 2:
        return aStr[-1] + aStr[0]
    else:
        return aStr[-1] + reverseString(aStr[0:len(aStr)-1])
    # return aStr[::-1]

# print reverseString('1234')
#
# Problem 4: X-ian
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    ###TODO.
    if len(x) == 2:
        if word.index(x[0]) < word.index(x[1]):
            return True
        else:
            return False
    else:
        return x_ian(x[:2], word) and x_ian(x[1:], word)

        
# print x_ian('eric', 'meritocracy')
# print x_ian('eric', 'cerium')
# print x_ian('john', 'mahjong')
#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    ### TODO.
    if len(text) < 70:
        return text
    else:
        p = text[lineLength:].index(' ')
        # return p
        return text[:lineLength] + text[lineLength:][p].replace(' ','\n') + insertNewlines(text[lineLength+p+1:], lineLength)
            
            # return text[:lineLength] + text[lineLength:][p].replace(' ','\n') + insertNewlines(text[lineLength+1:], lineLength)
        # p = text[lineLength:].index(' ')
        # return (text[:lineLength] + (text[lineLength + p]).replace(' ','\n') + insertNewlines(text[(lineLength):], lineLength))

text = "Nonsense words: sight dead wooden feed current almost salt nature gate tear employee expect program membership governor ground connect in pad stripe crowd frighten year headdress passenger quantity elastic march encourage deafen moon bleed net tailor international"
lineLength = 70

print insertNewlines(text, lineLength)

