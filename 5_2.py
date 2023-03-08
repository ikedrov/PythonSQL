import sqlite3

'''Creating new Database'''

db = sqlite3.connect('test_sql.db')
print('Connected to Database')
cur = db.cursor()

#cur.execute('''CREATE TABLE IF NOT EXISTS Students(
#    StudentsID INTEGER PRIMARY KEY,
#    First_name TEXT NOT NULL,
#    Last_name TEXT NOT NULL);
#''')
#db.commit()
#print('Created Students Table')

#cur.execute('''INSERT INTO Students(StudentsID, First_name, Last_name)
#    VALUES(1, "Ivan", "Ivanov");''')
#db.commit()

cur.execute('''CREATE TABLE IF NOT EXISTS Students1(
    StudentsID INTEGER PRIMARY KEY AUTOINCREMENT,
    First_name TEXT NOT NULL,
    Last_name TEXT NOT NULL);
''')
db.commit()
print('Created Students1 Table')

#cur.execute('''INSERT INTO Students1(First_name, Last_name)
#    VALUES("Petr", "Petrov");''')
#db.commit()

#data_students = ('Semen', 'Semenov')
#cur.execute('''INSERT INTO Students1(First_name, Last_name)
#    VALUES(?, ?);''', data_students)
#db.commit()

data_students = [('Alex', 'Aleksandrov'), ('Olga', 'Olgina')]
cur.executemany('''INSERT INTO Students1(First_name, Last_name)
    VALUES(?, ?);''', data_students)
db.commit()
print('Added new data')