import csv
import sqlite3

# Function to open a connection to the database
def get_db():
    conn = sqlite3.connect('friday_db.db')
    cursor = conn.cursor()
    return conn, cursor

# Function to create a table in the database
def create_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS job_applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            page_num INT,
            page_name TEXT,
            sign_up TEXT,
            Name TEXT,
            Email TEXT,
            understanding TEXT,
            confidence TEXT,
            assessment TEXT       
        )
    ''')

# Function to read data from the CSV file
def read_csv_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def transfer_data_to_db(cursor, csv_data):
    for row in csv_data:
        page_num  = row['Page_num']
        page_name = row['page_name']
        sign_up =row['sign-up status']
        Name = row['Name']  
        Email = row['Email']
        understanding =row['Understanding']
        confidence = row['Confidence']
        assessment = row['Assessment']

        cursor.execute('''
            INSERT INTO job_applications (page_num,page_name,sign_up,Name,Email,understanding,confidence,assessment)
            VALUES (?,?,?,?,?,?,?,?)
        ''', (row['Page_num'],row['page_name'],row['sign-up status'],row['Name'],row['Email'],row['Understanding'],row['Confidence'],row['Assessment']))

# Open a connection to the database
conn, cursor = get_db()

# Create the table in the database
create_table(cursor)

# Read data from the CSV file
csv_data = read_csv_file('job_applications.csv')

# Transfer data from the CSV file to the database table
transfer_data_to_db(cursor, csv_data)

# Commit and close the connection to the database
conn.commit()
conn.close()