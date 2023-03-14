""" 
    make a program which remove all punction into give string
    make a list of this str where each word len is bigger than argv[2]
"""
import sys 
import  string 

try:
    assert len(sys.argv) == 3 , "Allow only two argument"
    str(sys.argv[1])
    assert int(sys.argv[2]) , "Second must be a integer"
except :
    print("ERROR")
else:
    txt =  "".join(x  for x in sys.argv[1] if x not in  string.punctuation)
    word_list = [x for x in txt.split(" ") if len(x) > int(sys.argv[2]) ]
    print(word_list)