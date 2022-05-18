from flask import Flask, Response

#1 inicializacion
module_name = __name__
app: Flask = Flask(__name__)

#3 rutas
@app.route("/")
def index():

    quote: str = "<h1> Quotes </h1> Tiki Taka, Jogo Bonito, Champagne, Pim Pam toma lacasitos"

    return quote

#2 run
if __name__ == "__main__":
    app.run(debug=True)