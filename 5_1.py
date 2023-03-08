import sqlite3

'''Connecting to Database'''

db = sqlite3.connect(r'/Users/ivankedrov/StepikSQL/4_2.db')
print('Connected to Database')
cur = db.cursor()

cur.execute('''SELECT * FROM Students''')
result = cur.fetchall()
print(result)
