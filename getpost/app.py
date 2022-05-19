from crypt import methods
from flask import Flask, Response, render_template,request
from pathlib import Path

# parametros por ruta

#1 inicializacion
module_name = __name__
app: Flask = Flask(__name__)
root_path : Path = Path(app.root_path) # importante

#3 rutas
@app.route("/", methods=['GET','POST'])
def index():

    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        comic : str = request.form['comic']
        volume : int = request.form['volumen']
        return f'you have bought {comic} volume {volume}'
    return ''

#2 run
if __name__ == "__main__":
    app.run(debug=True)