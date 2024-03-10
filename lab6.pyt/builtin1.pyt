import math

def multiply_numbers(numbers):
    return math.prod(numbers)

numbers = [3 , 4 , 5 , 6]
result = multiply_numbers(numbers)
print("Result:", result)

"""
import math

def multiply_numbers(numbers):
    numbers = [int(x) for x in numbers.split()]
    return math.prod(numbers)

numbers = input()
result = multiply_numbers(numbers)
print(result)
"""