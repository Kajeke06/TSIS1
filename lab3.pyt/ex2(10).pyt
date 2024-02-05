def unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

input_list = input("given").split()
input_list = [int(num) for num in input_list]

result = unique_elements(input_list)
print( input_list)
print(result)