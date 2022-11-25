class Rectangle:
    
    #constructor
    def __init__(self, length, breadth):
        #Instance Variable
        self.length = length
        self.breadth = breadth
    
    #function of area and perimeter:
    def area(self):
        self.area = (self.length * self.breadth)
        return (self.area)
    def perimeter(self):
        self.perimeter = 2*(self.length * self.breadth)
        return (self.perimeter)

#passing arguments
r1 = Rectangle (10,20)
r2= Rectangle (5,30)

#printing
print (r1.area())
print(r2.perimeter())






