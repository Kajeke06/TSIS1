def Kajeke(string):
    result = []
    for char in string:
        if char.isupper():
            result.append(char)
    return result
string = input()
result = Kajeke(string)
print(result)