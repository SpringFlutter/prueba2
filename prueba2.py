from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__, template_folder='')

# Conexion a la base de datos dbDatos en la nube
app.config['MONGO_URI'] = 'mongodb+srv://projectspring85:prueba123@cluster0.xqrsb1a.mongodb.net/dbDatos?retryWrites=true&w=majority'

mongo = PyMongo(app)

# Definir API GET para consumir los datos, recibira el parametro idInstitucion
@app.route('/api/datos/institucion/<string:idInstitucion>', methods=['GET'])
def get_data(idInstitucion):
    data = list(mongo.db.docInstitucion.find({'institucion_id':idInstitucion}, {'_id': 0}))
    # Se imprime los datos
    print(data)
    # Se regresa los datos en una pagina.html
    if data:
        return render_template('pagina.html', data=data)
    else:
        return render_template('pagina.html', message='sin datos')

if __name__ == '__main__':
    app.run('127.0.0.1', port=5000)
