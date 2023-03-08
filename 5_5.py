'''Changing Data in Table'''

import sqlite3

db = sqlite3.connect('test_sql.db')
print('Connected to Database')
cur = db.cursor()

update_surname = ('Sokolova', 4)
cur.execute('''UPDATE Students1 SET Last_name = ? WHERE StudentsID = ?;''', update_surname)
db.commit()
print('Table updated')
