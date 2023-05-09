"""test"""
import random
import string
import sys


def generator(txt:str = "", sep=" ", option=None):
    """Splits the text according to sep value and yield the substrings.
    option precise if a action is performed to the substrings before it is yielded."""
    
    try:
        is_printable = all([ x in string.printable for x in txt])
        print(is_printable)
        if not is_printable:
            raise ValueError("text can be : only printable character")
        word = txt.split(sep)
        if option == "shuffle":
            random.shuffle(word)
        elif option == "unique":
            word = list(set(word))
        elif option == "ordered":
            word.sort()
        elif option is not None:
            raise ValueError("Option can be : 'shuffle', 'unique', 'ordered'")
    except ValueError as error_msg:
        print(error_msg, file=sys.stderr)

    else:
        for x in word:
            yield x

text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" ", option="ordered"):
    print(word)

