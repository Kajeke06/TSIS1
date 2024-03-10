file1 = input()
file2 = input()
with open (file1, 'r') as src:
    with open (file2, 'w') as copy:
        for i in src: #Этот цикл проходит по содержимому исходного файла построчно.
            copy.write(i)