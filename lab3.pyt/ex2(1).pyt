def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

try:
    grams_amount = float(input("how many grams: "))
    result = grams_to_ounces(grams_amount)
    print(f"{grams_amount} grams is equal to {result:.2f} ounces.")
except ValueError:
    print("ERror")
