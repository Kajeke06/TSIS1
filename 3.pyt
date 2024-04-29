import psycopg2

# Подключение к базе данных PostgreSQL
conn = psycopg2.connect(
    host="your_host",
    database="postgres",
    user="your_username",
    password="your_password"
)

# Создание курсора
cur = conn.cursor()

# Выполнение SQL-запроса
cur.execute("SELECT datname FROM pg_database;")

# Получение результатов запроса
rows = cur.fetchall()
for row in rows:
    print(row[0])

# Закрытие курсора и соединения
cur.close()
conn.close()
