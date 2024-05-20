# Libraries ---------------------------------------- 
import pandas as pd
import os, sys
sys.path.append(os.getcwd())
# Esto es para agregar al path la ruta de ejecución actual y poder importar respecto a la ruta del proyecto, desde donde se debe ejecutar el código

# Loading data ---------------------------------------- 
sp = pd.read_csv("files/datasets/intermediate/h02_springfield.csv")
sh = pd.read_csv("files/datasets/intermediate/h02_shelbyville.csv")

# Study dataframes ------------------------------------
# sringfield
sp_genres = sp.groupby('genre')['genre'].count()
sp_genres = sp_genres.sort_values(ascending=False)
print(sp_genres.head(10))

#study table
sh_genres = sh.groupby('genre')['genre'].count()
sh_genres = sh_genres.sort_values(ascending=False)
print(sh_genres.head(10))

# summary data ---------------------------------------
sp_genres_df = sp_genres.to_frame().rename(columns={'genre': 'springfield'}).reset_index()
sh_genres_df = sh_genres.to_frame().rename(columns={'genre': 'shelbyville'}).reset_index()

# Concatenate horizontally
result = pd.concat([sp_genres_df, sh_genres_df], axis=1)
print(result.head(10))

# Save data ----------------------------------------
result.to_csv("files/datasets/output/h03_hypotesis.csv", index=False)