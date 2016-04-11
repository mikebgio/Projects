#!/usr/bin/python
'''
**Number Names** - Show how to spell out a number in English.
You can use a preexisting implementation or roll your own,
but you should support inputs up to at least one million
(or the maximum value of your languages default bounded integer
type, if thats less). *Optional: Support for inputs other than positive
integers (like zero, negative integers, and floating-point numbers).*
'''
# This is currently under construction

prim = dict(zero=0, one=1, two=2, three=3, four=4, five=5, six=6, seven=7, eight=8,
            nine=9, ten=10, eleven=11, twelve=12, thirteen=13, fourteen=14, fifteen=15,
            sixteen=16, seventeen=17, eighteen=18, nineteen=19, twenty=20, thirty=30,
            forty=40, fifty=50, sixty=60, seventy=70, eighty=80, ninety=90, hundred=100,
            thousand=1000, million=10000
            )


def main(indo):
	print num_to_name(indo)


def num_to_name(number):
    pass

if __name__ == '__main__':
    main(raw_input("--> "))
