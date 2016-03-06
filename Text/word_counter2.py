#!/usr/bin/python
"""
Count Words in a String - Counts the number of individual words 
in a string. For added complexity read these strings 
in from a text file and generate a summary.
"""
import sys
#Currently has an issue where it's adding empty strings to the split list
#Has something to do with instances of '\n\n'
#look into dividing separate words in a better way

def main(argv):
	words = split_words(argv)
	print "There are %d words in '%s'" %(len(words), argv)
	print "There are %d unique words in '%s'" %(len(set(words)), argv)

def split_words(file):
	with open(file, 'r') as f:
		read_data = f.read()
		lowcase = read_data.lower()
		stripped = lowcase.translate(None, ',;."!?[]()')
		dehyphen = stripped.replace('-',' ')
		words = dehyphen.split()
		return words


if __name__ == '__main__':main(sys.argv[1])