import math as m
def circle(r):
    def area(radius=r):
        return 2*radius
    def perimeter(r):
        return 3*r
    return area,perimeter

a,p=circle(5)
x=a()
print("1st "+str(x))
x=a(100)
print("1st "+str(x))
# x=a(10)
# print("2nd"+str(x))
