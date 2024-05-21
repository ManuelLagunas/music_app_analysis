# Music app analysis

# Introducción
En este proyecto, se comparan las preferencias musicales de las ciudades de Springfield y Shelbyville. Estudiando datos reales de transmisión de música online para probar las hipótesis a continuación plateadas y comparar el comportamiento de los usuarios y las usuarias de estas dos ciudades.

## Objetivo
Prueba tres hipótesis:
- La actividad de los usuarios y las usuarias difiere según el día de la semana y dependiendo de la cuidad.
- Los lunes por la mañana, los habitantes de Springfield y Shelbyville escuchan géneros distintos. Lo mismo ocurre con los viernes por la noche.
- Los oyentes de Springfield y Shelbyville tienen preferencias distintas. En Springfield prefieren el pop, mientras que en Shelbyville hay más personas a las que les gusta el rap.

## Etapas
El proyecto consistirá en tres etapas:
- Descripción de los datos
- Preprocesamiento de datos
- Prueba de hipótesis

# Instrucciones

Con la finalidad de mostrar diferentes tipos de herramientas de trabajo se han creado diferentes versiones del mismo analisis:

* Un jupyternotebook
* Un quarto markdown
* Una versión en html, generada a partir de el quarto markdown
* y una versión modularizada con scripts de python con el uso de un pipeline 

## Instrucciones jupyternotebook

* Asegurarse de que cumple con los requisitos del archivo ```'requirements.txt'```
* Correr el archivo ```music_app_analysis.ipynb```

## Instrucciones quarto markdown

* Asegurarse de que cumple con los requisitos del archivo ```'requirements.txt'```
* Correr el archivo ```music_app_analysis.qmd```

## Instrucciones html

* Abrir el archivo ```'music_app_analysis.html' en un navegador web

## Instrucciones jupyternotebook

* Asegurarse de que cumple con los requisitos del archivo ```'requirements.txt'```
* Correr el archivo ```'pipeline/p01_pipeline'```
  
### Conclusiones
* **Primera hipotesis**
* La primera hipótesis el la siguiente: La actividad de los usuarios y las usuarias difiere según el día de la semana y dependiendo de la cuidad. Para confirmarse o negarse la hipótesis se creo el Dataframe de nombre df_day_city del cual podemos concluir lo siguiente:

  - 1.Los usuarios de Spingfield escuchas mas canciones en todos los días de la semana que los usuarios de Shelbyville según los valores absolutos. Sin embargo de acuerdo a los porentajes se ven diferencias de aproximadamente un digito siendo los días lunes y viernes de mayor escucha en Springfield que en Shelbyville, solo presentandose el caso de ser mayores los oyenetes según porcentajes en Shelbyville que en Springfield

  - 2.En Sprinfield se observa que los días Lunes y viernes se escuchan casi el mismo número de canciones obsrvandose un aumento marginal el día viernes respecto al lunes y decayendo el día miercoles considerablemente

  - 3.Caso contrario en Shelbyville, donde se observa el mismo comportamiento que Springfield los días Lunes y viernes que se mantienen constantes con un aumento marginal el día viernes respecto al lunes pero siendo el día miercoles el día en que mas escuchan música los usuarios de Shelbyville.

* Por lo que podemos decir que la hipotesis es confirmada parcialmente. Siendo correcta si hablamos del día miercoles,donde en una ciudad se ve una disminución y en la otra un aumento; E incorrecta los días lunes y viernes ya que se observa el mismo comportamiento en ambas ciudades, donde solo hay un aumento marginal de canciones escuchadas el día viernes respecto al lunes.

* **Segunda hipotesis**
* La segunda hipótesis a estudiar es: Los lunes por la mañana, los habitantes de Springfield y Shelbyville escuchan géneros distintos. Lo mismo ocurre con los viernes por la noche Según los resultados obtenidos por el segundo estudio de los datos podemos concluir que:

* Aunque los generos no aparecen en el mismo orden, ambas ciudades escuchan los mismos generos los días lunes por la mañana, existiendo diferencias minimas sobre los generos que cada ciudad escucha.
  
* De igual manera. Aunque si bien no aparecen en el mismo orden podemos ver que los viernes por la tarde los usuarios de ambas ciudades escuchan los mismos 15 generos musicales
  
* Por tanto podemos decir que la hipótesis planteadea es incorrecta, ya que los datos indican que ambas ciudades gustan de escuchar los mismos generos.

* **Tercera hipotesis**
* La tercera hipótesis a comprobar es: Los oyentes de Springfield y Shelbyville tienen preferencias distintas. En Springfield prefieren el pop, mientras que en Shelbyville hay más personas a las que les gusta el rap.

* De acuerdo con los resultados obtenidos podemos decir que la hipótesis es parcialmente correcta ya que:
  - En primer lugar de ambas ciudades, es el genero pop, por lo que la hipotesis es correcta en el caso de Springfield e incorrecta en el caso de Shelbyville que aseguraba que el genero preferido era rap
  - El genero rap no aparece como de los mas escuchados en la lista del top 10 de Shelbyville concluyendo entonces que la segunda parte de la hipótesis es incorrecta.

# Conclusiones
* 1.La actividad de los usuarios y las usuarias difiere según el día de la semana y dependiendo de la cuidad. Es correcta parcialmente, ya que en ambas ciudades de observo el mismo comportamiento los días lunes y viernes observandose un cambio significativo solo los días miercoles.

* 2.Los lunes por la mañana, los habitantes de Springfield y Shelbyville escuchan géneros distintos. Lo mismo ocurre con los viernes por la noche. Los resultados arrojaron que ambas ciudades escuchan los mismos generos en ambos días y momentos por lo que la hipótesis es incorrecta.

* 3.Los oyentes de Springfield y Shelbyville tienen preferencias distintas. En Springfield prefieren el pop, mientras que en Shelbyville hay más personas a las que les gusta el rap. La hipotesis es parcialmente correcta, ya que ambos gustan del pop como genero principal

## Por tomar en cuenta
En proyectos de investigación reales, la prueba de hipótesis estadística es más precisa y cuantitativa. También se debe tomar en cuenta que no siempre se pueden sacar conclusiones sobre una ciudad entera a partir de datos de una sola fuente.