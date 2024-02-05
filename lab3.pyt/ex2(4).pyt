def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter():
    try:
        numbers = input("Enter the numbers separated by spaces: ")
        number_list = [int(num) for num in numbers.split()]
        prime_numbers = [num for num in number_list if is_prime(num)]
        
        print("Entered numbers:", number_list)
        print("prime numbers:", prime_numbers)
    except ValueError:
        print("Error")
filter()