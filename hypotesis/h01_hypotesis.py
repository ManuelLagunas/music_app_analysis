# Libraries ---------------------------------------- 

import pandas as pd
import os, sys
sys.path.append(os.getcwd())
# Esto es para agregar al path la ruta de ejecución actual y poder importar respecto a la ruta del proyecto, desde donde se debe ejecutar el código

# Loading data ---------------------------------------- 
df = pd.read_csv("files/datasets/intermediate/a02_preprossesing.csv")

# Study dataframes ------------------------------------
# ---------------- plays by city -------------------
group_by_city_tracknumbers=df.groupby(by='city')['track'].count()
print(group_by_city_tracknumbers)

# --------------- plays by day of the week ------------------
group_by_day_tracknumbers=df.groupby(by='day')['track'].count()
print(group_by_day_tracknumbers)

# Study function ------------------------------------
def number_tracks(day,city):
    track_list=df[(df['day']==day) & (df['city']==city)]
    track_list_count = track_list['userid'].count()
    return track_list_count

# Calculation ------------------------------------
springfield_monday = number_tracks('Monday','Springfield')
# print(springfield_monday)

shelbyville_monday = number_tracks('Monday','Shelbyville')
# print(shelbyville_monday)

springfield_wednesday = number_tracks('Wednesday','Springfield')
# print(springfield_wednesday)

shelbyville_wednesday = number_tracks('Wednesday','Shelbyville')
# print(shelbyville_wednesday)

springfield_friday = number_tracks('Friday','Springfield')
# print(springfield_friday)

shelbyville_friday = number_tracks('Friday','Shelbyville')
# print(shelbyville_friday)

# Summary table ------------------------------------
headers=['ciy','monday','wednesday','friday']
results_day_city=[
                 ['Springfield',springfield_monday,springfield_wednesday,springfield_friday],
                 ['Shelbyville',shelbyville_monday,shelbyville_wednesday,shelbyville_friday]
]
df_day_city=pd.DataFrame(data=results_day_city, columns=headers)
print(df_day_city)

# Save data ----------------------------------------
df_day_city.to_csv("files/datasets/output/h01_hypotesis.csv", index=False)