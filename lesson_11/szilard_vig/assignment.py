class Polygons(object):
    
    def __init__(self,*args):
        self.sides = args
        
    def __str__(self):
        no_of_sides = len(self.sides)
        return f'{no_of_sides}is the number of sides'
        
    def display(self):
        for side_index, length in enumerate(self.sides, start=1):
            print(f'Side {side_index} with length:{length}')

class PerimeterMixin:

    def perimeter(self):
        perimeter = sum(self.sides)
        return f'The perimeter is {perimeter}'

class Triangle(PerimeterMixin, Polygons):
    # `s(s-a)(s-b)(s-c) ** 0.5` where s = `(a+b+c) / 2`
    def __init__(self,*args):
        super().__init__(*args)
        
    def area(self):
        s1 = self.sides[0]
        s2 = self.sides[1]
        s3 = self.sides[2]
        s_p = sum(self.sides) / 2 
        return (s_p*(s_p-s1)*(s_p-s2)*(s_p-s3))**0.5

class Square(PerimeterMixin, Polygons):
    def __init__(self,*args):
        super().__init__(*args)
        
    def area(self):
        side, *_ = self.sides
        return side ** 2

    @classmethod
    def from_area(cls, area):
        side = area ** 0.5
        return cls(side)




sq1 = Square(2)
sq1.display()

sq2 = Square.from_area(16)
sq2.display()

tr1 = Triangle(2,3,4)
print(tr1.perimeter())