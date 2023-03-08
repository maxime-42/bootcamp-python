#!/usr/bin/python3
"""take input argument 
	reove the progrmq name reverse
 	If no argument are provided, do nothing
	If more than one argument are provided, merge them 
    into a single string with each argument separated by a space character.
    by reverse oreder of argument and alphabe upcase to lowercase vice versa
    exemple : 
		input     == ['Hello', 'my Friend']
		first rev  == ['my Friend', 'Hello']
		second rev == 'hELLO MY fRIEND'
		third      == 'DNEIRf YM OLLEh'
"""

import sys


if len(sys.argv) < 2:
    exit(0)
sys.argv.pop(0)
sys.argv.reverse()
result = ' '.join(sys.argv[::-1]).swapcase()
print(f"{result[::-1]}")
