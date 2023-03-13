import sqlite3

'''Connecting to Database'''

db = sqlite3.connect(r'/Users/ivankedrov/StepikSQL/sql_join.db')
print('Connected to Database')
cur = db.cursor()

# cur.execute('''SELECT * FROM Persons''')
# result = cur.fetchall()
# print(result)

'''INNER JOIN'''
print('INNER JOIN')
cur.execute('''
SELECT PersonID, First_name, PositionID, Position
FROM Persons 
INNER JOIN Positions ON PositionID = Position_ref; ''')
result_all = cur.fetchall()
for result in result_all:
    print(result)
print('*' * 50)

'''LEFT JOIN'''
print('LEFT JOIN')
cur.execute('''
SELECT PersonID, First_name, PositionID, Position
FROM Persons 
LEFT JOIN Positions ON PositionID = Position_ref; ''')
result_all = cur.fetchall()
for result in result_all:
    print(result)
print('*' * 50)

'''RIGHT JOIN'''
print('RIGHT JOIN')
cur.execute('''
SELECT PersonID, First_name, PositionID, Position
FROM Positions 
LEFT JOIN Persons ON PositionID = Position_ref; ''')
result_all = cur.fetchall()
for result in result_all:
    print(result)
print('*' * 50)

'''FULL JOIN'''
print('FULL JOIN')
cur.execute('''
SELECT PersonID, First_name, PositionID, Position
FROM Persons 
LEFT JOIN Positions ON PositionID = Position_ref
UNION
SELECT PersonID, First_name, PositionID, Position
FROM Positions 
LEFT JOIN Persons ON PositionID = Position_ref;''')
result_all = cur.fetchall()
for result in result_all:
    print(result)
print('*' * 50)

'''Difference'''
print('Difference')
cur.execute('''
SELECT PersonID, First_name, PositionID, Position
FROM Persons 
LEFT JOIN Positions ON PositionID = Position_ref
WHERE PositionID IS NULL
UNION
SELECT PersonID, First_name, PositionID, Position
FROM Positions 
LEFT JOIN Persons ON PositionID = Position_ref
WHERE Position_ref IS NULL;''')
result_all = cur.fetchall()
for result in result_all:
    print(result)
print('*' * 50)