import math

class Polygons(object):
    def __init__(self, *args):
        self.sides = args

    def __str__(self):
        no_of_sides = len(self.sides)
        return '{} is the number of sides'.format(no_of_sides)

    def display(self):
        for side_index, length in enumerate(self.sides, start=1):
            print('Side {} with length: {}'.format(side_index, length))

class PerimeterMixin():
    def perimeter(self):
        return f'The perimeter is {sum(self.sides)}'

class Triangle(PerimeterMixin, Polygons):
    # `s(s-a)(s-b)(s-c) ** 0.5` where s = `(a+b+c) / 2`
    def __init__(self, *args):
        super().__init__(*args)

    def area(self):
        s1, s2, s3 = self.sides
        s_p = sum(self.sides) / 2
        return math.sqrt(s_p * (s_p - s1) * (s_p - s2) * (s_p - s3))

class Square(Polygons):
    def __init__(self, side):
        super().__init__(side, side, side, side)

    @classmethod
    def from_area(cls, area):
        side = math.sqrt(area)
        return cls(side)

    def area(self):
        side, *_ = self.sides
        return side**2

sq1 = Square(4)
sq1.display()

sq2 = Square.from_area(25)
sq2.display()

tr1 = Triangle(2,3,4)
# tr1.display()
print(tr1.perimeter())