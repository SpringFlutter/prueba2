# Prueba 2

Servicio web

## Tabla de contenido

- [Prueba 2](#project-title)
  - [Tabla de contenido](#tabla-de-contenido)
  - [Requerimientos](#requerimientos)
  - [Codigo](#codigo)
  - [Uso](#uso)

### Requerimientos

Las librerias necesarias se encuentran en el archivo requirements.txt. Ademas, se necesita tener una cuenta creada en mongo atlas con una base de datos para establecer la conexion.

## Codigo

Parte 3 : en este bloque se conecta a mongo usando Flask
```python

  app = Flask(__name__, template_folder='')
  
  # Conexion a la base de datos dbDatos en la nube
  app.config['MONGO_URI'] = 'mongodb+srv://projectspring85:prueba123@cluster0.xqrsb1a.mongodb.net/dbDatos?retryWrites=true&w=majority'
  
  mongo = PyMongo(app)

```
En el siguiente bloque se define la ruta http://127.0.0.1:5000/api/datos/institucion/{idInstitucion} para filtrar los datos, imprimirlos y devolverlos en una pagina html
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
Probar el servicio abriendo el explorador e ingresando el enlace http://127.0.0.1:5000/api/datos/institucion/118, donde 118 es el id de la institucion ARCOTEL.
![GitHub Logo](resultadoweb.png)
Ademas se puede ver el ejercicio completo con resultados en el archivo prueba.ipynb
