class Area:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def details(self):
        print(f'The details of the rectangle are: length {self.length} cm, breadth: {self.breadth} cm')

#inheritence from the parent class
class Rectangle(Area):
    def __init__(self, length, breadth):
        super().__init__(length, breadth)

    def Area_of_Rectangle(self):
        area = self.length * self.breadth
        print(f'Area of rectangle is {area} cm^2')




for i in range(1, 10):
    obj1 = Rectangle(3,2)
    obj1.Area_of_Rectangle()
    obj1.details()

for i in range(1, 6):
    for j in range(i, 6):
        print('*', end="")

    print("")

