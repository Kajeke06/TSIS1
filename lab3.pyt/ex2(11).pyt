def is_palindrome(word):
    cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
    return cleaned_word == cleaned_word[::-1]

user_input = input()
if is_palindrome(user_input):
    print("Palindrome")
else:
    print("Not palindrome")