def Kajeke(n):
    for num in range(0, n + 1, 2):
        yield str(num)
        
        

n = int(input())
even_numbers = ", ".join(Kajeke(n))
print(even_numbers)