class shape():
    def __init__(self):
        pass
    def area(self):
        return 0
class square(shape):
    def __init__(self):
        self.length = float(input())
    def area(self):
        return self.length**22
    
x = square()
print(x.area())
y = shape()
print(y.area())
