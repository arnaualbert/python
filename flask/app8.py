from crypt import methods
from flask import Flask, Response, render_template,request

# parametros por ruta

#1 inicializacion
module_name = __name__
app: Flask = Flask(__name__)

#3 rutas
@app.route("/", methods=['GET','POST'])
def index():

    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass

    return ''


#2 run
if __name__ == "__main__":
    app.run(debug=True)