'''
1. Создать базу данных exchanger.db
2. Создать таблицу users_balance с колонками UserID, Balance_RUB (INTEGER), Balance_USD (INTEGER),
Balance_EUR (INTEGER)
3. Добавить пользователя с данными 100000, 1000, 1000
4. Добавить следующий функционал:
- обмен валюты по желанию пользователя
5. Позволить пользователю самостоятельно выбрать валютную пару, используя ввод в консоль
и произвести обмен валюты, через input()
'''

import sqlite3

db = sqlite3.connect('exchanger.db')
print('Connected to Database')
cur = db.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS users_balance(
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Balance_RUB INTEGER NOT NULL,
    Balance_USD INTEGER NOT NULL,
    Balance_EUR INTEGER NOT NULL);
''')
db.commit()
print('Created users_balance table')

user = (100000, 1000, 1000)
cur.execute('''INSERT INTO users_balance(Balance_RUB, Balance_USD, Balance_EUR)
    VALUES(?, ?, ?);''', user)
db.commit()
print('Added new data')

usd_rub = 70
eur_rub = 80
usd_eur = 0.87
eur_usd = 1.15

cur1 = input('''Добро пожаловать в наш обменный пункт, курс валют следующий:
1 USD = 70 RUB
1 EUR = 80 RUB
1 USD = 0,87 EUR
1 EUR = 1,15 USD

Введите какую валюты желаете обменять:
1. RUB
2. USD
3. EUR: ''')

while cur1 not in ('1', '2', '3'):
    print('Incorrect input')
    cur1 = input('''Добро пожаловать в наш обменный пункт, курс валют следующий:
    1 USD = 70 RUB
    1 EUR = 80 RUB
    1 USD = 0,87 EUR
    1 EUR = 1,15 USD

    Введите какую валюты желаете обменять:
    1. RUB
    2. USD
    3. EUR: ''')

amount = input('Какая сумма Вас интересует?: ')
while not amount.isdigit():
    print('Incorrect input')
    amount = input('Какая сумма Вас интересует?: ')

cur2 = input('''Какую валюту готовы предложить взамен?
1. RUB
2. USD
3. EUR: ''')
while cur2 not in ('1', '2', '3') or cur1 == cur2:
    print('Incorrect input. Currency must be from the list bellow and different from the first')
    cur2 = input('''Какую валюту готовы предложить взамен?
    1. RUB
    2. USD
    3. EUR: ''')

cur.execute('''SELECT * FROM users_balance''')
table = cur.fetchall()
print(table[0][1], table[0][2], table[0][3])

if cur1 == '1' and cur2 == '2':
    while int(amount) > table[0][1]:
        print('Not enough money, choose another amount')
        amount = input('Какая сумма Вас интересует?: ')
    else:
        new_balance = (table[0][1] - int(amount), table[0][2] + int(amount) / usd_rub)
        cur.execute('''UPDATE users_balance SET Balance_RUB = ?, Balance_USD = ?;''', new_balance)
        db.commit()
        print('Success')

if cur1 == '1' and cur2 == '3':
    while int(amount) > table[0][1]:
        print('Not enough money, choose another amount')
        amount = input('Какая сумма Вас интересует?: ')
    else:
        new_balance = (table[0][1] - int(amount), table[0][3] + int(amount) / eur_rub)
        cur.execute('''UPDATE users_balance SET Balance_RUB = ?, Balance_EUR = ?;''', new_balance)
        db.commit()
        print('Success')

if cur1 == '2' and cur2 == '1':
    while int(amount) > table[0][2]:
        print('Not enough money, choose another amount')
        amount = input('Какая сумма Вас интересует?: ')
    else:
        new_balance = (table[0][2] - int(amount), table[0][1] + int(amount) * usd_rub)
        cur.execute('''UPDATE users_balance SET Balance_USD = ?, Balance_RUB = ?;''', new_balance)
        db.commit()
        print('Success')

if cur1 == '2' and cur2 == '3':
    while int(amount) > table[0][2]:
        print('Not enough money, choose another amount')
        amount = input('Какая сумма Вас интересует?: ')
    else:
        new_balance = (table[0][2] - int(amount), table[0][3] + int(amount) * usd_eur)
        cur.execute('''UPDATE users_balance SET Balance_USD = ?, Balance_EUR = ?;''', new_balance)
        db.commit()
        print('Success')

if cur1 == '3' and cur2 == '1':
    while int(amount) > table[0][3]:
        print('Not enough money, choose another amount')
        amount = input('Какая сумма Вас интересует?: ')
    else:
        new_balance = (table[0][3] - int(amount), table[0][1] + int(amount) * eur_rub)
        cur.execute('''UPDATE users_balance SET Balance_EUR = ?, Balance_RUB = ?;''', new_balance)
        db.commit()
        print('Success')

if cur1 == '3' and cur2 == '2':
    while int(amount) > table[0][3]:
        print('Not enough money, choose another amount')
        amount = input('Какая сумма Вас интересует?: ')
    else:
        new_balance = (table[0][3] - int(amount), table[0][2] + int(amount) * eur_usd)
        cur.execute('''UPDATE users_balance SET Balance_EUR = ?, Balance_USD = ?;''', new_balance)
        db.commit()
        print('Success')
