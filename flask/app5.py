from unicodedata import name
from flask import Flask, Response, render_template

# parametros por ruta

#1 inicializacion
module_name = __name__
app: Flask = Flask(__name__)

#3 rutas
@app.route("/")
def index():

    saludo : str = "hola" # con render tamplate se le pasa el nombre de el archivo y las variables

    return saludo

@app.route("/hello/<name>")
def saludo(name):

    saludo : str = f"hola {name}"# con render tamplate se le pasa el nombre de el archivo y las variables

    return saludo


#2 run
if __name__ == "__main__":
    app.run(debug=True)