#!/usr/bin/python
# THIS ONE IS OLD AND LAME
"""
Count Words in a String - Counts the number of individual words
in a string. For added complexity read these strings
in from a text file and generate a summary.
"""

# Currently has an issue where it's adding empty strings to the split list
# Has something to do with instances of '\n\n'
# look into dividing separate words in a better way


def main():
    indo = raw_input("Enter file path: ")
    c = count_words(indo)
    print "There are %d words in '%s'" % (c, indo)


def count_words(file):
    with open(file, 'r') as f:
        read_data = f.read()
        stripped = read_data.replace('-', ' ')
        words = stripped.split()
        print words
        return len(words)

if __name__ == '__main__':
    main()
