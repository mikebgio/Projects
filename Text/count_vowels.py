#!/usr/bin/python
# Count Vowels - Enter a string and the program counts the number of vowels in the text. 
# For added complexity have it report a sum of each vowel found.

vowels = ['a','e','i','o','u']

def count_vowels(astring): 
	x=astring
	total=0
	for v in vowels:
		count=x.count(v)
		total+=count
		if count == 1: 
			noun = 'time' 
		else: noun = 'times'
		print "'%s' shows up %d %s" % (v, x.count(v), noun)
	return total


def main():
	while True:
		counted = count_vowels(raw_input('> '))
		print counted

if __name__ == '__main__':main()
