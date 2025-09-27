from math import sqrt

class TrException (Exception):
    pass

class Triangle:
    def __init__(self, a, b, c):
        if a<=0 or c<=0 or b<=0:
            raise TrException('отрицательная или нулевая длина стороны')
        if is_triangle(a, b, c):
            self.a = a
            self.b = b
            self.c = c
        else:
            raise TrException('это не треугольник')

    def perimeter(self):
        return round(self.a+self.b+self.c, 14)
    def area (self):
        pp = self.perimeter()/2
        return sqrt(pp*(pp-self.a)*(pp-self.b)*(pp-self.c))

def is_triangle(a, b, c):
    return a<b+c and b <a+c and c< a+b