def Kajeke(n):
    for num in range(1, n + 1):
        yield num * num
# Yield:Квадрат каждого числа от 1 до N.



n = int(input())
for quadrat in Kajeke(n):
    print(quadrat)