'''
COUNTING VOWELS
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
'''
# s = 'azcbobobegghakl'
s = 'pethrworig'


def counting_Vowels(s):
	count = 0
	for i in s:
		if i in 'aeiou':
			count += 1
	print 'Number of vowels: %s' % count

counting_Vowels(s)