#!/usr/bin/python
# Check if Palindrome-Checks if the string entered by the user is a palindrome.
# That is that it reads the same forwards as backwards like racecar

# Uses reverse_string module previously created.

from reverse_string import reverse_string


def check_palindrome(astring):
    q = astring.translate(None, ' ')  # removes spaces
    if q.lower() == reverse_string(q.lower()):  # makes sure that case matches
        return True


def main():
    while True:
        a = check_palindrome(raw_input("Enter String:\n"))
        if a:
            print "Palindrome!"
        else:
            print "NOT!"

if __name__ == '__main__':
    main()
