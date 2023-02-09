import sqlite3

conn = sqlite3.connect('database.db') # nos conectamos a la base de datos

conn.execute('CREATE TABLE halloffamesports (valoruno TEXT, valordos TEXT, valortres TEXT, valorquatro INTEGER)') # creamos una tabla con los campos correspondientes

conn.execute('CREATE TABLE halloffamemusic (valoruno TEXT, valordos TEXT, valortres TEXT, valorquatro INTEGER)') # creamos una tabla con los campos correspondientes

conn.execute('CREATE TABLE halloffamecars (valoruno TEXT, valordos INTEGER, valortres INTEGER, valorquatro TEXT)') # creamos una tabla con los campos correspondientes

conn.execute('CREATE TABLE halloffameteachers (valoruno TEXT, valordos TEXT, valortres TEXT, valorquatro INTEGER)') # creamos una tabla con los campos correspondientes

conn.execute('CREATE TABLE halloffamescietist (valoruno TEXT, valordos TEXT, valortres TEXT,valorquatro INTEGER)') # camos una tabla con los campos correspondientes

conn.execute('CREATE TABLE infofotos (name TEXT, historia TEXT)') # creamos una tabla con los campos correspondientes

conn.close()