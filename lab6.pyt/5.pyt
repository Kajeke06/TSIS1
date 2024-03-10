list = ['men', 'oku', 'su', 'mers', 'bmw']

file_name=input("Enter your file name:")

with open(file_name, "w") as f:
    for x in list:
        f.write(x + "\n")
#Режим "w" означает, что файл будет открыт для записи, и если файл с таким именем уже существует, его содержимое будет удалено.
print("List has been written to", file_name)