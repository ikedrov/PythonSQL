'''SELECT Request'''

import sqlite3

'''Connecting to Database'''

db = sqlite3.connect(r'/Users/ivankedrov/StepikSQL/4_2.db')
print('Connected to Database')
cur = db.cursor()

cur.execute('''SELECT * FROM Students;''')
#result_one = cur.fetchone()
result_many = cur.fetchmany(2)
# result_all = cur.fetchall()
#print(result_one)
print(result_many)
#print(result_all)