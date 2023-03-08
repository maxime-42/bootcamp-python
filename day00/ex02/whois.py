import sys

assert len(sys.argv) == 2, "AssertionError: more than one argument are provided"
assert sys.argv[1].isnumeric(), "AssertionError: argument is not an integer"

nb:int = int(sys.argv[1])
if nb == 0:
	print("I'm Zero.")
elif  (nb % 2) == 0:
	print("I'm Even.")
else:
	print("I'm Odd..")
	
