# Pipeline

# Music app analysis

## Fuente de Informacion

```'files/datasets/intermediate/a02_preprocessing.csv'```

## Parámetros
Los parametros ya estan definidos para este estudio

## Paso 01

**a02_preprocessing.py**
```
'/preprocessing/a02_preprocessing.py'
```

**Descripcion:**
* Script para arreglar los problemas detectados en la fase de analisis exploratorio de datos

**Chunks:**
* Leer y crear el dataframe
* Ajustar el nombre de las columnas a la convencion snake_case
* Arreglar los valores nulos
* Eliminar duplicados explicitos
* Arreglar duplicados implicitos

## Paso 02

**h01_hypotesis.py**
```
'/hypotesis/h01_hypotesis.py'
```

**Descripcion:**
* Script que genera un dataframe que estudia el numero de reproducciones de ambas ciudades los dias lunes, miercoles y viernes

**Chunks:**
* Leer y crear el dataframe
* Función que toma como parametros el día y la ciudad y filtra los datos en el dataframe
* Filtrado de los datos
* Creación de un dataframe de resumen
* Guardado de los resultados en la ruta ```'files/datasets/output/h01_hypotesis.py'```

## Paso 03

**h02_hypotesis.py**
```
'/hypotesis/h02_hypotesis.py'
```

**Descripcion:**
* Script que genera un dataframe que estudia el numero de reproducciones de ambas ciudades los dias lunes, por la mañana y los viernes por la tarde

**Chunks:**
* Leer y crear el dataframe
* Creacion de dataframes por ciudad
* Guardado de los resultados en la ruta ```'files/datasets/intermediate/h02_shelbyville.py'```
* Guardado de los resultados en la ruta ```'files/datasets/intermediate/h02_springfield.py'```
* Función que toma como parametros el día y una hora de inicio y hora final para poder filtrar los datos del dataframe de la ciudad correspondiente
* Filtrado de los datos
* Creación de un dataframe de resumen
* Guardado de los resultados en la ruta ```'files/datasets/output/h02_hypotesis.py'```

## Paso 04

**h03_hypotesis.py**
```
'/hypotesis/h03_hypotesis.py'
```

**Descripcion:**
* Script que genera un dataframe con los 15 genreros mas escuchados por ciudad con la finalidad de ver si son los mismos o difieren de ciudad a ciudad

**Chunks:**
* Leer y crear el dataframe para este estudio se utilizan ```'files/datasets/intermediate/h02_shelbyville.py'``` y ```'files/datasets/intermediate/h02_springfield.py'```
* se agrupan los datos mediante grouby segun el genero y se cuentan el numero de reproducciones por cada dataframe de las ciudades
* Creación de un dataframe de resumen
* Guardado de los resultados en la ruta ```'files/datasets/output/h03_hypotesis.py'```