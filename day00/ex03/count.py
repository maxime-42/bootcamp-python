import sys
import string 

assert len(sys.argv) == 1, "Not argument needed"

def	text_analyzer(txt:str):
	""""""
	counter = {"uppcase":0, "lowercase": 0, "ponctuation":0, "space": 0}
	for x in txt:
		if x.isupper():
			counter['uppcase'] += 1
		elif x.islower():
			counter['lowercase'] += 1
		elif  x in string.punctuation:
			counter['ponctuation'] += 1
		elif x.isspace():
			counter['space'] += 1

	print(f"- {counter['uppcase']} letter(s)")
	print(f"- {counter['lowercase']} letter(s)")
	print(f"- {counter['ponctuation']} mark(s)")
	print(f"- {counter['space']} makr(s)")

