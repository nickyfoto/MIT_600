'''
ALPHABETICAL SUBSTRINGS  (15/15 points)
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s 
in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. 
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
'''
# Official answer
curString = s[0]
longest = s[0]
for i in range(1, len(s)):
    if s[i] >= curString[-1]:
        curString += s[i]
        if len(curString) > len(longest):
            longest = curString
    else:
        curString = s[i]
print 'Longest substring in alphabetical order is:', longest

# s = 'zyxwvutsrqponmlkjihgfedcba'
# s = 'azcbobobegghakl'
# s = 'abcbcd'

# convert string into a list of all possible strings
collection = []
for i in range(len(s)):
	x = i
	while i < len(s):
		collection.append(s[x:(i+1)])
		i += 1

# print len(collection)
# print collection

def alphabeticalOrderCheck(s):
	'''
	check if a string is in alphabetical order
	'''
	proof = []
	for i in range(len(s)-1):
		if s[i] <= s[i+1]:
			proof.append(True)
		else:
			proof.append(False)
	if False in proof:
		return False
	else:
		return True

availables = []
# store good results in a new list
for ans in collection:
	if alphabeticalOrderCheck(ans) == True:
		availables.append(ans)

# find the longest/first substring in the good result list
print max(availables, key=len)