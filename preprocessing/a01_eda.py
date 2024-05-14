# Librerias ---------------------------------------- 

import pandas as pd
import os, sys
sys.path.append(os.getcwd()) # Esto es para agregar al path la ruta de ejecución actual y poder importar respecto a la ruta del proyecto, desde donde se debe ejecutar el código

# Loading data ---------------------------------------- 
df_raw = pd.read_csv("files/datasets/input/music_project_en.csv")

# Data exploration ---------------------------------------- 

df_raw.sample(10)
df_raw.shape
df_raw.info()
df_raw.describe()
# Null values
df_raw.isnull().sum()
(df_raw.isnull().sum() / len(df_raw)) * 100
# duplicate values
df_raw.duplicated().sum()


