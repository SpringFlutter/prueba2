# Prueba 1

Servicio web

## Tabla de contenido

- [Prueba 1](#project-title)
  - [Tabla de contenido](#tabla-de-contenido)
  - [Requerimientos](#requerimientos)
  - [Codigo](#codigo)
  - [Uso](#uso)

### Requerimientos

Las librerias necesarias se encuentran en el archivo requirements.txt.

### Fuente de datos
La fuente de datos a utilizar sera la proporcionada por API Gob.Ec, la cual contiene datos que se generan en las instituciones públicas del ecuador.
Para mayor informacion y sus metodos de uso visitar en el siguiente enlace: https://www.gob.ec/api

## Codigo

Parte 1 : en este bloque se conecta a mongo usando Flask
```python

  app = Flask(__name__, template_folder='')
  
  # Conexion a la base de datos dbDatos en la nube
  app.config['MONGO_URI'] = 'mongodb+srv://projectspring85:prueba123@cluster0.xqrsb1a.mongodb.net/dbDatos?retryWrites=true&w=majority'
  
  mongo = PyMongo(app)

```
Parte 2: en este bloque se define la ruta http://127.0.0.1:5000/api/datos/institucion/{idInstitucion} para filtrar los datos, imprimirlos y devolverlos en una pagina html
```python
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
```

## Uso
Instalar las librerias necesarias
```python
pip install -r requirements.txt
```
Correr el codigo

```python
python3 prueba2.py
```
