import csv
import numpy as np
import pandas as pd

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

date_1 = df_1["fecha"]
date_1 = date_1.drop(date_1.index[[0]])

date_2 = df_2["fecha"]
date_2 = date_2.drop(date_2.index[[0]])


#This is for the first database
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

#Information seeking

inf_1 = df_1["64. Actualmente Leo (o me intereso por programas de televisión o radio) sobre enfermedades físicas graves"]
inf_1 = inf_1.drop(inf_1.index[[0]])
inf_1 = np.array(inf_1, dtype=float)

#Somatization

som_1 = df_1["62. Actualmente Creo que padezco alguna enfermedad física grave (aunque no me la han confirmado)"]
som_1 = som_1.drop(som_1.index[[0]])
som_1 = np.array(som_1, dtype=float)

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

#Label PTSD

ptsd = df_1["PTSD"]
ptsd = ptsd.drop(ptsd.index[[0]])
ptsd = np.array(ptsd, dtype=float)


#prepared the dates data type

date_1 = df_1["fecha"]
date_1 = date_1.drop(date_1.index[[0]])

date_2 = df_2["fecha"]
date_2 = date_2.drop(date_2.index[[0]])


#create numpyarrays

anx_array = np.vstack( (anx_1, anx_2, anx_3, anx_4, anx_5, anx_6) ).T

str_array = np.vstack( (str_1, str_2, str_3, str_4, str_5, str_6, str_7) ).T

avo_array = np.vstack( (avo_1, avo_2, avo_3 ) ).T

dis_array = np.vstack( (dis_1, dis_2, dis_3, dis_4, dis_5 ) ).T

features_array = np.vstack( (anx_1, anx_2, anx_3, anx_4, anx_5, anx_6, str_1, str_2, str_3, str_4, str_5, str_6, str_7, avo_1, avo_2, avo_3, dis_1, dis_2, dis_3, dis_4, dis_5, som_1, inf_1  ) ).T

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



#mean lifeline pre
enterqueue_mean_pre_72_lifeline = np.array( [998.667,1241.333,1023.333,778,746.667,1411.333,655.333,668,960,497.333,641.333,616,856.667,1011.333,592.667,1211.333,1220,642] )

connect_mean_pre_72_lifeline = np.array([782.667,878.667,801.333,552,668,949.333,588.667,545.333,889.333,440,469.333,346.667,400.667,750.667,526,577.333,340,250.667])

abandon_mean_pre_72_lifeline = np.array([216,362.667,222,226.667,78.667,463.333,66.667,122.667,71.333,58,172.667,268.667,456,260.667,66.667,633.333,879.333,390.667])

wtc_mean_pre_72_lifeline = np.array([11.547,24.96,21.821,25.555,7.963,44.639,7.032,17.626,5.739,10.489,66.823,70.432,113.204,61.346,16.407,146.168,256.589,163.182])

wta_mean_pre_72_lifeline = np.array([78.243,90.123,66.236,82.766,65.357,99.597,51.025,104.289,61.895,157.069,177.557,193.055,179.03,131.282,110.171,163.504,254.992,284.539])

call_dur_mean_pre_72_lifeline = np.array([338.656,371.648,354.467,399.799,360.055,372.062,407.728,527.296,252.606,492.224,481.756,643.429,781.135,571.276,635.141,697.396,918.899,850.776])

lifeline_mean_72_array = np.vstack((enterqueue_mean_pre_72_lifeline, connect_mean_pre_72_lifeline, abandon_mean_pre_72_lifeline , wtc_mean_pre_72_lifeline, wta_mean_pre_72_lifeline, call_dur_mean_pre_72_lifeline)).T

#max lifeline

enterqueue_max_72_lifeline = (	[1242,	1214,	1056	,784,	700	,1414,	964	,	368,	1074,	570,	996,	978,	970,	1336,	576	,1352,	1064	,	628	]	)
connect_max_72_lifeline	=	(	[	980,	1156	,	780,	592	,	620,	1124	,	812,	312	,	912,	472,	200,	554	,	612,	956	,	512,	648	,	614,	282	]	)
abandon_max_72_lifeline	=	(	[	262,	56	,	276,	192	,	80,	296	,	152,	56	,	162,	98	,	758,	428	,	358,	380	,	64,	704	,	448,	346	]	)
wtc_max_72_lifeline	=	(	[	23.086	,	3.533	,	13.772	,	28.159	,	17.658	,	31.972	,	8.222	,	16.718	,	7.706	,	23.275	,	302.273	,	91.377	,	94.673	,	44.772	,	26.105	,	165.611	,	98.401	,	60.723	]	)
wta_max_72_lifeline	=	(	[	79.748	,	34.536	,	84.826	,	79.865	,	71.475	,	81.176	,	55.961	,	128.857	,	75.086	,	182.592	,	233.127	,	331.846	,	154.972	,	107.216	,	124.875	,	192.642	,	146.067	,	184.283	]	)
call_dur_max_72_lifeline =		(	[	504.47	,	279.953	,	370.682	,	392.997	,	487.259	,	348.328	,	319.553	,	350.51	,	373.945	,	672.247	,	1261.622	,	519.766	,	359.925	,	615.146	,	597.604	,	721.795	,	478.369	,	682.725	]	)

lifeline_max_72_array = np.vstack((enterqueue_max_72_lifeline, connect_max_72_lifeline, abandon_max_72_lifeline , wtc_max_72_lifeline, wta_max_72_lifeline, call_dur_max_72_lifeline)).T

