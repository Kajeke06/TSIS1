from itertools import permutations
def print_permutations():
    try:
        input_string = input("Enter a string: ")
        permuted_strings = [''.join(p) for p in permutations(input_string)]
        
        print("Permutations:")
        for permuted_string in permuted_strings:
            print(permuted_string)
    except ValueError:
        print("Error")

print_permutations()