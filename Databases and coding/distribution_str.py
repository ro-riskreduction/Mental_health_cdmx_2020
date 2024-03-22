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


#Stress

str_1 = df_1["37. En el último mes Pienso o imagino, repetidamente, que voy a enfermar"]
str_1 = str_1.drop(str_1.index[[0]])
str_1 = np.array(str_1, dtype=float)

str_2 = df_1["38. En el último mes Tengo pesadillas que se repiten acerca de la enfermedad"]
str_2 = str_2.drop(str_2.index[[0]])
str_2 = np.array(str_2, dtype=float)

str_3 = df_1["39 En el último mes Me siento preocupada(o) cuando se menciona la enfermedad"]
str_3 = str_3.drop(str_3.index[[0]])
str_3 = np.array(str_3, dtype=float)

str_4 = df_1["40 En el último mes Tengo reacciones físicas desagradable cuando pienso en la enfermedad (por ejemplo, latidos cardiacos muy fuertes, problemas para respirar, sudoración)"]
str_4 = str_4.drop(str_4.index[[0]])
str_4 = np.array(str_4, dtype=float)

str_5 = df_1["44 En el último mes Pienso que si me enfermo o se enferma alguien de mi familia, es por mi culpa"]
str_5 = str_5.drop(str_5.index[[0]])
str_5 = np.array(str_5, dtype=float)

str_6 = df_1["48 En el último mes Siento que mi futuro es incierto a partir de que comenzó el riesgo a padecer esta enfermedad"]
str_6 = str_6.drop(str_6.index[[0]])
str_6 = np.array(str_6, dtype=float)

str_7 = df_1["53 En el último mes Me siento asustada(o) por los riesgos a padecer esta enfermedad"]
str_7 = str_7.drop(str_7.index[[0]])
str_7 = np.array(str_7, dtype=float)



a0     = np.mean( str_1 )
a1     = np.median( str_1 )
result = stats.mode( str_1 ) # mode(s) and count(s)
a2     = result.mode

b0     = np.mean( str_2 )
b1     = np.median( str_2 )
result = stats.mode( str_2 ) # mode(s) and count(s)
b2     = result.mode

c0     = np.mean( str_3 )
c1     = np.median( str_3 )
result = stats.mode( str_3 ) # mode(s) and count(s)
c2     = result.mode

d0     = np.mean( str_4)
d1     = np.median( str_4 )
result = stats.mode( str_4 ) # mode(s) and count(s)
d2     = result.mode

e0     = np.mean( str_5 )
e1     = np.median( str_5 )
result = stats.mode( str_5 ) # mode(s) and count(s)
e2     = result.mode

f0     = np.mean( str_6 )
f1     = np.median( str_6 )
result = stats.mode( str_6 ) # mode(s) and count(s)
f2     = result.mode

g0     = np.mean( str_7 )
g1     = np.median( str_7 )
result = stats.mode( str_7 ) # mode(s) and count(s)
g2     = result.mode




plt.figure()

plt.subplot(4,2,1)
plt.hist(str_1, bins=10)
plt.axvline(a0, color='r', label='Mean')
plt.axvline(a1, color='g', label='Median')
plt.axvline(a2, color='k', label='Mode')
plt.legend()
plt.xlabel('Score for stress Q.37')
plt.ylabel('Number of calls')
plt.title("Figure 8")

plt.subplot(4,2,2)
plt.hist(str_2, bins=10)
plt.axvline(b0, color='r', label='Mean')
plt.axvline(b1, color='g', label='Median')
plt.axvline(b2, color='k', label='Mode')
plt.legend()
plt.xlabel('Score for stress Q.38')
plt.ylabel('Number of calls')
plt.title("Figure 9")

plt.subplot(4,2,3)
plt.hist(str_3, bins=10)
plt.axvline(c0, color='r', label='Mean')
plt.axvline(c1, color='g', label='Median')
plt.axvline(c2, color='k', label='Mode')
plt.legend()
plt.xlabel('Score for stress Q.39')
plt.ylabel('Number of calls')
plt.title("Figure 10")

plt.subplot(4,2,4)
plt.hist(str_4, bins=10)
plt.axvline(d0, color='r', label='Mean')
plt.axvline(d1, color='g', label='Median')
plt.axvline(d2, color='k', label='Mode')
plt.legend()
plt.xlabel('Score for stress Q.40')
plt.ylabel('Number of calls')
plt.title("Figure 11")

plt.subplot(4,2,5)
plt.hist(str_5, bins=10)
plt.axvline(e0, color='r', label='Mean')
plt.axvline(e1, color='g', label='Median')
plt.axvline(e2, color='k', label='Mode')
plt.legend()
plt.xlabel('Score for stress Q.44')
plt.ylabel('Number of calls')
plt.title("Figure 12")

plt.subplot(4,2,6)
plt.hist(str_6, bins=10)
plt.axvline(f0, color='r', label='Mean')
plt.axvline(f1, color='g', label='Median')
plt.axvline(f2, color='k', label='Mode')
plt.legend()
plt.xlabel('Score for stress Q.48')
plt.ylabel('Number of calls')
plt.title("Figure 13")

plt.subplot(4,2,7)
plt.hist(str_7, bins=10)
plt.axvline(f0, color='r', label='Mean')
plt.axvline(f1, color='g', label='Median')
plt.axvline(f2, color='k', label='Mode')
plt.legend()
plt.xlabel('Score for stress Q.53')
plt.ylabel('Number of calls')
plt.title("Figure 14")

plt.tight_layout()

plt.show()
