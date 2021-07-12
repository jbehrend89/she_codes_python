import sqlite3

connection = sqlite3.connect("books.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS book (
        id INTEGER PRIMARY KEY,
        title TEXT, 
        pages INTEGER,
        current_page INTEGER
    )
""")

# cursor.execute("""
#     INSERT INTO book VALUES (
#         9, 'A Great Book', 213, 27
#     )
# """)

# cursor.execute("""
#     INSERT INTO book VALUES (
#         10, 'Another Great Book', 213, 27
#     )
# """)


connection.commit()

rows = cursor.execute("""
    SELECT title, pages, current_page FROM book
""")

for row in rows:
    print(row)
connection.close
