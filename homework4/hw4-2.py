import math

class dot:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def __str__(self):
        return "[" + str(self._x) + ", " + str(self._y) + "]"

def dist(vector1, vector2):
    return ((vector2.get_y() - vector1.get_y()) ** 2 + (vector2.get_x() - vector1.get_x()) ** 2) ** 0.5

class figure:
    def __init__(self, type="figure"):
        self._type = type

    def __str__(self):
        return str(self._type)

    def area(self):
        pass

    def perimeter(self):
        pass

class triangle(figure, dot):
    def __init__(self, dot1, dot2, dot3, type="triangle"):
        super().__init__(type)
        self._dot_1 = dot1
        self._dot_2 = dot2
        self._dot_3 = dot3

    def area(self):
        S = abs((self._dot_2.get_x() - self._dot_1.get_x())*(self._dot_3.get_y() - self._dot_1.get_y()) - (self._dot_3.get_x() - self._dot_1.get_x())*(self._dot_2.get_y() - self._dot_1.get_y()))/2
        return 'Triangle area S = ' + str(S)

    def perimeter(self):
        P = dist(self._dot_1, self._dot_2) + dist(self._dot_2, self._dot_3) + dist(self._dot_1, self._dot_3)
        return 'Triangle perimetr P = ' + str(P)

class parallelogram(figure, dot):
    def __init__(self, dot1, dot2, dot3, dot4, type="parallelogram"):
        super().__init__(type)
        self._dot_1 = dot1
        self._dot_2 = dot2
        self._dot_3 = dot3
        self._dot_4 = dot4

    def Normal(self):
        Height = ((dist(self._dot_1, self._dot_2))**2 + (dist(self._dot_2, self._dot_3))**2)**0.5
        return Height

    def area(self):
        if dist(self._dot_1, self._dot_2) >= dist(self._dot_2, self._dot_3):
            S = dist(self._dot_1, self._dot_2)*self.Normal()
        else:
            S = dist(self._dot_2, self._dot_3)*self.Normal()
        return 'Parallelogram area S = ' + str(S)

    def perimeter(self):
        Per = 2*(dist(self._dot_1, self._dot_2) + dist(self._dot_2, self._dot_3))
        return 'Parallelogram perimetr P = ' + str(Per)

class rhombus(parallelogram):
    def __init__(self, dot1, dot2, dot3, dot4, type="rhombus"):
        super().__init__(dot1, dot2, dot3, dot4, type)
        self._dot_1 = dot1
        self._dot_2 = dot2
        self._dot_3 = dot3
        self._dot_4 = dot4

    def area(self):
        S = 0.5*dist(self._dot_1, self._dot_3)*dist(self._dot_2, self._dot_4)
        return 'Rhombus area S = ' + str(S)

    def perimeter(self):
        P = 4*dist(self._dot_1, self._dot_2)
        return 'Rhombus perimeter P = ' + str(P)

class rectangle(parallelogram):
    def __init__(self, dot1, dot2, dot3, dot4, type="rectangle"):
        super().__init__(dot1, dot2, dot3, dot4, type)
        self._dot_1 = dot1
        self._dot_2 = dot2
        self._dot_3 = dot3
        self._dot_4 = dot4

    def area(self):
        S = dist(self._dot_1, self._dot_2)*dist(self._dot_2, self._dot_3)
        return 'Rectangle area S = ' + str(S)

    def perimeter(self):
        P = 2 * (dist(self._dot_1, self._dot_2) + dist(self._dot_2, self._dot_3))
        return 'Rectangle perimeter P = ' + str(P)

class square(rectangle, rhombus):
    def __init__(self, dot1, dot2, dot3, dot4, type="square"):
        super().__init__(dot1, dot2, dot3, dot4, type)
        self._dot_1 = dot1
        self._dot_2 = dot2
        self._dot_3 = dot3
        self._dot_4 = dot4

    def area(self):
        S = dist(self._dot_1, self._dot_2)**2
        return 'Square area S = ' + str(S)

    def perimeter(self):
        P = 4*dist(self._dot_1, self._dot_2)
        return 'Square perimeter P = ' + str(P)

class circle(figure, dot):
    def __init__(self, center, radius, type="circle"):
        super().__init__(type)
        self._dot_1 = center
        self._radius = radius

    def area(self):
        S = math.pi*(self._radius)**2
        return 'Circle area S = ' + str(S)

    def perimeter(self):
        P = 2*math.pi*self._radius
        return 'Circle perimeter P = ' + str(P)


a = triangle(dot(), dot(1, 3), dot(2, 1))
print(a)
print(a.perimeter())
print(a.area())
b = parallelogram(dot(), dot(2, 5), dot(7, 5), dot(5, 0))
print(b.area())
print(b.perimeter())
c = rhombus(dot(), dot(2, 3), dot(0, 4), dot(2, -3))
print(c)
print(c.area())
print(c.perimeter())
d = rectangle(dot(), dot(0, 3), dot(4, 3), dot(4, 0))
print(d)
print(d.area())
print(d.perimeter())
e = square(dot(), dot(0, 3), dot(3, 3), dot(3, 0))
print(e)
print(e.area())
print(e.perimeter())
f = circle(dot(), 6)
print(f)
print(f.area())
print(f.perimeter())
