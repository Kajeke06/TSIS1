def prime(number):
    if int(number) < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

integer = input()
numbers = integer.split()
numbers = [int(num) for num in numbers]

only_prime = list(filter(lambda x: prime(x), numbers))

print("Prime numbers:", only_prime)