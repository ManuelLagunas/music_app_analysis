# Libreries ---------------------------------------- 

import pandas as pd
import os, sys
sys.path.append(os.getcwd()) # Esto es para agregar al path la ruta de ejecución actual y poder importar respecto a la ruta del proyecto, desde donde se debe ejecutar el código

# Loading data ---------------------------------------- 
df_raw = pd.read_csv("files/datasets/input/music_project_en.csv")

# Data fixing __________________________________________

# -------------- Columns name -------------------------
print(df_raw.columns)
def convert_to_snake_case(df):
    df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('-', '_').str.lower()
    return df

df = convert_to_snake_case(df_raw)
print(df.columns)

# -------------- Fixing null values -------------------------
df[['track', 'artist', 'genre']] = df[['track', 'artist', 'genre']].fillna('unknown') 
print(df.isna().sum())

# -------------- Duplicated data -------------------------
df=df.drop_duplicates().reset_index(drop=True)
print(df.duplicated().sum())

# -------------- Non explicit duplicated data -------------------------
df['genre'] = df['genre'].replace(['hip', 'hop', 'hip-hop'], 'hiphop')
print(sorted(df['genre'].unique()))

# Save data ----------------------------------------
df.to_csv("files/datasets/intermediate/a02_preprossesing.csv", index=False)