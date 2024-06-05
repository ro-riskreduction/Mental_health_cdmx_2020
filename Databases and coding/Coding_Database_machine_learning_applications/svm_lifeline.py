import csv
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from mpl_toolkits import mplot3d
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
import sklearn.metrics
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn import neighbors, svm, preprocessing
from sklearn.preprocessing import RobustScaler
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score
import datetime as dt

#retrieve the dataframes with parsed dates

#df_1 = pd.read_csv("analysis_clean.csv", parse_dates= ["fecha"] )
df_2 = pd.read_csv("Registros por dia.csv", parse_dates=["fecha"])

#df_1 = pd.read_excel(r"analysis_clean.xlsx", parse_dates= ["fecha"] )
#df_2 = pd.read_excel(r"Registros por dia.xlsx", parse_dates=["fecha"])
#df_3 = pd.read_excel(r"Mobility_google_cdmx_2020.xlsx")
#df_4 = pd.read_excel(r'Defunciones cdmx.xlsx')
#df_5 = pd.read_csv('GT_Noticias.csv')
#df_6 = pd.read_csv('GT_Busqueda_Web.csv')

#df_1.set_index("fecha")
df_2.set_index("fecha")
#I will select the vectors for each quality and convert them to a numpy array

#

#prepared the dates data type

#date_1 = df_1["fecha"]
#date_1 = date_1.drop(date_1.index[[0]])

date_2 = df_2["fecha"]
date_2 = date_2.drop(date_2.index[[0]])

df_2['fecha_ordinal']= df_2['fecha'].map(dt.datetime.toordinal)
fecha_ord = df_2['fecha_ordinal']
fecha_ord = fecha_ord.drop(fecha_ord.index[[0]])
fecha_ord_array = np.array(fecha_ord, dtype=float)

#correct times_3 (deleted corresponding to df_1)
###################################################################################
measures_2_ll = (df_2["fecha"] >= "5/29/2020" ) & (df_2["fecha"] <= "6/4/2020" )
measures_2_ll = df_2[measures_2_ll]

earth_vs_1_ll = (df_2["fecha"] >= "6/20/2020" ) & (df_2["fecha"] <= "6/26/2020" )
earth_vs_1_ll = df_2[earth_vs_1_ll]

anounc_3_ll = (df_2["fecha"] >= "6/24/2020" ) & (df_2["fecha"] <= "7/1/2020" )
anounc_3_ll = df_2[anounc_3_ll]

measures_3_ll = (df_2["fecha"] >= "6/28/2020" ) & (df_2["fecha"] <= "7/4/2020" )
measures_3_ll = df_2[measures_3_ll]

prom_2_ll = (df_2["fecha"] >= "7/24/2020" ) & (df_2["fecha"] <= "7/30/2020" )
prom_2_ll = df_2[prom_2_ll]

fest_2_ll = (df_2["fecha"] >= "9/13/2020" ) & (df_2["fecha"] <= "9/19/2020" )
fest_2_ll = df_2[fest_2_ll]

prom_3_ll = (df_2["fecha"] >= "9/17/2020" ) & (df_2["fecha"] <= "9/23/2020" )
prom_3_ll = df_2[prom_3_ll]

prom_4_ll = (df_2["fecha"] >= "11/23/2020" ) & (df_2["fecha"] <= "11/29/2020" )
prom_4_ll = df_2[prom_4_ll]

fest_3_ll = (df_2["fecha"] >= "12/22/2020" ) & (df_2["fecha"] <= "12/28/2020" )
fest_3_ll = df_2[fest_3_ll]

earth_l_1_ll = (df_2["fecha"] >= "3/16/2021" ) & (df_2["fecha"] <= "3/22/2021" )
earth_l_1_ll = df_2[earth_l_1_ll]

earth_vs_2_ll = (df_2["fecha"] >= "9/4/2021" ) & (df_2["fecha"] <= "9/10/2021" )
earth_vs_2_ll = df_2[earth_vs_2_ll]

earth_l_2_ll = (df_2["fecha"] >= "2/28/2022" ) & (df_2["fecha"] <= "3/6/2022" )
earth_l_2_ll = df_2[earth_l_2_ll]

earth_l_3_ll = (df_2["fecha"] >= "3/15/2022" ) & (df_2["fecha"] <= "3/21/2022" )
earth_l_3_ll = df_2[earth_l_3_ll]

earth_l_4_ll = (df_2["fecha"] >= "8/9/2022" ) & (df_2["fecha"] <= "8/15/2022" )
earth_l_4_ll = df_2[earth_l_4_ll]

earth_vs_3_ll = (df_2["fecha"] >= "9/16/2022" ) & (df_2["fecha"] <= "9/22/2022" )
earth_vs_3_ll = df_2[earth_vs_3_ll]

earth_s_1_ll = (df_2["fecha"] >= "9/19/2022" ) & (df_2["fecha"] <= "9/25/2022" )
earth_s_1_ll = df_2[earth_s_1_ll]

earth_m_1_ll = (df_2["fecha"] >= "12/8/2022" ) & (df_2["fecha"] <= "12/14/2022" )
earth_m_1_ll = df_2[earth_m_1_ll]

earth_m_2_ll = (df_2["fecha"] >= "3/31/2023" ) & (df_2["fecha"] <= "4/6/2023" )
earth_m_2_ll = df_2[earth_m_2_ll]

########################################################################################
#pre_date_of_event


measures_2_ll_pre = (df_2["fecha"] >= "5/29/2020" ) & (df_2["fecha"] <= "5/31/2020" )
measures_2_ll_pre = df_2[measures_2_ll_pre]

earth_vs_1_ll_pre = (df_2["fecha"] >= "6/20/2020" ) & (df_2["fecha"] <= "6/22/2020" )
earth_vs_1_ll_pre = df_2[earth_vs_1_ll_pre]

anounc_3_ll_pre = (df_2["fecha"] >= "6/25/2020" ) & (df_2["fecha"] <= "6/27/2020" )
anounc_3_ll_pre = df_2[anounc_3_ll_pre]

measures_3_ll_pre = (df_2["fecha"] >= "6/28/2020" ) & (df_2["fecha"] <= "6/30/2020" )
measures_3_ll_pre = df_2[measures_3_ll_pre]

prom_2_ll_pre = (df_2["fecha"] >= "7/24/2020" ) & (df_2["fecha"] <= "7/26/2020" )
prom_2_ll_pre = df_2[prom_2_ll_pre]

fest_2_ll_pre = (df_2["fecha"] >= "9/13/2020" ) & (df_2["fecha"] <= "9/15/2020" )
fest_2_ll_pre = df_2[fest_2_ll_pre]

prom_3_ll_pre = (df_2["fecha"] >= "9/17/2020" ) & (df_2["fecha"] <= "9/19/2020" )
prom_3_ll_pre = df_2[prom_3_ll_pre]

prom_4_ll_pre = (df_2["fecha"] >= "11/23/2020" ) & (df_2["fecha"] <= "11/25/2020" )
prom_4_ll_pre = df_2[prom_4_ll_pre]

fest_3_ll_pre = (df_2["fecha"] >= "12/22/2020" ) & (df_2["fecha"] <= "12/24/2020" )
fest_3_ll_pre = df_2[fest_3_ll_pre]

earth_l_1_ll_pre = (df_2["fecha"] >= "3/16/2021" ) & (df_2["fecha"] <= "3/18/2021" )
earth_l_1_ll_pre = df_2[earth_l_1_ll_pre]

earth_vs_2_ll_pre = (df_2["fecha"] >= "9/4/2021" ) & (df_2["fecha"] <= "9/6/2021" )
earth_vs_2_ll_pre = df_2[earth_vs_2_ll_pre]

earth_l_2_ll_pre = (df_2["fecha"] >= "2/28/2022" ) & (df_2["fecha"] <= "3/2/2022" )
earth_l_2_ll_pre = df_2[earth_l_2_ll_pre]

earth_l_3_ll_pre = (df_2["fecha"] >= "3/15/2022" ) & (df_2["fecha"] <= "3/17/2022" )
earth_l_3_ll_pre = df_2[earth_l_3_ll_pre]

earth_l_4_ll_pre = (df_2["fecha"] >= "8/9/2022" ) & (df_2["fecha"] <= "8/11/2022" )
earth_l_4_ll_pre = df_2[earth_l_4_ll_pre]

earth_vs_3_ll_pre = (df_2["fecha"] >= "9/16/2022" ) & (df_2["fecha"] <= "9/18/2022" )
earth_vs_3_ll_pre = df_2[earth_vs_3_ll_pre]

earth_s_1_ll_pre = (df_2["fecha"] >= "9/19/2022" ) & (df_2["fecha"] <= "9/21/2022" )
earth_s_1_ll_pre = df_2[earth_s_1_ll_pre]

earth_m_1_ll_pre = (df_2["fecha"] >= "12/8/2022" ) & (df_2["fecha"] <= "12/10/2022" )
earth_m_1_ll_pre = df_2[earth_m_1_ll_pre]

earth_m_2_ll_pre = (df_2["fecha"] >= "3/31/2023" ) & (df_2["fecha"] <= "4/2/2023" )
earth_m_2_ll_pre = df_2[earth_m_2_ll_pre]

######################################################################################################
#post_event


measures_2_ll_post = (df_2["fecha"] >= "6/2/2020" ) & (df_2["fecha"] <= "6/4/2020" )
measures_2_ll_post = df_2[measures_2_ll_post]

earth_vs_1_ll_post = (df_2["fecha"] >= "6/24/2020" ) & (df_2["fecha"] <= "6/26/2020" )
earth_vs_1_ll_post = df_2[earth_vs_1_ll_post]

anounc_3_ll_post = (df_2["fecha"] >= "6/29/2020" ) & (df_2["fecha"] <= "7/1/2020" )
anounc_3_ll_post = df_2[anounc_3_ll_post]

measures_3_ll_post = (df_2["fecha"] >= "7/2/2020" ) & (df_2["fecha"] <= "7/4/2020" )
measures_3_ll_post = df_2[measures_3_ll_post]

prom_2_ll_post = (df_2["fecha"] >= "7/28/2020" ) & (df_2["fecha"] <= "7/30/2020" )
prom_2_ll_post = df_2[prom_2_ll_post]

fest_2_ll_post = (df_2["fecha"] >= "9/17/2020" ) & (df_2["fecha"] <= "9/19/2020" )
fest_2_ll_post = df_2[fest_2_ll_post]

prom_3_ll_post = (df_2["fecha"] >= "9/21/2020" ) & (df_2["fecha"] <= "9/23/2020" )
prom_3_ll_post = df_2[prom_3_ll_post]

prom_4_ll_post = (df_2["fecha"] >= "11/27/2020" ) & (df_2["fecha"] <= "11/29/2020" )
prom_4_ll_post = df_2[prom_4_ll_post]

fest_3_ll_post = (df_2["fecha"] >= "12/26/2020" ) & (df_2["fecha"] <= "12/28/2020" )
fest_3_ll_post = df_2[fest_3_ll_post]

earth_l_1_ll_post = (df_2["fecha"] >= "3/20/2021" ) & (df_2["fecha"] <= "3/22/2021" )
earth_l_1_ll_post = df_2[earth_l_1_ll_post]

earth_vs_2_ll_post = (df_2["fecha"] >= "9/8/2021" ) & (df_2["fecha"] <= "9/10/2021" )
earth_vs_2_ll_post = df_2[earth_vs_2_ll_post]

earth_l_2_ll_post = (df_2["fecha"] >= "3/4/2022" ) & (df_2["fecha"] <= "3/6/2022" )
earth_l_2_ll_post = df_2[earth_l_2_ll_post]

earth_l_3_ll_post = (df_2["fecha"] >= "3/19/2022" ) & (df_2["fecha"] <= "3/21/2022" )
earth_l_3_ll_post = df_2[earth_l_3_ll_post]

earth_l_4_ll_post = (df_2["fecha"] >= "8/13/2022" ) & (df_2["fecha"] <= "8/15/2022" )
earth_l_4_ll_post = df_2[earth_l_4_ll_post]

earth_vs_3_ll_post = (df_2["fecha"] >= "9/20/2022" ) & (df_2["fecha"] <= "9/22/2022" )
earth_vs_3_ll_post = df_2[earth_vs_3_ll_post]

earth_s_1_ll_post = (df_2["fecha"] >= "9/23/2022" ) & (df_2["fecha"] <= "9/25/2022" )
earth_s_1_ll_post = df_2[earth_s_1_ll_post]

earth_m_1_ll_post = (df_2["fecha"] >= "12/12/2022" ) & (df_2["fecha"] <= "12/14/2022" )
earth_m_1_ll_post = df_2[earth_m_1_ll_post]

earth_m_2_ll_post = (df_2["fecha"] >= "4/4/2023" ) & (df_2["fecha"] <= "4/6/2023" )
earth_m_2_ll_post = df_2[earth_m_2_ll_post]


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

X_enterqueue = np.array([enterqueue]).T
svr  = svm.SVR()
svr.fit(X_enterqueue, fecha_ord_array)
svr_predict = svr.predict(X_enterqueue)


# plot the true and prediction datasets

plt.figure(figsize = (16, 9))
plt.scatter(date_2, enterqueue)
plt.xlabel("Dates")
plt.ylabel("Number of calls")
plt.title("True daily calls 'Lifeline service'")
plt.xticks(rotation = 90)
fig = plt.gcf()
fig.text(0.5, -0.05, 'Figure 33', ha='center')
plt.show()

print()


plt.figure(figsize = (16, 9))
ax = plt.axes()
ax.plot(fecha_ord_array, svr_predict, 'r.', label='Predictions')
ax.set_xlabel('Dates')
plt.xticks(rotation = 90)
ax.set_ylabel('Enterqueue')
plt.tick_params(labelbottom=False)
plt.tick_params(labelleft=False)
plt.title("Predicted calls 'Lifeline service'")
fig.text(0.5, -0.05, 'Figure 34', ha='center')
plt.show()


