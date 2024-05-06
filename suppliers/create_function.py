import psycopg2

conn = psycopg2.connect(
    host="127.0.0.1",
    database="postgres",
    user="postgres",
    password="Kajeke006"
)

cur = conn.cursor()

# Запрос для создания функции
create_function_query = """
CREATE OR REPLACE FUNCTION get_records_by_pattern(search_pattern TEXT)
RETURNS TABLE(id INT, name TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY SELECT * FROM phonebook WHERE name LIKE search_pattern;
END;
$$ LANGUAGE plpgsql;
"""

# Выполнение запроса
cur.execute(create_function_query)

# Применение изменений
conn.commit()

# Закрытие соединения
cur.close()
conn.close()
