import math
def Kajeke(a, b):
    for i in range(a, b):
        yield i * i
        
        
a = int(input())
b = int(input())
quadrat = 0
for square in Kajeke(a, b):
    quadrat += square
print(a, b, quadrat)