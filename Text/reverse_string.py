#!/usr/bin/python
# Reverse a String - Enter a string and the program will reverse it
# and print it out.


def reverse_string(user_input):
    return user_input[::-1]


def main():
    while True:
        indo = raw_input(
            "What do you need reversed? (Type exit to leave)\n -->")
        print reverse_string(indo)
        if indo in ('exit', 'EXIT', 'Exit'):
            return False

if __name__ == "__main__":
    main()
