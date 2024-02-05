import math 
class Point:
    def __init__(self, x, y, x1, y1):
        self.x = x
        self.x1 = x1
        self.y = y
        self.y1 = y1
        
    def show(self):
        print(f"X is equal to: {self.x}")
        print(f"Y is equal to: {self.y}")
        
    def move(self):
        print(f"After moving X1 is equal to: {self.x1}")
        print(f"After moving Y1 is equal to: {self.y1}")
        
    def dist(self):
        return math.sqrt((self.x - self.x1)**2 + (self.y - self.y1)**2)
    
x = int(input("Enter the value of X: "))
y = int(input("Enter the value of Y: "))
x1 = int(input("Enter the value of X1: "))
y1 = int(input("Enter the value of Y1: "))
coor = Point(x, y, x1, y1)
coor.show()
coor.move()
print(coor.dist())