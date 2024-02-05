def histogram(numbers):
    if not numbers:
        return
    
    numbers_list = [int(num) for num in numbers.split()]
    for num in numbers_list:
        print('*' * num)

numbers_input = input()
histogram(numbers_input)