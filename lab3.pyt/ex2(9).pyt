import math

def sphere_volume(radius):

    if radius < 0:
        return 

    volume = (4 / 3) * math.pi * radius**3
    return volume


radius_input = float(input())
result = sphere_volume(radius_input)
print(f"{radius_input} = {result}")
