#!/usr/bin/python
# Pig Latin is a game of alterations played on the English language game.

vowels = ('a','e','i','o','u')
pig = ['yay','ay']

def vowel_hunt(word):
	vow_places = [word.find(v) for v in vowels]
	vow_place = [x for x in vow_places if x != -1]
	return min(vow_place)

def piggy(word):
	s = vowel_hunt(word)
	if s > 0:
		suff = 1
	else: suff = 0
	return word[s::] + word[0:s] + pig[suff]

def main():
	while True:
		print piggy(raw_input("--> "))

if __name__ == "__main__": main()
