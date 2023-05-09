import sys
def check_params(coefs, words) -> bool:
    if not all([isinstance(obj, list) for obj in [coefs, words]]):
        return False
    if len(coefs) != len(words):
        return False
    if not all([isinstance(obj, str) for obj in words]):
        return False
    if not all([isinstance(obj, (int, float)) for obj in coefs]):
        return False
    return True

class Evaluator:
    def __init__(self) -> None:
        pass

    @staticmethod
    def zip_evaluate(coefs:list, words:list):
        try :
           if check_params(coefs, words) is False:
               raise ValueError("Value Error: value can be only list")
        except ValueError as error_msg:
            print(error_msg, file=sys.stderr)
            return -1
        else:
            combine = zip(coefs, words)
            return sum(x[0] * len(x[1]) for x in combine )
    
    @staticmethod
    def enumerate_evaluate(coefs:list, words:list):
        try :
            if check_params(coefs, words) is False:
               raise ValueError("Value Error: value can be only list")
        except ValueError as error_msg:
            print(error_msg, file=sys.stderr)
            return -1
        else:
            return sum(coefs[i] * len(word) for i, word in enumerate(words))