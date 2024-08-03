import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')
#cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)',
 #              ('User', 'example@gmail.com', '10', '1000'))
for i in range(1, 11):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)',
                   (f'User{i}', f'example{i}@gmail.com', i*10, '1000'))

cursor.execute('UPDATE Users SET balance = ? WHERE id%2!=0', (500, ))
cursor.execute('DELETE FROM Users WHERE id%3==1')
cursor.execute('SELECT * FROM Users WHERE age!=60 ')
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')

cursor.execute('DELETE FROM Users WHERE id = 6')
cursor.execute('SELECT COUNT(id) FROM Users')
total_users = cursor.fetchone()[0]
print(total_users)
cursor.execute('SELECT SUM(balance) FROM Users')
all_balance = cursor.fetchone()[0]
print(all_balance)
print(all_balance / total_users)


connection.commit()
connection.close()