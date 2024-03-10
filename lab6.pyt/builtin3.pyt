def is_palindrome(string):
    reversed_string = ''.join(reversed(string))
    if string == reversed_string:
        print("The string is palindrome!")
    else:
        print("The string is not palindrome!")
string = input("string: ")
is_palindrome(string)
