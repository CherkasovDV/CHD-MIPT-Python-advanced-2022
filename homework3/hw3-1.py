import math

class Node:
    def __init__(self, value,
                 prev_pointer=None, next_pointer=None):
        self.set_value(value)
        self.set_prev(prev_pointer)
        self.set_next(next_pointer)

    def get_value(self):
        return self._value

    def get_next(self):
        return self._next_pointer

    def get_prev(self):
        return self._prev_pointer

    def set_value(self, value):
        self._value = value

    def set_prev(self, prev_pointer):
        self._prev_pointer = prev_pointer

    def set_next(self, next_pointer):
        self._next_pointer = next_pointer

    def __str__(self):
        return str(self.get_value())

class Complex:
 
    def __init__(self, collection = None):
        self._start_pointer = None
        self._finish_pointer = None
        self._length = 0

    def __len__(self):
        return self._length

    def append(self, value):
        if self._length == 0:
            self._start_pointer = Node(value)
            self._finish_pointer = self._start_pointer
            self._length = 1
        else:
            self._finish_pointer.set_next(Node(value,
                                               self._finish_pointer))
            self._finish_pointer = self._finish_pointer.get_next()
            self._length += 1

    def __getitem__(self, i):
        if i < 0 or i >= self._length:
            return False

        curr_pointer = self._start_pointer
        for j in range(i):
            curr_pointer = curr_pointer.get_next()
        return curr_pointer.get_value()
 
    def __add__(self, other):
        return Complex(self._start_pointer + other._start_pointer, self._finish_pointer + other._finish_pointer)
 
    def __sub__(self, other):
        return Complex(self._start_pointer - other._start_pointer, self._finish_pointer - other._finish_pointer)

    def abs(self):
        return math.sqrt(self._start_pointer**2 + self._finish_pointer**2)
    
    def __mul__(self, other):
        return Complex(self._start_pointer*other._start_pointer - self._finish_pointer*other._finish_pointer,
                       self._start_pointer*other._finish_pointer - self._finish_pointer*other._start_pointer)
 
    def __truediv__(self, other):
        return Complex((self._start_pointer*other._start_pointer + self._finish_pointer*other._finish_pointer)/(other._start_pointer**2 + other._finish_pointer**2),
                       (self._finish_pointer*other._start_pointer - self._start_pointer*other._finish_pointer)/(other._start_pointer**2 + other._finish_pointer**2))

    def convtoexp(self):
        return f'{self.abs()}*exp({math.atan(self._finish_pointer/self._start_pointer)}i)'

    def convtoalg(self):
        return f'{self._start_pointer*cos(self._finish_pointer)}{"-" if sin(self._finish_pointer) < 0 else "+"}{self._start_pointer*sin(self._finish_pointer)}i'

    def __str__(self):
        if self._length == 1:
            res = "%.2f+0.00i" % (self._start_pointer)
        else:
            res = "%.2f-%.2fi" % (self._start_pointer, abs(self._finish_pointer))
        return result

A = Complex()
B=list(map(float, input().split()))
for i in range(len(B)):
    A.append(B[i])
C = Complex()
D=list(map(float, input().split()))
for i in range(len(D)):
    C.append(D[i])
print(*map(str, [A+C, A-C, A*C, A/C, A.abs(), C.abs()]), sep='\n')
