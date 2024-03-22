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

#Information seeking

inf_1 = df_1["64. Actualmente Leo (o me intereso por programas de televisión o radio) sobre enfermedades físicas graves"]
inf_1 = inf_1.drop(inf_1.index[[0]])
inf_1 = np.array(inf_1, dtype=float)

#Somatization

som_1 = df_1["62. Actualmente Creo que padezco alguna enfermedad física grave (aunque no me la han confirmado)"]
som_1 = som_1.drop(som_1.index[[0]])
som_1 = np.array(som_1, dtype=float)


a0     = np.mean( inf_1 )
a1     = np.median( inf_1 )
result = stats.mode( inf_1 ) # mode(s) and count(s)
a2     = result.mode

b0     = np.mean( som_1 )
b1     = np.median( som_1  )
result = stats.mode( som_1  ) # mode(s) and count(s)
b2     = result.mode





plt.figure()

plt.subplot(1,2,1)
plt.hist(inf_1, bins=10)
plt.axvline(a0, color='r', label='Mean')
plt.axvline(a1, color='g', label='Median')
plt.axvline(a2, color='k', label='Mode')
plt.legend()
plt.xlabel('Score for information seeking Q.64')
plt.ylabel('Number of calls')
plt.title("Figure 23")

plt.subplot(1,2,2)
plt.hist(som_1, bins=10)
plt.axvline(b0, color='r', label='Mean')
plt.axvline(b1, color='g', label='Median')
plt.axvline(b2, color='k', label='Mode')
plt.legend()
plt.xlabel('Score for somatization Q.62')
plt.ylabel('Number of calls')
plt.title("Figure 24")


plt.tight_layout()

plt.show()
