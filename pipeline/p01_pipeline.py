# Libreries ----------------------------------------

import os, sys
import argparse
sys.path.append(os.getcwd()) # Esto es para agregar al path la ruta de ejecución actual y poder importar respecto a la ruta del proyecto, desde donde se debe ejecutar el código
import params as params
   
# Defining Executable File Extensions ---------------------------------------- 

if params.sistema_operativo == 'Windows':
        extension_binarios = ".exe"
else:
        extension_binarios = ""

# Preprocessing ---------------------------------------- 
print(f"---------------------------------- \nComenzando el preproceso\n----------------------------------")
os.system(f"python{extension_binarios} preprocessing/a02_preprocessing.py")
print(f"---------------------------------- \nLos datos estan listos para ser trabajados\n----------------------------------")

# firts hypotesis ---------------------------------------- 
print(f"---------------------------------- \n Primera hipotesis\n----------------------------------")
os.system(f"python{extension_binarios} hypotesis/h01_hypotesis.py")
print(f"---------------------------------- \n Puede ver las conclusiones en el archivo readme\n----------------------------------")

# second hypotesis ---------------------------------------- 
print(f"---------------------------------- \n Segunda hipotesis\n----------------------------------")
os.system(f"python{extension_binarios} hypotesis/h02_hypotesis.py")
print(f"---------------------------------- \n Puede ver las conclusiones en el archivo readme\n----------------------------------")

# third hypotesis ---------------------------------------- 
print(f"---------------------------------- \n Tercera hipotesis\n----------------------------------")
os.system(f"python{extension_binarios} hypotesis/h03_hypotesis.py")
print(f"---------------------------------- \n Puede ver las conclusiones en el archivo readme\n----------------------------------")