import math
def Kajeke(n):
    if n>=0:
        print(n)
        Kajeke(n - 1)
        
n = int(input())
Kajeke(n)