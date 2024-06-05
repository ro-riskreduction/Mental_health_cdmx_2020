import csv
import numpy as np
import pandas as pd
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from mpl_toolkits import mplot3d

#the code for the color 3d plot was retrieved from https://www.geeksforgeeks.org/3d-scatter-plotting-in-python-using-matplotlib/
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

#This is for the first database
#Anxiety


#prepared the dates data type

date_1 = df_1["fecha"]
date_1 = date_1.drop(date_1.index[[0]])

date_2 = df_2["fecha"]
date_2 = date_2.drop(date_2.index[[0]])



max_post_72 = np.array([542, 195, 157, 569, 409, 175, 198, 176, 279, 55, 317, 76, 2531])

daily_mean_pre = np.array([347, 303, 922.333, 256, 417, 195.667, 372, 61, 44.667, 58.333, 231.333, 38.333, 92]) 

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

#3d plot

fig    = plt.figure(figsize = (16, 9))
ax = plt.axes(projection ="3d")

ax.grid(linestyle ='-.', linewidth = 0.3, 
        alpha = 0.2)

my_cmap = plt.get_cmap('hsv')
sctt = ax.scatter3D(abandon, call_duration, connected_waiting_time, alpha = 0.8,
                    c = (abandon + call_duration + connected_waiting_time), cmap = my_cmap, 
                    marker ='^')
plt.title("Relationship between abandoned call attempts, call duration and waiting time before connection")
ax.set_xlabel('Abandon "n"', fontweight ='bold') 
ax.set_ylabel('Call duration "seconds"', fontweight ='bold') 
ax.set_zlabel('Waiting time before connection "seconds"', fontweight ='bold')
fig.colorbar(sctt, ax = ax, shrink = 0.8, aspect = 15)
#fig.text(0.5, 0.0, 'Figure 32. Relationship between dimensions mediating abandonment ', ha='center')
plt.show()




#second 3d plotting

#fig    = plt.figure(figsize = (16, 9))
#ax = plt.axes(projection ="3d")

#ax.grid(linestyle ='-.', linewidth = 0.3, 
#        alpha = 0.2)

#my_cmap = plt.get_cmap('hsv')
#sctt = ax.scatter3D(enterqueue, call_duration, abandon_waiting_time, alpha = 0.8,
#                    c = (enterqueue + call_duration + abandon_waiting_time), cmap = my_cmap, 
#                    marker ='^')
#plt.title("Relation between number of calls, call duration and waiting time before abandonment")
#ax.set_xlabel('Enterqueue "n"', fontweight ='bold') 
#ax.set_ylabel('Call duration "seconds"', fontweight ='bold') 
#ax.set_zlabel('Waiting time before abandonment "seconds"', fontweight ='bold')
#fig.colorbar(sctt, ax = ax, shrink = 0.8, aspect = 15)
#plt.show()

#third 3d plotting


#fig    = plt.figure(figsize = (16, 9))
#ax = plt.axes(projection ="3d")

#ax.grid(linestyle ='-.', linewidth = 0.3, 
#        alpha = 0.2)

#my_cmap = plt.get_cmap('hsv')
#sctt = ax.scatter3D(enterqueue, call_duration, connected_waiting_time, alpha = 0.8,
#                    c = (enterqueue + call_duration + connected_waiting_time), cmap = my_cmap, 
#                    marker ='^')
#plt.title("Relation between number of calls, call duration and waiting time before connection")
#ax.set_xlabel('Enterqueue "n"', fontweight ='bold') 
#ax.set_ylabel('Call duration "seconds"', fontweight ='bold') 
#ax.set_zlabel('Waiting time before connection "seconds"', fontweight ='bold')
#fig.colorbar(sctt, ax = ax, shrink = 0.8, aspect = 15)
#plt.show()