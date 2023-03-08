'''
1. Создать базу данных registration.db
2. Создать таблицу users_data с колонками UserID, Login (TEXT), Password (TEXT), Code (INTEGER)
3. Добавить пользователя с данными Ivan, qwer1234, 1234
4. Добавить следующий функционал:
- 1.регистрация нового пользователя (предусмотреть что каждый пользователь имеет уникальный Login)
- 2.авторизация в системе - Login, Password
- 3.восстановление пароля по кодовому слову с заменой пароля (обязательный ввод Login)
5. Позволить пользователю самостоятельно выбрать одно из трех действий используя ввод в консоль,
через input() введя цифры 1,2,3.
'''

import sqlite3

db = sqlite3.connect('registration.db')
print('Connected to Database')
cur = db.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS users_data(
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Login TEXT NOT NULL,
    Password TEXT NOT NULL,
    Code INTEGER NOT NULL);
''')
db.commit()
print('Created users_data table')

user1 = ('Ivan', 'qwer1234', 1234)
cur.execute('''INSERT INTO users_data(Login, Password, Code)
    VALUES(?, ?, ?);''', user1)
db.commit()
print('Added new data')

request = input('1 - new user registration, 2 - authorize, 3 - change password: ')
if request not in ('1', '2', '3'):
    print('Invalid input!')
    request = input('1 - new user registration, 2 - authorize, 3 - change password: ')
cur.execute('''SELECT * FROM users_data''')
table = cur.fetchall()

if int(request) == 1:
    login = input('Enter login: ')
    while any(login in i for i in table):
        print(f'User {login} already exists')
        login = input('Enter login: ')
    password = input('Enter password: ')
    code = input('Enter digital code: ')
    while not code.isdigit():
        code = input('Enter digital code: ')
    new_user = (login, password, int(code))
    cur.execute('''INSERT INTO users_data(Login, Password, Code)
        VALUES(?, ?, ?);''', new_user)
    db.commit()
    print('New user added successfully')

if int(request) == 2:
    login1 = input('Enter login: ')
    password1 = input('Enter password: ')
    if any(login1 and password1 in i for i in table):
        print('Successfully authorized')
    else:
        print('Invalid login or password')

if int(request) == 3:
    login2 = input('Enter login: ')
    code1 = input('Enter digital code: ')
    while not code1.isdigit():
        code1 = input('Enter digital code: ')
    if not any(login2 and int(code1) in i for i in table):
        print('Invalid login or code')
    else:
        for i in table:
            if login2 in i:
                new_pass = input('Enter new password: ')
                cur.execute('''UPDATE users_data SET Password = ? WHERE UserID = ?;''', (new_pass, i[0]))
                db.commit()
                print('Password changed successfully')






