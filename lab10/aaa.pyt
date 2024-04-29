import psycopg2
import csv

# Соединение с базой данных
host = "127.0.0.1"
user = "postgres"
password = "Kajeke006"
db_name = "suppliers"

conn = psycopg2.connect(
    host="127.0.0.1",
    user="postgres",
    password="Kajeke006",
    database="suppliers"
)

# Создание курсора для выполнения запросов
cur = conn.cursor()

def InputData():
    name = input("Input your name: ")
    number = input("Input your phone number: ")
    cur.execute('INSERT INTO phonebook ("name", "number") VALUES (%s, %s);', (name, number))

def Import():
    with open(r'C:\Users\User\Desktop\kajy.python\lab10\data.csv', 'r') as file:
        read = csv.reader(file)
        for i in read:
            name, phone_number = i
            cur.execute(' INSERT INTO phonebook ("name", "number") VALUES(%s, %s);', (name, phone_number))

def update_contact(name, phone_number):
    cur.execute('UPDATE phonebook SET "number"=%s WHERE "name"=%s', (name, phone_number))

def queryData():
    cur.execute(' SELECT * FROM phonebook ')
    data = cur.fetchall()
    path = r"C:\Users\User\Desktop\kajy.python\results.txt"  # Укажите путь к файлу, который вы хотите создать и записать
    
    f = open(path, "w")  # Открываем файл для записи
    for row in data:
        f.write("Name: " + str(row[0]) + "\n" + "Number: " + str(row[1]) + "\n")
    f.close() 

def deleteData():
    print("Which name do you want to delete?\n")
    personName = input()
    cur.execute(f''' DELETE FROM phonebook WHERE "name"='{personName}' ''')

def deleteAllData():
    cur.execute(' DELETE FROM phonebook ')

while True:
    try:
        x = int(input())
        if x == 1:
            InputData()
            conn.commit()  # Подтверждаем изменения в базе данных после каждой вставки данных
        elif x==2:
            Import()
            conn.commit()
        elif x==3:
            name1=input("Input name:")
            phone_number1=input("Input number:")
            update_contact(name1, phone_number1)
            conn.commit()
        if x == 4:
            queryData()
            conn.commit()
        if x == 5:
            deleteData()
            conn.commit()
        if x == 6:
            deleteAllData()
            conn.commit()
        elif x==7:
            break  # Выходим из цикла
    except ValueError:
        print("Invalid input. Please enter a number.")

# Закрытие курсора и соединения
cur.close()
conn.close()
