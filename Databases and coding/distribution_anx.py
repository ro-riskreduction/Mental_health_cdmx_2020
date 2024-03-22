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

#Anxiety

anx_1 = df_1["54 Durante las últimas 2 semanas Me he sentido nerviosa(o), ansiosa(o) o con los nervios de punta"]
anx_1 = anx_1.drop(anx_1.index[[0]])
anx_1 = np.array(anx_1, dtype=float)

anx_2 = df_1["55 Durante las últimas 2 semanas Me he sentido incapaz de controlar mis preocupaciones"]
anx_2 = anx_2.drop(anx_2.index[[0]])
anx_2 = np.array(anx_2, dtype=float)

anx_3 = df_1["56 Durante las últimas 2 semanas Me he sentido tan inquieta(o) que no he podido quedarme quieta(o)"]
anx_3 = anx_3.drop(anx_3.index[[0]])
anx_3 = np.array(anx_3, dtype=float)

anx_4 = df_1["57 Durante las últimas 2 semanas He tenido dificultad para relajarme"]
anx_4 = anx_4.drop(anx_4.index[[0]])
anx_4 = np.array(anx_4, dtype=float)

anx_5 = df_1["67 Durante las últimas 2 semanas Siento poco interés o placer en hacer cosas"]
anx_5 = anx_5.drop(anx_5.index[[0]])
anx_5 = np.array(anx_5, dtype=float)

anx_6 = df_1["68Durante las últimas 2 semanas Me he sentido decaída(o) deprimida(o) o sin esperanzas"]
anx_6 = anx_6.drop(anx_6.index[[0]])
anx_6 = np.array(anx_6, dtype=float)



a0     = np.mean( anx_1 )
a1     = np.median( anx_1 )
result = stats.mode( anx_1 ) # mode(s) and count(s)
a2     = result.mode

b0     = np.mean( anx_2 )
b1     = np.median( anx_2 )
result = stats.mode( anx_2 ) # mode(s) and count(s)
b2     = result.mode

c0     = np.mean( anx_3 )
c1     = np.median( anx_3 )
result = stats.mode( anx_3 ) # mode(s) and count(s)
c2     = result.mode

d0     = np.mean( anx_4 )
d1     = np.median( anx_4 )
result = stats.mode( anx_4 ) # mode(s) and count(s)
d2     = result.mode

e0     = np.mean( anx_5 )
e1     = np.median( anx_5 )
result = stats.mode( anx_5 ) # mode(s) and count(s)
e2     = result.mode

f0     = np.mean( anx_6 )
f1     = np.median( anx_6 )
result = stats.mode( anx_6 ) # mode(s) and count(s)
f2     = result.mode



plt.figure()

plt.subplot(2,3,1)
plt.hist(anx_1, bins=10)
plt.axvline(a0, color='r', label='Mean')
plt.axvline(a1, color='g', label='Median')
plt.axvline(a2, color='k', label='Mode')
plt.legend()
plt.xlabel('Score for anxiety Q.54')
plt.ylabel('Number of calls')
plt.title("Figure 2")

plt.subplot(2,3,2)
plt.hist(anx_2, bins=10)
plt.axvline(b0, color='r', label='Mean')
plt.axvline(b1, color='g', label='Median')
plt.axvline(b2, color='k', label='Mode')
plt.legend()
plt.xlabel('Score for anxiety Q.55')
plt.ylabel('Number of calls')
plt.title("Figure 3")

plt.subplot(2,3,3)
plt.hist(anx_3, bins=10)
plt.axvline(c0, color='r', label='Mean')
plt.axvline(c1, color='g', label='Median')
plt.axvline(c2, color='k', label='Mode')
plt.legend()
plt.xlabel('Score for anxiety Q. 56')
plt.ylabel('Number of calls')
plt.title("Figure 4")

plt.subplot(2,3,4)
plt.hist(anx_4, bins=10)
plt.axvline(d0, color='r', label='Mean')
plt.axvline(d1, color='g', label='Median')
plt.axvline(d2, color='k', label='Mode')
plt.legend()
plt.xlabel('Score for anxiety Q. 57')
plt.ylabel('Number of calls')
plt.title("Figure 5")

plt.subplot(2,3,5)
plt.hist(anx_5, bins=10)
plt.axvline(e0, color='r', label='Mean')
plt.axvline(e1, color='g', label='Median')
plt.axvline(e2, color='k', label='Mode')
plt.legend()
plt.xlabel('Score for anxiety Q. 67')
plt.ylabel('Number of calls')
plt.title("Figure 6")

plt.subplot(2,3,6)
plt.hist(anx_6, bins=10)
plt.axvline(f0, color='r', label='Mean')
plt.axvline(f1, color='g', label='Median')
plt.axvline(f2, color='k', label='Mode')
plt.legend()
plt.xlabel('Score for anxiety Q. 68')
plt.ylabel('Number of calls')
plt.title("Figure 7")

plt.tight_layout()

plt.show()
