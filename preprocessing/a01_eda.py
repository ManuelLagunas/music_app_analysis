# Libreries ---------------------------------------- 

import pandas as pd
import os, sys
sys.path.append(os.getcwd()) # Esto es para agregar al path la ruta de ejecución actual y poder importar respecto a la ruta del proyecto, desde donde se debe ejecutar el código

# Loading data ---------------------------------------- 
df_raw = pd.read_csv("files/datasets/input/music_project_en.csv")

# Data exploration ---------------------------------------- 

# Basic exploration
print(df_raw.sample(10))
print()
print(df_raw.shape)
print()
print(df_raw.info())
print()
print(df_raw.describe())

# Null values
print(df_raw.isnull().sum())
print()
print((df_raw.isnull().sum() / len(df_raw)) * 100)
print()

# duplicate values
df_raw.duplicated().sum()
print()

# Non explicit duplicated data
print(sorted(df['genre'].unique()))