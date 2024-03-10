import math
import time

def function(number, milliseconds):
    seconds = milliseconds / 1000
    time.sleep(seconds)
    square_root = math.sqrt(number)
    print(f"Square root of {number} after {milliseconds} is {square_root}")
number = int(input())
milliseconds = int(input())
function(number, milliseconds)