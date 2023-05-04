import sys
import copy

IS_SIZE= 1
IS_RANGE= 2
IS_COLUMN_VECTOR = 3

def is_range(values):
    try:
        if values[0] > values[1]:
             raise TypeError("error index 0 must be smaller than index 1, ex: (a < b)")
    except TypeError as error_msg:
        print(error_msg, file=sys.stdout)
        exit(1)
    else:
        value = [[float(i)] for i in range(values[0], values[1])]
        shape = (len(values), 1)
        return value, shape, IS_RANGE


def is_column_vector(column):
    value =  copy.deepcopy(column)
    shape = (len(column), 1)
    # print("Column is oki")
    return value, shape, IS_COLUMN_VECTOR



def check_is_column_vector(column):

    if not  all([isinstance(row, list) and  len(row) == 1 and isinstance(row[0], float) for row in column]):
        return False
    return True


def is_row_vector(row_vector):

    value =  copy.deepcopy(row_vector)
    shape = (1, len(row_vector[0]))
    return value, shape

def check_is_row_vector(lst):
    if not isinstance(lst, list):
        return False
    if len(lst) != 1:
        return False
    if not isinstance(lst[0], list):
        return False
    if not all(isinstance(num, float) for num in lst[0]):
        return False
    return True

class Vector:

    def __init__(self, values):
        self.shape = tuple()

        if isinstance(values, int):
            self.values = [[float(i)] for i in range(values)]
            self.shape = (len(self.values), 1)
            self.data_type = IS_SIZE
        elif isinstance(values, tuple):
            self.values, self.shape, self.data_type = is_range(values)
        elif check_is_column_vector(values):
            self.values, self.shape, self.data_type = is_column_vector(values)

        elif check_is_row_vector(values):
            self.values, self.shape = is_row_vector(values)
            # print("the shape : ", self.shape)
        else:
            print("Errror ELse")
            exit(1)



    def __add__(self, other):
        if not (isinstance(other, Vector) and (other.shape == self.shape)):
            raise ValueError("Addition only between vectors of same shape")
        res = []
        if self.shape == (1, 1):
            res.append(self.values[0] + other.values[0])
        elif self.shape[0] > 1:#(n, 1)
            for a, b in zip(self.values, other.values):
                res.append([a[0] + b[0]])
        else: # # (1, n)
            for a, b in zip(self.values, other.values):
                res.append(a + b)
        return Vector(res)

    def __radd__(self, other):
        return self.__add__(other)

    
    def __sub__(self, other):
        if not (isinstance(other, Vector) and (other.shape == self.shape)):
            raise ValueError("Subtraction only between vectors of same shape")
        res = []
        if self.shape == (1, 1):
            res.append(self.values[0] - other.values[0])
        elif self.shape[0] > 1:#(n, 1)
            for a, b in zip(self.values, other.values):
                res.append([a[0] - b[0]])
        else: # (1, n)
            for a, b in zip(self.values, other.values):
                res.append(a - b)
        return Vector(res)


    def __rsub__(self, other):
        return self.__sub__(other)


    def __mul__(self, other):
        if not isinstance(other, (float, int)):
            raise ValueError("Multiplication only with float/int")
        res = []
        if self.shape == (1, 1):
            res.append(self.values[0] * other)
        elif self.shape[0] > 1:#(n, 1)
            for a in self.values:
                res.append([a[0] * other])
        else: # (1, n)
            res.append([a * other for a in self.values[0]])
        return Vector(res)


    def __rmul__(self, other):
        return self.__mul__(other)


    def __truediv__(self, other):
        try:
            if not isinstance(other, (float, int)):
                raise ValueError("Truediv only with float/int")
            if float(other) == 0.0:
                raise ValueError("# ZeroDivisionError: division by zero.")
            res = []
            if self.shape == (1, 1):
                res.append(self.values[0] / other)
            elif self.shape[0] > 1:#(n , 1)
                for a in self.values:
                    res.append([a[0] / other])
            else: # (1, n)
               res.append([a /other for a in self.values[0]])
        except ValueError as error_msg:
            print(error_msg)
        else:
            return Vector(res)


    def dot(self, other) -> float or int:
        try:
            if not (isinstance(other, Vector) and self.shape == other.shape) :
                raise ValueError("Vector.dot take a vector of same dimension")

            res = 0
            length = len(self.values)
            if self.shape[0] == 1:
                for a, b in zip(self.values[0], other.values[0]):
                    res += a * b
            else:
                for a, b in zip(self.values, other.values):
                    res += a[0] * b[0]
        except ValueError as error_msg:
            print(error_msg, file=sys.stderr)
        else:   
            return res
    
    def __rtruediv__(self, other):
        try:
            raise ValueError('A scalar cannot be divided by a Vector.')
        except ValueError as error_msg:
            print(error_msg, file=sys.stderr)


    def T(self):
        res = []
        if self.shape[0] > 1:
            tmp = [ x[0] for x in self.values]
            res.append(tmp)
        else:
            for lst in self.values:
                for x in lst:
                    res.append([x])

        print(res)
        return Vector(res)


    def __repr__(self) -> str:
        return (f"Values: {self.values} | Shape: {self.shape}")

    def __str__(self) -> str:
        return (f"Vector({self.values})")
