def insert_spaces(text):
    words = [text[0]]
    for char in text[1:]:
        if char.isupper():
            words.append(char)
        else:
            words[-1] += char
        return ' '.join(words)
string = input()
formatted_text = insert_spaces(string)
print(formatted_text)