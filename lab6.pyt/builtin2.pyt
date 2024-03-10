def Kajeke(string):
    uppercase_count = 0
    lowercase_count = 0
    for char in string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count +=1
    return uppercase_count, lowercase_count
input_string = input()
upper, lower = Kajeke(input_string)
print("uppercase_count", upper)
print("lowercase_count", lower)
