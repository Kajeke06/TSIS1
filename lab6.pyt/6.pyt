import string
letters = string.ascii_lowercase
for letter in letters:
  filename = letter + ".txt"
  with open(filename, "w") as file:
    file.write(letter)
print("Created 26 text files (A.txt to Z.txt).")
#Режим "w" означает, что файл будет открыт для записи, и если файл с таким именем уже существует, его содержимое будет удалено.