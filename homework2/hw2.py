import math

class Complex:
 
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
        
    def __get__(self):  
        return self
    
    def __set__(self, a, b):  
        self._a = a
        self._b = b
        
    def __repr__(self):
        return f'{self.a}{"-" if self.b < 0 else "+"}{abs(self.b)}i'
 
    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.a + other.a, self.b + other.b)
        if isinstance(other, (int, float)):
            return Complex(self.a + other, self.b)
        raise NotImplementedError
 
    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.a - other.a, self.b - other.b)
        if isinstance(other, (int, float)):
            return Complex(self.a - other, self.b)
        raise NotImplementedError

    def mod(self):
        return math.sqrt(self.a**2 + self.b**2)
    
    def __mul__(self, other):
        return Complex(self.a*other.a - self.b*other.b, self.a*other.b - self.b*other.a)
 
    def __truediv__(self, other):
        return Complex((self.a*other.a + self.b*other.b)/(other.a**2 + other.b**2), (self.b*other.a - self.a*other.b)/(other.a**2 + other.b**2))

    def convtoexp(self):
        return f'{mod(self)}*exp({math.atan(self.b/self.a)}i)'

    def convtoalg(self):
        return f'{self.a*cos(self.b)}{"-" if sin(self.b) < 0 else "+"}{self.a*sin(self.b)}i'
 
c1 = Complex(1, 2)
c2 = Complex(7, -8)
print(c1, c2)
print(c1/c2)
