import csv
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import preprocessing
from sklearn.decomposition import PCA

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

#this is for the second data base

enterqueue = df_2["Enterqueue"]
enterqueue = enterqueue.drop(enterqueue.index[[0]])
enterqueue = np.array(enterqueue, dtype=float)

connect = df_2["Connect"]
connect = connect.drop(connect.index[[0]])
connect = np.array(connect, dtype=float)


abandon = df_2["Abandon"]
abandon = abandon.drop(abandon.index[[0]])
abandon = np.array(abandon, dtype=float)


connected_waiting_time = df_2["Conectado - Tiempo de espera"]
connected_waiting_time = connected_waiting_time.drop(connected_waiting_time.index[[0]])
connected_waiting_time = np.array(connected_waiting_time, dtype=float)


abandon_waiting_time = df_2["Abandono - Tiempo de espera"]
abandon_waiting_time = abandon_waiting_time.drop(abandon_waiting_time.index[[0]])
abandon_waiting_time = np.array(abandon_waiting_time, dtype=float)


call_duration = df_2["Tiempo en llamada"]
call_duration = call_duration.drop(call_duration.index[[0]])
call_duration = np.array(call_duration, dtype=float)

lifeline_array = np.vstack( (enterqueue, connect, abandon, connected_waiting_time, abandon_waiting_time, call_duration ) ).T

enter_dur_wtc_graph_3d = np.vstack ( (enterqueue, call_duration, connected_waiting_time ) ).T

lifeline_pca = np.vstack( (enterqueue,connect, abandon, connected_waiting_time, abandon_waiting_time, call_duration ) ).T



pca = PCA(n_components=6)
pca.fit(lifeline_pca)
print( pca )
print()
pc0 = pca.components_[0]
pc1 = pca.components_[1]
pc2 = pca.components_[2]
pc3 = pca.components_[3]
pc4 = pca.components_[4]
pc5 = pca.components_[5]


print( f'First PC  : {pc0}')
print( f'Second PC : {pc1}')
print( f'3 PC      : {pc2}')
print( f'4 PC      : {pc3}')
print( f'5 PC      : {pc4}')
print( f'6 PC      : {pc5}')
print( pca.n_samples_ )
print()


print("Explained variance ratio")
print( pca.explained_variance_ratio_ )

