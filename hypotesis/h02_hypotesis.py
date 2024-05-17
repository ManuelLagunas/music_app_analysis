# Libraries ---------------------------------------- 
import pandas as pd
import os, sys
sys.path.append(os.getcwd())
# Esto es para agregar al path la ruta de ejecución actual y poder importar respecto a la ruta del proyecto, desde donde se debe ejecutar el código

# Loading data ---------------------------------------- 
df = pd.read_csv("files/datasets/intermediate/a02_preprossesing.csv")

# Study dataframes ------------------------------------
# ------------ cities separation ----------------
spr_general=df[df['city']=='Springfield']
print(spr_general)
print()

shel_general=df[df['city']=='Shelbyville']
print(shel_general)

# Study function ------------------------------------
def genre_weekday(df,day,time1,time2):
    genre_df = df[(df['day']==day) & (df['time']<time2) & (df['time']>time1)]
    genre_df_count = genre_df.groupby('genre')['genre'].count()
    genre_df_sorted = genre_df_count.sort_values(ascending=False)
    return genre_df_sorted[:15]

# Calculations ------------------------------------
spr_mond_mor=genre_weekday(spr_general,'Monday','07:00:00','11:00:00')
print(spr_mond_mor)
print()

shel_mond_mor=genre_weekday(shel_general,'Monday','07:00:00','11:00:00')
print(shel_mond_mor)
print()

spr_frid_eve=genre_weekday(spr_general,'Friday','17:00:00','23:00:00')
print(spr_frid_eve)
print()

shel_frid_eve=genre_weekday(shel_general,'Friday','17:00:00','23:00:00')
print(shel_frid_eve)

# summary data ---------------------------------------
# Convert Series to DataFrames
spr_mond_mor_df = spr_mond_mor.to_frame().rename(columns={'genre': 'springfield_monday'}).reset_index()
shel_mond_mor_df = shel_mond_mor.to_frame().rename(columns={'genre': 'shelbyville_monday'}).reset_index()
spr_frid_eve_df = spr_frid_eve.to_frame().rename(columns={'genre': 'springfield_friday'}).reset_index()
shel_frid_eve_df = shel_frid_eve.to_frame().rename(columns={'genre': 'shelbyville_friday'}).reset_index()

# Merge DataFrames
merged_df = spr_mond_mor_df.merge(shel_mond_mor_df, on='genre', how='outer')
merged_df = merged_df.merge(spr_frid_eve_df, on='genre', how='outer')
merged_df = merged_df.merge(shel_frid_eve_df, on='genre', how='outer')

# Save data ----------------------------------------
merged_df.to_csv("files/datasets/output/h02_hypotesis.csv", index=False)