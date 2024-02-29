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

#Distancing

dis_1 = df_1["45. En el último mes He perdido interés por las actividades que antes disfrutaba"]
dis_1 = dis_1.drop(dis_1.index[[0]])
dis_1 = np.array(dis_1, dtype=float)

dis_2 = df_1["46. En el último mes Me siento distante de las personas con quienes convivo, a partir de que inició el riesgo de esta enfermedad"]
dis_2 = dis_2.drop(dis_2.index[[0]])
dis_2 = np.array(dis_2, dtype=float)

dis_3 = df_1["49. En el último mes Siento que deseo hacer cosas para hacerme daño"]
dis_3 = dis_3.drop(dis_3.index[[0]])
dis_3 = np.array(dis_3, dtype=float)

dis_4 = df_1["50. En el último mes Tengo dificultad para quedarme dormido o seguir durmiendo"]
dis_4 = dis_4.drop(dis_4.index[[0]])
dis_4 = np.array(dis_4, dtype=float)

dis_5 = df_1["51. En el último mes Me siento enojada (o)"]
dis_5 = dis_5.drop(dis_5.index[[0]])
dis_5 = np.array(dis_5, dtype=float)



a0     = np.mean( dis_1 )
a1     = np.median( dis_1 )
result = stats.mode( dis_1 ) # mode(s) and count(s)
a2     = result.mode

b0     = np.mean( dis_2 )
b1     = np.median( dis_2 )
result = stats.mode( dis_2 ) # mode(s) and count(s)
b2     = result.mode

c0     = np.mean( dis_3 )
c1     = np.median( dis_3 )
result = stats.mode( dis_3 ) # mode(s) and count(s)
c2     = result.mode

d0     = np.mean( dis_4)
d1     = np.median( dis_4 )
result = stats.mode( dis_4 ) # mode(s) and count(s)
d2     = result.mode

e0     = np.mean( dis_5 )
e1     = np.median( dis_5 )
result = stats.mode( dis_5 ) # mode(s) and count(s)
e2     = result.mode




plt.figure()

plt.subplot(2,3,1)
plt.hist(dis_1, bins=5)
plt.axvline(a0, color='r', label='Mean')
plt.axvline(a1, color='g', label='Median')
plt.axvline(a2, color='k', label='Mode')
plt.legend()
plt.xlabel('Score for distancing Q.45')
plt.ylabel('Number of calls')
plt.title("Figure 18")

plt.subplot(2,3,2)
plt.hist(dis_2, bins=5)
plt.axvline(b0, color='r', label='Mean')
plt.axvline(b1, color='g', label='Median')
plt.axvline(b2, color='k', label='Mode')
plt.legend()
plt.xlabel('Score for distancing Q.46')
plt.ylabel('Number of calls')
plt.title("Figure 19")

plt.subplot(2,3,3)
plt.hist(dis_3, bins=5)
plt.axvline(c0, color='r', label='Mean')
plt.axvline(c1, color='g', label='Median')
plt.axvline(c2, color='k', label='Mode')
plt.legend()
plt.xlabel('Score for distancing Q.49')
plt.ylabel('Number of calls')
plt.title("Figure 20")

plt.subplot(2,3,4)
plt.hist(dis_4, bins=5)
plt.axvline(d0, color='r', label='Mean')
plt.axvline(d1, color='g', label='Median')
plt.axvline(d2, color='k', label='Mode')
plt.legend()
plt.xlabel('Score for distancing Q.50')
plt.ylabel('Number of calls')
plt.title("Figure 21")

plt.subplot(2,3,5)
plt.hist(dis_5, bins=5)
plt.axvline(e0, color='r', label='Mean')
plt.axvline(e1, color='g', label='Median')
plt.axvline(e2, color='k', label='Mode')
plt.legend()
plt.xlabel('Score for distancing Q.51')
plt.ylabel('Number of calls')
plt.title("Figure 22")

plt.tight_layout()

plt.show()