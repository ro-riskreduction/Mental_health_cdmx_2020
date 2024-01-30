import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

#retrieve the dataframes with parsed dates
df_1 = pd.read_csv("analysis_clean.csv", parse_dates= ["fecha"] )
df_2 = pd.read_csv("Registros por dia.csv", parse_dates=["fecha"])

#df_1 = pd.read_excel(r"analysis_clean.xlsx", parse_dates= ["fecha"] )
#df_2 = pd.read_excel(r"Registros por dia.xlsx", parse_dates=["fecha"])
#df_3 = pd.read_excel(r"Mobility_google_cdmx_2020.xlsx")
#df_4 = pd.read_excel(r'Defunciones cdmx.xlsx')
#df_5 = pd.read_csv('GT_Noticias.csv')
#df_6 = pd.read_csv('GT_Busqueda_Web.csv')

df_1.set_index("fecha")
df_2.set_index("fecha")
#I will select the vectors for each quality and convert them to a numpy array

#Avoidance

avo_1 = df_1["41.En el último mes Evito pensar, sentir o hablar sobre la enfermedad"]
avo_1 = avo_1.drop(avo_1.index[[0]])
avo_1 = np.array(avo_1, dtype=float)

avo_2 = df_1["42. En el último mes Evito ver o recurrir a información oficial sobre la enfermedad"]
avo_2 = avo_2.drop(avo_2.index[[0]])
avo_2 = np.array(avo_2, dtype=float)

avo_3 = df_1["43. En el último mes Tengo dificultad para recordar lo que recomiendan las autoridades para enfrentar el riesgo o la enfermedad"]
avo_3 = avo_3.drop(avo_3.index[[0]])
avo_3 = np.array(avo_3, dtype=float)

#Measure lines

a0     = np.mean( avo_1 )
a1     = np.median( avo_1 )
result = stats.mode( avo_1 ) # mode(s) and count(s)
a2     = result.mode

b0     = np.mean( avo_2 )
b1     = np.median( avo_2 )
result = stats.mode( avo_2 ) # mode(s) and count(s)
b2     = result.mode

c0     = np.mean( avo_3 )
c1     = np.median( avo_3 )
result = stats.mode( avo_3 ) # mode(s) and count(s)
c2     = result.mode



plt.figure()

plt.subplot(1,3,1)
plt.hist(avo_1, bins=5)
plt.axvline(a0, color='r', label='Mean')
plt.axvline(a1, color='g', label='Median')
plt.axvline(a2, color='k', label='Mode')
plt.legend()
plt.xlabel('Score for avoidance Q. 41')
plt.ylabel('Number of calls')

plt.subplot(1,3,2)
plt.hist(avo_2, bins=5)
plt.axvline(b0, color='r', label='Mean')
plt.axvline(b1, color='g', label='Median')
plt.axvline(b2, color='k', label='Mode')
plt.legend()
plt.xlabel('Score for avoidance Q. 42')
plt.ylabel('Number of calls')

plt.subplot(1,3,3)
plt.hist(avo_3, bins=5)
plt.axvline(c0, color='r', label='Mean')
plt.axvline(c1, color='g', label='Median')
plt.axvline(c2, color='k', label='Mode')
plt.legend()
plt.xlabel('Score for avoidance Q. 43')
plt.ylabel('Number of calls')


plt.tight_layout()

plt.show()
