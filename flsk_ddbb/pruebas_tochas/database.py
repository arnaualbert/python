import sqlite3

conn = sqlite3.connect('database.db')


conn.execute('CREATE TABLE halloffamesports (name TEXT, sport TEXT, team TEXT, trofeos INTEGER)')

conn.execute('CREATE TABLE halloffamemusic (name TEXT, genre TEXT, grupo TEXT, grammy INTEGER)')

conn.execute('CREATE TABLE halloffamecars (name TEXT, price INTEGER, hp INTEGER, brand TEXT)')

conn.execute('CREATE TABLE halloffameteachers (name TEXT, asignatura TEXT, calidad TEXT, aprobados INTEGER)')

conn.execute('CREATE TABLE halloffamescietist (name TEXT, campo TEXT, papers INTEGER)')

conn.close()