def fahrenheit_to_celcius(fahrenheit):
    celcius = (5 / 9) * (fahrenheit - 32)
    return celcius

try:
    fahrenheit_temp = float(input("Enter temperature in Fahrenheit: "))
    celcius_temp = fahrenheit_to_celcius(fahrenheit_temp)
    print("{} Fahrenheit is equal to {:.2f} Celcius".format(fahrenheit_temp, celcius_temp))
except ValueError:
    print("Error: Please enter a valid number for temperature.")