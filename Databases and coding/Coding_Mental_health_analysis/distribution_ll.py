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

complete_caller = df_2["Completecaller"]
complete_caller = complete_caller.drop(complete_caller.index[[0]])
complete_caller = np.array(complete_caller, dtype=float)

complete_agent = df_2["Completeagent"]
complete_agent = complete_agent.drop(complete_agent.index[[0]])
complete_agent = np.array(complete_agent, dtype=float)

abandon_waiting_time = df_2["Abandono - Tiempo de espera"]
abandon_waiting_time = abandon_waiting_time.drop(abandon_waiting_time.index[[0]])
abandon_waiting_time = np.array(abandon_waiting_time, dtype=float)

connected_waiting_time = df_2["Conectado - Tiempo de espera"]
connected_waiting_time = connected_waiting_time.drop(connected_waiting_time.index[[0]])
connected_waiting_time = np.array(connected_waiting_time, dtype=float)

call_duration = df_2["Tiempo en llamada"]
call_duration = call_duration.drop(call_duration.index[[0]])
call_duration = np.array(call_duration, dtype=float)


a0     = np.mean( enterqueue )
a1     = np.median( enterqueue )
result = stats.mode( enterqueue ) # mode(s) and count(s)
a2     = result.mode

b0     = np.mean( connect )
b1     = np.median( connect )
result = stats.mode( connect ) # mode(s) and count(s)
b2     = result.mode

c0     = np.mean( abandon )
c1     = np.median( abandon )
result = stats.mode( abandon ) # mode(s) and count(s)
c2     = result.mode

d0     = np.mean( connected_waiting_time )
d1     = np.median( connected_waiting_time )
result = stats.mode( connected_waiting_time ) # mode(s) and count(s)
d2     = result.mode

e0     = np.mean( abandon_waiting_time )
e1     = np.median( abandon_waiting_time )
result = stats.mode( abandon_waiting_time ) # mode(s) and count(s)
e2     = result.mode

f0     = np.mean( call_duration )
f1     = np.median( call_duration )
result = stats.mode( call_duration ) # mode(s) and count(s)
f2     = result.mode



plt.figure()

plt.subplot(2,3,1)
plt.hist(enterqueue)
plt.axvline(a0, color='r', label='Mean')
plt.axvline(a1, color='g', label='Median')
plt.axvline(a2, color='k', label='Mode')
plt.legend()
plt.xlabel('Enterqueue')
plt.ylabel('Number of calls')
plt.title("Figure 26")

plt.subplot(2,3,2)
plt.hist(connect)
plt.axvline(b0, color='r', label='Mean')
plt.axvline(b1, color='g', label='Median')
plt.axvline(b2, color='k', label='Mode')
plt.legend()
plt.xlabel('Connected')
plt.ylabel('Number of calls')
plt.title("Figure 27")

plt.subplot(2,3,3)
plt.hist(abandon)
plt.axvline(c0, color='r', label='Mean')
plt.axvline(c1, color='g', label='Median')
plt.axvline(c2, color='k', label='Mode')
plt.legend()
plt.xlabel('Abandoned')
plt.ylabel('Number of calls')
plt.title("Figure 28")

plt.subplot(2,3,4)
plt.hist(connected_waiting_time)
plt.axvline(d0, color='r', label='Mean')
plt.axvline(d1, color='g', label='Median')
plt.axvline(d2, color='k', label='Mode')
plt.legend()
plt.xlabel('Time before connexion')
plt.ylabel('Seconds')
plt.title("Figure 29")

plt.subplot(2,3,5)
plt.hist(abandon_waiting_time)
plt.axvline(e0, color='r', label='Mean')
plt.axvline(e1, color='g', label='Median')
plt.axvline(e2, color='k', label='Mode')
plt.legend()
plt.xlabel('Time before abandoning')
plt.ylabel('Seconds')
plt.title("Figure 30")

plt.subplot(2,3,6)
plt.hist(call_duration, bins=5)
plt.axvline(f0, color='r', label='Mean')
plt.axvline(f1, color='g', label='Median')
plt.axvline(f2, color='k', label='Mode')
plt.legend()
plt.xlabel('Call duration')
plt.ylabel('Seconds')
plt.title("Figure 31")

plt.tight_layout()

plt.show()