def Kajeke(n):
    result = []
    for num in range(n + 1):
        if num % 3 == 0 and num % 4 == 0:
            result.append(num)
    return result

n = int(input())
result_list = Kajeke(n)
for num in result_list:
    print(num)