def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence


x = str(input())
result = reverse_words(x)
print(result)

"""
def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

x = input()
result = reverse_words(x)
print(result)
"""