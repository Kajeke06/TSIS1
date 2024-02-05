def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        total_legs = 2 * chickens + 4 * rabbits
        if total_legs == numlegs:
            return chickens, rabbits

    return None

numheads = int(input("Enter the number of heads: "))
numlegs = int(input("Enter the number of legs: "))

result = solve(numheads, numlegs)

if result:
    chickens, rabbits = result
    print(f"Number of chickens: {chickens}, Number of rabbits: {rabbits}")
else:
    print("Solution not found.")