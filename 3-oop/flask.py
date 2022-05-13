from flask import Flask
app = Flask(__name__)

@app.route("/")
def holamundo():
    return "¡Hola Mundo!"

app.run(port=5000)