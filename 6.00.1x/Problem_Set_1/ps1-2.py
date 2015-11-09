'''
COUNTING BOBS  (15/15 points)
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
 For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2
'''
s = 'azcbobobegghakl'

def counting_Bobs(s):
	i = 0
	count = 0
	for i in range(0,len(s)):
		if s[i:(i+3)] == 'bob':
			count += 1
	print 'Number of times bob occurs is: %s' % count
	
counting_Bobs(s)