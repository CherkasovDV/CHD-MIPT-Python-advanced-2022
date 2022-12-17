import math

class NotSingleExponentalRepresent(Exception):
    pass

class ValueError(Exception):
    pass

class Complex:
    def __init__(self, x=0, y=0):
        self.set(x, y)
        if type(self._x) == int or type(self._x) == float:
            self._x = x
        else:
            raise ValueError
        if type(self._y) == int or type(self._y) == float:
            self._y = y
        else:
            raise ValueError
        if math.sqrt(self._x ** 2 + self._y ** 2) > 0:
            self._r = (x ** 2 + y ** 2) ** 0.5
            self._phi = math.atan(y / x)
        else:
            raise NotSingleExponentalRepresent('')

    def get(self):
        return self._x, self._y

    def set(self, x, y):
        self._x = x
        self._y = y

    def exponential(self):
        return self._r, self._phi

    def classical(self):
        if self._r > 0:
            self._x = self._r*math.cos(self._phi)
            self._y = self._r*math.sin(self._phi)
            return str(self._x, self._y)
        return str('R Value must be more than zero!')

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            return self._x + other, self._y
        if type(other) == Complex:
            return self._x + other._x, self._y + other._y

    def __radd__(self, other):
        if type(other) == int or type(other) == float:
            return self._x + other, self._y
        if type(other) == Complex:
            return self._x + other._x, self._y + other._y

    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            return self._x - other, self._y
        if type(other) == Complex:
            return self._x - other._x, self._y - other._y

    def __rsub__(self, other):
        if type(other) == int or type(other) == float:
            return self._x - other, self._y
        if type(other) == Complex:
            return self._x - other._x, self._y - other._y

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return self._x * other, self._y * other
        if type(other) == Complex:
            return self._x * other._x - self._y * other._y, self._x * other._y + self._y * other._x

    def __rmul__(self, other):
        if type(other) == int or type(other) == float:
            return self._x * other, self._y * other
        if type(other) == Complex:
            return self._x * other._x - self._y * other._y, self._x * other._y + self._y * other._x

    def __truediv__(self, other):
        if type(other) == int or type(other) == float:
            if other != 0:
                return self._x / other, self._y / other
            return str('Devisor must not be equal to zero!')
        if type(other) == Complex:
            if other._x != 0 or other._y != 0:
                Re_num = self._x * other._x - self._y * other._y
                Im_num = self._x * other._y + other._x * self._y
                denom = (other._x) ** 2 + (other._y) ** 2
                num1 = Re_num / denom
                num2 = Im_num / denom
                return num1, num2
            return str('Devisor must not be equal to zero!')

    def __rtruediv__(self, other):
        if type(other) == int or type(other) == float:
            if other != 0:
                return self._x / other, self._y / other
            return str('Devisor must not be equal to zero!')
        if type(other) == Complex:
            if other._x != 0 or other._y != 0:
                Re_num = self._x * other._x - self._y * other._y
                Im_num = self._x * other._y + other._x * self._y
                denom = (other._x) ** 2 + (other._y) ** 2
                num1 = Re_num / denom
                num2 = Im_num / denom
                return num1, num2
            return str('Devisor must not be equal to zero!')
