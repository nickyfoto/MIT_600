import string

def getAvailableLetters(lettersGuessed):
	result = ''
	result_list = list(string.ascii_lowercase)
	for i in lettersGuessed:
		if i in result_list:
			result_list.remove(i)
	for item in result_list:
		result += item
	return result

def isWordGuessed(secretWord, lettersGuessed):
	b = []
	for i in secretWord:
		if i in lettersGuessed:
			b.append(True)
		else:
			b.append(False)
	if False in b:
		return False
	else:
		return True

def getGuessedWord(secretWord, lettersGuessed):
	result = ''
	# print result
	for i in range(0,len(secretWord)):
		if secretWord[i] in lettersGuessed:
			result += (secretWord[i]+'')
		else:
			result += '_'
	return result




lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print getAvailableLetters(lettersGuessed)
print 'abcdfghjlmnoqtuvwxyz'
