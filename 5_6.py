'''Deleting data from table'''

import sqlite3

db = sqlite3.connect('test_sql.db')
print('Connected to Database')
cur = db.cursor()

delete_data = '3'
cur.execute('''DELETE FROM Students1 WHERE StudentsID = ?;''', delete_data)
db.commit()
print('Data is deleted')

# cur.execute('''DROP TABLE Students2''')
# db.commit()
# print('Table is deleted')