import sqlite3

conn = sqlite3.connect('database.db')


conn.execute('CREATE TABLE halloffame (name TEXT, sport TEXT, team TEXT, age TEXT)')

conn.close()