import sqlite3

# Function to create a SQLite connection and cursor
def get_db():
    conn = sqlite3.connect('form_data.db')
    return conn, conn.cursor()

# Create table if it doesn't exist
def create_table():
    conn, cursor = get_db()
    cursor.execute('''CREATE TABLE IF NOT EXISTS formData 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT,
                       email TEXT,
                       qualification TEXT,
                       domain TEXT,
                       role TEXT,
                       experience TEXT,
                       about TEXT,
                       comments TEXT)''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_table()
