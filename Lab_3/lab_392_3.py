import math

file = open(r'shape.txt')
lines = file.readlines()
file.close()
shape_lis = []
tri_count = 1
rec_count = 1
cir_count = 1


class Shape:
    def __init__(self):
        pass

    def getarea(self):
        pass


class Rectangle(Shape):
    def __init__(self, l, w):
        super().__init__()
        self.l = l
        self.w = w

    def getarea(self):
        return self.l * self.w


class Triangle(Shape):
    def __init__(self, b, h):
        super().__init__()
        self.b = b
        self.h = h

    def getarea(self):
        return (self.b * self.h) / 2


class Circle(Shape):
    def __init__(self, r):
        super().__init__()
        self.r = r

    def getarea(self):
        return round(math.pi * self.r * self.r, 2)


for line in lines:
    components = line.split(',')
    shape = components[0]
    if shape == "Rectangle":
        shape_lis.append(Rectangle(float(components[1]), float(components[2])))
    if shape == "Triangle":
        shape_lis.append(Triangle(float(components[1]), float(components[2])))
    if shape == "Circle":
        shape_lis.append(Circle(float(components[1])))


for shape in shape_lis:
    if 'Rectangle' in str(shape):
        print("Rectangle" + str(rec_count) + "'s area is: " + str(shape.getarea()))
        rec_count += 1
    if 'Triangle' in str(shape):
        print("Triangle" + str(tri_count) + "'s area is: " + str(shape.getarea()))
        tri_count += 1
    if 'Circle' in str(shape):
        print("Circle" + str(cir_count) + "'s area is: " + str(shape.getarea()))
        cir_count += 1

