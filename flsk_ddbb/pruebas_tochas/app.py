from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/enternewsportman')
def new_sportman():
   return render_template('deportista.html')

@app.route('/addrecsport',methods = ['POST', 'GET'])
def addrecsport():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            sport = request.form['sport']
            team = request.form['team']
            trofeos = request.form['trofeos']

            with sql.connect("database.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO halloffamesports (name,sport,team,trofeos) VALUES (?,?,?,?)",(nm,sport,team,trofeos) )

                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
         return render_template("resultsport.html",msg = msg)
         con.close()

@app.route('/enternewmusic')
def new_music():
   return render_template('musico.html')

@app.route('/addrecmusic',methods = ['POST', 'GET'])
def addrecmusic():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            genre = request.form['genre']
            group = request.form['grupo']
            grammy = request.form['grammy']

            with sql.connect("database.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO halloffamemusic (name,genre,grupo,grammy) VALUES (?,?,?,?)",(nm,genre,group,grammy) )

                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
         return render_template("resultmusic.html",msg = msg)
         con.close()

@app.route('/enternewcar')
def new_car():
   return render_template('car.html')

@app.route('/addreccar',methods = ['POST', 'GET'])
def addreccar():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            price = request.form['price']
            hp = request.form['hp']
            brand = request.form['brand']

            with sql.connect("database.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO halloffamecars (name, price, hp, brand) VALUES (?,?,?,?)",(nm,price,hp,brand) )

                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
         return render_template("resultcar.html",msg = msg)
         con.close()


@app.route('/enternewteacher')
def new_teacher():
   return render_template('teacher.html')

@app.route('/addrecteacher',methods = ['POST', 'GET'])
def addrecteacher():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            asignatura = request.form['asignatura']
            calidad = request.form['calidad']
            aprobados = request.form['aprobados']

            with sql.connect("database.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO halloffameteachers (name, asignatura, calidad, aprobados) VALUES (?,?,?,?)",(nm,asignatura,calidad,aprobados) )

                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
         return render_template("resultteacher.html",msg = msg)
         con.close()


@app.route('/enternewscietist')
def new_scientist():
   return render_template('scientist.html')

@app.route('/addrecscientist',methods = ['POST', 'GET'])
def addrecscientist():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            campo = request.form['campo']
            papers = request.form['papers']

            with sql.connect("database.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO halloffamescietist (name , campo, papers) VALUES (?,?,?)",(nm,campo,papers) )

                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
         return render_template("resultscientist.html",msg = msg)
         con.close()

@app.route('/pregunta')
def pregunta():
    return render_template('buscar_fotos.html')

@app.route('/addpregunta',methods = ['POST','GET'])
def addpregunta():
    if request.method == 'POST':
        try:
            #basededatos = request.form['bbdd']
            #factores = request.form['factores']
            #factoritos = request.form['factoritos']

            with sql.connect("database.db") as con:
                con.row_factory = sql.Row
                cur = con.cursor()

                cur.execute("CREATE TABLE pregunta AS SELECT * FROM halloffamesports")#,(basededatos,factores, factoritos))
                con.commit()
                rows = cur.fetchall();
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
         return render_template("resultscientist.html",msg = msg)
         con.close()


def query_db(query, args=(), one=False):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


@app.route('/listrespuesta')
def listrespuesta():
   con = sql.connect("database.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from pregunta")

   rows = cur.fetchall();
   return render_template("respuesta.html",rows = rows)



@app.route('/listsport')
def listsport():
   con = sql.connect("database.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from halloffamesports")

   rows = cur.fetchall();
   return render_template("listsport.html",rows = rows)



@app.route('/listmusic')
def listmusic():
   con = sql.connect("database.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from halloffamemusic")

   rows = cur.fetchall();
   return render_template("listmusic.html",rows = rows)

@app.route('/listcar')
def listcar():
   con = sql.connect("database.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from halloffamecars")

   rows = cur.fetchall();
   return render_template("listcar.html",rows = rows)

@app.route('/listteacher')
def listteacher():
   con = sql.connect("database.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from halloffameteachers")

   rows = cur.fetchall();
   return render_template("listteacher.html",rows = rows)

@app.route('/listscientist')
def listscientist():
   con = sql.connect("database.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from halloffamescietist")

   rows = cur.fetchall();
   return render_template("listscientist.html",rows = rows)

if __name__ == '__main__':
    app.run(debug = True)
    # for user in query_db('select * from halloffamesports'):
    #     print(user['namem'], 'has the id', user['sport'])