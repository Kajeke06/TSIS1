import math
def cotan(x):
    return 1 / math.tan(x)
def Kajeke(n, m):
    radian = math.radians(180 / n)
    audan = n / 4 * m ** 2 * cotan(radian)
    return audan

n = float(input())
m = float(input())
audan = Kajeke(n, m)
print(audan)