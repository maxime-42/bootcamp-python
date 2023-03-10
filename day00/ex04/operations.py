import sys 


def div_and_rest(a, b, type_operation):
	"""this function make division and modulo, check error"""
	result = 0 
	try:
		if type_operation == "Quotient" :
			result = a / b
		elif type_operation == "Remainder":
			result = a % b
	except ZeroDivisionError:
		print ("ERROR (%s by zero)", type_operation)
	else:
		return (f"{type_operation}: {result}")


"""check errro and print result"""

if len(sys.argv) > 3:
	print("AssertionError: too many arguments")
	exit(1)

try :
	if len(sys.argv) < 3:
		raise ValueError
	a = int(sys.argv[1])
	b = int(sys.argv[2])

except ValueError:
	print("Usage: python operations.py <number1> <number2>")

else :
	print("Sum: ", a + b)
	print("Difference: ", a - b)
	print("Product: ", a * b)
	print(div_and_rest(a, b, "Quotient"))
	print(div_and_rest(a, b, "Remainder"))