from flask import Flask, Response, render_template

#1 inicializacion
module_name = __name__
app: Flask = Flask(__name__)

#3 rutas
@app.route("/")
def index():

    html : str = render_template("index.html", title="Flask v3", name="Arnau") # con render tamplate se le pasa el nombre de el archivo y las variables

    return html

#2 run
if __name__ == "__main__":
    app.run(debug=True)