import sqlite3

# Connect to the SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create the table with three columns: id, name, and age
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Insert three records into the table
users = [
    (1, 'John', 25),
    (2, 'Alice', 30),
    (3, 'Bob', 28)
]

cursor.executemany('INSERT INTO users VALUES (?, ?, ?)', users)

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()
