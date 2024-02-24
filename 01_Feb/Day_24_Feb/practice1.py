# Question no 1
# Create a class named 'Student' with a string variable 'name' and an integer variable 'roll_no'. 
# Assign the value of roll_no as '2' and that of name as "John" by creating an object of the class Student.


class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def getdetails(self):
        return {'name': self.name, 'rollno': self.rollno}
    
stobj = Student('John', 2)
# print(stobj.getdetails())

#Question no 2
#Assign and print the roll number, phone number and address of two students having names "Sam" and "John" \
#respectively by creating two objects of the class 'Student'.

class StudentDetails:

    def __init__(self, name, phone_number, address):
        self.name = name
        self.phone_number = phone_number
        self.address = address

    def get_student_details(self):
        return {'name': self.name, 'phone_number': self.phone_number, 'address': self.address}
    
stobj1 = StudentDetails('Sam', 9845634564, 'Lalitpur')
stobj2 = StudentDetails('john', 9834214533, 'Kathmandu')

# print(stobj1.get_student_details())
# print(stobj2.get_student_details())

#Question no 3
#Write a program to print the area and perimeter of a triangle having sides of 3, 4 and 5 units by creating a 
#class named 'Triangle' with a function to print the area and perimeter.

class Triangle:

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def triangle_side_details(self):
        return {'side1': self.side1, 'side2': self.side2, 'side3': self.side3}
    
    def area(self):
        area = (self.side1 + self.side2 + self.side3) / 3
        print(f"Area of triangle: {area} cm^2")
        return self
    
    def perimeter(self):
        perimeter = (self.side1 + self.side2 + self.side3)
        print(f"perimeter of triangle: {perimeter} cm")
        return self
    
triangle1 = Triangle(3, 4, 5).area().perimeter()

#Question no 4
#Write a program to print the area of two rectangles having sides (4,5) and (5,8) respectively by creating a class 
#named 'Rectangle' with a function named 'Area' which returns the area. Length and breadth are passed as parameters to its constructor

class Rectangle:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def Area(self):
        area = print(f"Area of rectangle: {2*(self.length + self.breadth)} cm^2")
        return area
        
rectangle1 = Rectangle(4, 5).Area()
