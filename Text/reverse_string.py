#!/usr/bin/python
#Reverse a String - Enter a string and the program will reverse it 
#and print it out.

def reverse_string(user_input):
	a =''
	for i in reversed(user_input):
		a += i
	print a
	pass

def main():
	while True:
		indo = raw_input("What do you need reversed? \n -->")
		reverse_string(indo)

if __name__ == "__main__":main()