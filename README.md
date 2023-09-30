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

Parte 1 : en este bloque de codigo realizamos un solicitud GET para obtener los datos de las instituciones finacieras
```python
    url = 'https://www.gob.ec/api/v1/instituciones'
    headers = {'User-agent': 'Chrome/58.0.3029.110'}

    # Realizar una solicitud GET
    response = requests.get(url=url, headers=headers)

    # Verificar si la solicitud fue exitosa (código de respuesta 200)
    if response.status_code == 200:
        # Convertir la respuesta a formato JSON
        data = response.json()

        primer_resultado = data[0]

        for resultado in data:
            # Iterar a través de las claves (campos) en el objeto
            for campo, valor in primer_resultado.items():
                # Imprimir el nombre del campo y su valor
                print(f"{campo}: {valor}")

    else:
        print(f'Error al hacer la solicitud. Código de respuesta: {response.status_code}')
```
Parte 2: en este bloque almacenamos los datos obtenidos en una base datos mongodb en la nube
```python
    # Cadena de conexion a la base de datos en la nube
    connection_string = "mongodb+srv://projectspring85:prueba123@cluster0.xqrsb1a.mongodb.net/?retryWrites=true&w=majority"

    # Se abre una conexion a la base de datos dbDatos en la coleccion docInstitucion
    client = pymongo.MongoClient(connection_string)
    db = client["dbDatos"]
    collection = db["docInstitucion"]

    # Se insertan los datos
    result = collection.insert_many(data)

    # Se imprime los ID de documentos insertados
    print("Documentos insertados IDs:", result.inserted_ids)

    # Se cierra la conexion
    client.close()
```

## Uso
Instalar las librerias necesarias
```python
pip install -r requirements.txt
```
Correr el codigo

```python
python3 prueba.py
```
