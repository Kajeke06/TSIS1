from datetime import datetime

def Kajeke(data1, data2):
    data1 = datetime(*data1)
    data2 = datetime(*data2)
    
    difference_seconds = abs((data2 - data1).total_seconds())
    return difference_seconds

data1 = tuple(map(int, input("Enter date 1 (year month day): ").split()))
data2 = tuple(map(int, input("Enter date 2 (year month day): ").split()))

try:
    difference_in_seconds = Kajeke(data1, data2)
    print(difference_in_seconds)
except NotImplementedError:
    print()