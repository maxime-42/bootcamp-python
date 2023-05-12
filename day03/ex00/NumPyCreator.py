import numpy as np

class NumPyCreator():
    def __init__(self):
        pass

    def from_list(self, lst):
        try:
            array = np.array(lst)
        except ValueError as error_msg:
            print(error_msg)
        else:
            return array
        return None 

    def from_tuple(self, tpl):
        return np.array(tpl)

    def from_iterable(self, itr):
        return np.array(itr)

    def from_shape(self, shape, value=0):
        return np.full(shape, value)

    def random(self, shape):
        return np.random.uniform(-1, 1, shape)

    def identity(self, n):
        return np.identity(n)


if __name__ == "__main__":
    npc = NumPyCreator()
    print(npc.from_list([[1, 2, 3], [6, 3, 4]]))
    # Output :
    # array([[1, 2, 3],
    # [6, 3, 4]])
    print("\n", npc.from_list([[1,2,3],[6,4]]))

    print("\n",npc.from_list([[1,2,3],['a','b','c'],[6,4,7]]))

    print("\n", npc.from_list(((1,2),(3,4))))

    print("\n", npc.from_tuple(("a", "b", "c")))