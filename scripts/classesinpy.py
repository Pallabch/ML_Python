class Rectangle:
    def __init__(self,len,bre):
        self.length=len
        self.breadth=bre
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
    def display(self,length,breadth):
        print("The length is {}".format(length))
        print("The breadth is {}".format(breadth))
    
rect=Rectangle(10,5)

print(rect.area())
        





