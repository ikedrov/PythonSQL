'''Sending several requests'''

import sqlite3

db = sqlite3.connect('test_sql.db')
print('Connected to Database')
cur = db.cursor()

cur.executescript('''CREATE TABLE IF NOT EXISTS Students2(
    StudentsID INTEGER PRIMARY KEY AUTOINCREMENT,
    First_name TEXT NOT NULL,
    Last_name TEXT NOT NULL);
    
    INSERT INTO Students2(First_name, Last_name)
    VALUES("Fedor", "Fedorov");
''')
db.commit()
print('Created Students2 Table')

