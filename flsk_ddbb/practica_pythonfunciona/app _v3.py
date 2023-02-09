from crypt import methods
from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html') # we return an html when they are on the main page

@app.route('/delete',methods=['POST','GET'])
def delete_something():
    if request.method == 'GET':
        return render_template('borra.html')
    if request.method == 'POST':
        database = request.form['database']
        uid = request.form['uid']
        con=sql.connect("database.db")
        cur=con.cursor()
        cur.execute(f"delete from {database} where valoruno = ?",(uid,))
        con.commit()
    return render_template('home.html')

@app.route('/witm',methods = ['POST','GET'])
def pwitm():
    if request.method == 'GET':
        return render_template('witm.html')
    if request.method == 'POST':
        database = request.form['database']
        campo = request.form['campo']
        con = sql.connect("database.db") # connect to the database
        con.row_factory = sql.Row
   
        cur = con.cursor() # we open a cursor
        cur.execute(f"select * from {database} where {campo} = (SELECT max({campo}) from {database})") # select all from database
   
        rows = cur.fetchall()
    return render_template("pregunta.html",rows = rows)
    con.close()

@app.route('/add',methods = ['GET','POST'])
def add():
    if request.method == 'GET':
        return render_template('form.html')
    if request.method == 'POST': # if the data request method is POST it does the following;
        try:
            database = request.form['database']
            valoruno = request.form['valoruno'] # we request the information to the form
            valordos = request.form['valordos'] # we request the information to the form
            valortres = request.form['valortres'] # we request the information to the form
            valorquatro = request.form['valorquatro']
         
            with sql.connect("database.db") as con: # connect to the database
                cur = con.cursor() # we open a cursor
            
                cur.execute(f"INSERT INTO {database} (valoruno , valordos, valortres,valorquatro) VALUES (?,?,?,?)",(valoruno,valordos,valortres,valorquatro) ) # insert the data into the sqlite3 table
            
                con.commit() # we do the commit
                msg = "Funciona" # we put the message for the html that we will return if it works
        except:
            con.rollback()
            msg = "No" # we put the message for the html that we will return if it does not work
      
        finally:
            return render_template("resultscientist.html",msg = msg) # we return an html saying if it has been added correctly or not
            con.close()

@app.route('/fotos',methods = ['POST', 'GET'])
def get_fotos():
    if request.method == 'GET':
        return render_template('fotos.html')
    if request.method == 'POST': # if the data request method is POST it does the following;
        try:
            foto = request.form['foto'] # we request the information to the form
            if foto == 'deporte': 
                return render_template('deporte.html') # if the variable is deporte it shows its respective html
            elif foto == 'music':
                return render_template('music.html') # if the variable is music it shows its respective html
            elif foto == 'ciencia':
                return render_template('ciencia.html') # if the variable is ciencia it shows its respective html
        except:
            return render_template('no_funciona.html')
            
@app.route('/msn')
def listmsn():
    con = sql.connect("database.db") # connect to the database
    con.row_factory = sql.Row
   
    cur = con.cursor() # we open a cursor
    cur.execute("select * from infofotos where name = 'msn'") # select all from database
   
    rows = cur.fetchall()
    return render_template("show.html",rows = rows) # we return an html with the information from the database

@app.route('/palou')
def listpalou():
    con = sql.connect("database.db") # connect to the database
    con.row_factory = sql.Row
   
    cur = con.cursor() # we open a cursor
    cur.execute("select * from infofotos where name = 'palou'") # select all from database
   
    rows = cur.fetchall()
    return render_template("show.html",rows = rows) # we return an html with the information from the database

@app.route('/warriors')
def listwarriors():
    con = sql.connect("database.db") # connect to the database
    con.row_factory = sql.Row
   
    cur = con.cursor() # we open a cursor
    cur.execute("select * from infofotos where name = 'curry'") # select all from database
   
    rows = cur.fetchall()
    return render_template("show.html",rows = rows) # we return an html with the information from the database

@app.route('/messi')
def listmessi():
    con = sql.connect("database.db") # connect to the database
    con.row_factory = sql.Row
   
    cur = con.cursor() # we open a cursor
    cur.execute("select * from infofotos where name = 'messi'") # select all from database
   
    rows = cur.fetchall()
    return render_template("show.html",rows = rows) # we return an html with the information from the database

@app.route('/motogp')
def listmotogp():
    con = sql.connect("database.db") # connect to the database
    con.row_factory = sql.Row
   
    cur = con.cursor() # we open a cursor
    cur.execute("select * from infofotos where name = 'motogp'") # select all from database
   
    rows = cur.fetchall()
    return render_template("show.html",rows = rows) # we return an html with the information from the database

@app.route('/bolt')
def listbolt():
    con = sql.connect("database.db") # connect to the database
    con.row_factory = sql.Row
   
    cur = con.cursor() # we open a cursor
    cur.execute("select * from infofotos where name = 'bolt'") # select all from database
   
    rows = cur.fetchall()
    return render_template("show.html",rows = rows) # we return an html with the information from the database

@app.route('/travis')
def listravis():
    con = sql.connect("database.db") # connect to the database
    con.row_factory = sql.Row
   
    cur = con.cursor() # we open a cursor
    cur.execute("select * from infofotos where name = 'travis'") # select all from database
   
    rows = cur.fetchall()
    return render_template("show.html",rows = rows) # we return an html with the information from the database

@app.route('/mozart')
def listmozart():
    con = sql.connect("database.db") # connect to the database
    con.row_factory = sql.Row
   
    cur = con.cursor() # we open a cursor
    cur.execute("select * from infofotos where name = 'mozart'") # select all from database
   
    rows = cur.fetchall()
    return render_template("show.html",rows = rows) # we return an html with the information from the database

@app.route('/acdc')
def listacdc():
    con = sql.connect("database.db") # connect to the database
    con.row_factory = sql.Row
   
    cur = con.cursor() # we open a cursor
    cur.execute("select * from infofotos where name = 'acdc'") # select all from database
   
    rows = cur.fetchall()
    return render_template("show.html",rows = rows) # we return an html with the information from the database

@app.route('/marley')
def listmarley():
    con = sql.connect("database.db") # connect to the database
    con.row_factory = sql.Row
   
    cur = con.cursor() # we open a cursor
    cur.execute("select * from infofotos where name = 'marley'") # select all from database
   
    rows = cur.fetchall()
    return render_template("show.html",rows = rows) # we return an html with the information from the database

@app.route('/beatles')
def listbeatles():
    con = sql.connect("database.db") # connect to the database
    con.row_factory = sql.Row
   
    cur = con.cursor() # we open a cursor
    cur.execute("select * from infofotos where name = 'beatles'") # select all from database
   
    rows = cur.fetchall()
    return render_template("show.html",rows = rows) # we return an html with the information from the database

@app.route('/sinatra')
def listsinatra():
    con = sql.connect("database.db") # connect to the database
    con.row_factory = sql.Row
   
    cur = con.cursor() # we open a cursor
    cur.execute("select * from infofotos where name = 'sinatra'") # select all from database
   
    rows = cur.fetchall()
    return render_template("show.html",rows = rows) # we return an html with the information from the database

@app.route('/erwin')
def listerwin():
    con = sql.connect("database.db") # connect to the database
    con.row_factory = sql.Row
   
    cur = con.cursor() # we open a cursor
    cur.execute("select * from infofotos where name = 'erwin'") # select all from database
   
    rows = cur.fetchall()
    return render_template("show.html",rows = rows) # we return an html with the information from the database

@app.route('/marie')
def listmarie():
    con = sql.connect("database.db") # connect to the database
    con.row_factory = sql.Row
   
    cur = con.cursor() # we open a cursor
    cur.execute("select * from infofotos where name = 'marie'") # select all from database
   
    rows = cur.fetchall()
    return render_template("show.html",rows = rows) # we return an html with the information from the database

@app.route('/newton')
def listnewton():
    con = sql.connect("database.db") # connect to the database
    con.row_factory = sql.Row
   
    cur = con.cursor() # we open a cursor
    cur.execute("select * from infofotos where name = 'newton'") # select all from database
   
    rows = cur.fetchall()
    return render_template("show.html",rows = rows) # we return an html with the information from the database

@app.route('/einstein')
def listeinstein():
    con = sql.connect("database.db") # connect to the database
    con.row_factory = sql.Row
   
    cur = con.cursor() # we open a cursor
    cur.execute("select * from infofotos where name = 'einstein'") # select all from database
   
    rows = cur.fetchall()
    return render_template("show.html",rows = rows) # we return an html with the information from the database

@app.route('/nobel')
def listnobel():
    con = sql.connect("database.db") # connect to the database
    con.row_factory = sql.Row
   
    cur = con.cursor() # we open a cursor
    cur.execute("select * from infofotos where name = 'nobel'") # select all from database
   
    rows = cur.fetchall()
    return render_template("show.html",rows = rows) # we return an html with the information from the database

@app.route('/franklin')
def listfranklin():
    con = sql.connect("database.db") # connect to the database
    con.row_factory = sql.Row
   
    cur = con.cursor() # we open a cursor
    cur.execute("select * from infofotos where name = 'franklin'") # select all from database
   
    rows = cur.fetchall()
    return render_template("show.html",rows = rows) # we return an html with the information from the database

@app.route('/list',methods = ['POST','GET'])
def list_query():
    if request.method == 'GET':
        return render_template('form_list.html')
    elif request.method == 'POST':
        database = request.form['database']
        con = sql.connect("database.db") # connect to the database
        con.row_factory = sql.Row
   
        cur = con.cursor() # we open a cursor
        cur.execute(f"select * from {database}") # select all from database
   
        rows = cur.fetchall()
    return render_template("list_query.html",rows = rows)
    con.close()
    
if __name__ == '__main__':
   app.run(debug = True)