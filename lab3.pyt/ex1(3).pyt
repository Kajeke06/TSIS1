class shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class rectangle(shape):
    def __init__(self):
        self.length = float(input())
        self.width = float(input())
    def area(self):
        return self.length * self.width
    
x = rectangle()
print("Area of recctangle:", x.area())
y = shape()
print("Area of shape:", y.area())