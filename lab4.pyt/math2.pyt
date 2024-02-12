import math
#s = 1/2 *a *h;
def Kajeke(a, b, h):
    audan = 1/2 * (a+b) * h
    return audan


h = float(input())
a = float(input())
b = float(input())
audan = Kajeke(a, b, h)
print(audan)