import csv
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import modules as md
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

##########################################################################################
#full_period

anounc_1 = (df_1["fecha"] >= "4/14/2020")  & (df_1["fecha"] <= "4/19/2020" )
anounc_1 = df_1[anounc_1]

measures_1 = (df_1["fecha"] >= "4/18/2020" ) & (df_1["fecha"] <= "4/24/2020" )
measures_1 = df_1[measures_1]

prom_1 = (df_1["fecha"] >= "4/23/2020" ) & (df_1["fecha"] <= "4/29/2020" )
prom_1 = df_1[prom_1]

fest_1 = (df_1["fecha"] >= "5/7/2020" ) & (df_1["fecha"] <= "5/13/2020" )
fest_1 = df_1[fest_1]

anounc_2 = (df_1["fecha"] >= "5/10/2020" ) & (df_1["fecha"] <= "5/16/2020" )
anounc_2 = df_1[anounc_2]

measures_2 = (df_1["fecha"] >= "5/29/2020" ) & (df_1["fecha"] <= "6/4/2020" )
measures_2 = df_1[measures_2]

earth_vs_1 = (df_1["fecha"] >= "6/20/2020" ) & (df_1["fecha"] <= "6/26/2020" )
earth_vs_1 = df_1[earth_vs_1]

anounc_3 = (df_1["fecha"] >= "6/24/2020" ) & (df_1["fecha"] <= "7/1/2020" )
anounc_3 = df_1[anounc_3]

measures_3 = (df_1["fecha"] >= "6/28/2020" ) & (df_1["fecha"] <= "7/4/2020" )
measures_3 = df_1[measures_3]

prom_2 = (df_1["fecha"] >= "7/24/2020" ) & (df_1["fecha"] <= "7/30/2020" )
prom_2 = df_1[prom_2]

fest_2 = (df_1["fecha"] >= "9/13/2020" ) & (df_1["fecha"] <= "9/19/2020" )
fest_2 = df_1[fest_2]

prom_3 = (df_1["fecha"] >= "9/17/2020" ) & (df_1["fecha"] <= "9/23/2020" )
prom_3 = df_1[prom_3]

prom_4 = (df_1["fecha"] >= "11/23/2020" ) & (df_1["fecha"] <= "11/29/2020" )
prom_4 = df_1[prom_4]

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

anounc_1_pre = (df_1["fecha"] >= "4/14/2020")  & (df_1["fecha"] <= "4/15/2020" )
anounc_1_pre = df_1[anounc_1_pre]

measures_1_pre = (df_1["fecha"] >= "4/18/2020" ) & (df_1["fecha"] <= "4/20/2020" )
measures_1_pre = df_1[measures_1_pre]

prom_1_pre = (df_1["fecha"] >= "4/23/2020" ) & (df_1["fecha"] <= "4/25/2020" )
prom_1_pre = df_1[prom_1_pre]

fest_1_pre = (df_1["fecha"] >= "5/7/2020" ) & (df_1["fecha"] <= "5/9/2020" )
fest_1_pre = df_1[fest_1_pre]

anounc_2_pre = (df_1["fecha"] >= "5/10/2020" ) & (df_1["fecha"] <= "5/12/2020" )
anounc_2_pre = df_1[anounc_2_pre]

measures_2_pre = (df_1["fecha"] >= "5/29/2020" ) & (df_1["fecha"] <= "6/1/2020" )
measures_2_pre = df_1[measures_2_pre]

earth_vs_1_pre = (df_1["fecha"] >= "6/20/2020" ) & (df_1["fecha"] <= "6/22/2020" )
earth_vs_1_pre = df_1[earth_vs_1_pre]

anounc_3_pre = (df_1["fecha"] >= "6/24/2020" ) & (df_1["fecha"] <= "6/26/2020" )
anounc_3_pre = df_1[anounc_3_pre]

measures_3_pre = (df_1["fecha"] >= "6/28/2020" ) & (df_1["fecha"] <= "7/1/2020" )
measures_3_pre = df_1[measures_3_pre]

prom_2_pre = (df_1["fecha"] >= "7/24/2020" ) & (df_1["fecha"] <= "7/26/2020" )
prom_2_pre = df_1[prom_2_pre]

fest_2_pre = (df_1["fecha"] >= "9/13/2020" ) & (df_1["fecha"] <= "9/15/2020" )
fest_2_pre = df_1[fest_2_pre]

prom_3_pre = (df_1["fecha"] >= "9/17/2020" ) & (df_1["fecha"] <= "9/19/2020" )
prom_3_pre = df_1[prom_3_pre]

prom_4_pre = (df_1["fecha"] >= "11/23/2020" ) & (df_1["fecha"] <= "11/25/2020" )
prom_4_pre = df_1[prom_4_pre]

measures_2_ll_pre = (df_2["fecha"] >= "5/29/2020" ) & (df_2["fecha"] <= "6/1/2020" )
measures_2_ll_pre = df_2[measures_2_ll_pre]

earth_vs_1_ll_pre = (df_2["fecha"] >= "6/20/2020" ) & (df_2["fecha"] <= "6/22/2020" )
earth_vs_1_ll_pre = df_2[earth_vs_1_ll_pre]

anounc_3_ll_pre = (df_2["fecha"] >= "6/24/2020" ) & (df_2["fecha"] <= "6/26/2020" )
anounc_3_ll_pre = df_2[anounc_3_ll_pre]

measures_3_ll_pre = (df_2["fecha"] >= "6/28/2020" ) & (df_2["fecha"] <= "7/1/2020" )
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

anounc_1_post = (df_1["fecha"] >= "4/17/2020")  & (df_1["fecha"] <= "4/19/2020" )
anounc_1_post = df_1[anounc_1_post]

measures_1_post = (df_1["fecha"] >= "4/22/2020" ) & (df_1["fecha"] <= "4/24/2020" )
measures_1_post = df_1[measures_1_post]

prom_1_post = (df_1["fecha"] >= "4/27/2020" ) & (df_1["fecha"] <= "4/29/2020" )
prom_1_post = df_1[prom_1_post]

fest_1_post = (df_1["fecha"] >= "5/11/2020" ) & (df_1["fecha"] <= "5/13/2020" )
fest_1_post = df_1[fest_1_post]

anounc_2_post = (df_1["fecha"] >= "5/14/2020" ) & (df_1["fecha"] <= "5/16/2020" )
anounc_2_post = df_1[anounc_2_post]

measures_2_post = (df_1["fecha"] >= "6/2/2020" ) & (df_1["fecha"] <= "6/4/2020" )
measures_2_post = df_1[measures_2_post]

earth_vs_1_post = (df_1["fecha"] >= "6/24/2020" ) & (df_1["fecha"] <= "6/26/2020" )
earth_vs_1_post = df_1[earth_vs_1_post]

anounc_3_post = (df_1["fecha"] >= "6/28/2020" ) & (df_1["fecha"] <= "7/1/2020" )
anounc_3_post = df_1[anounc_3_post]

measures_3_post = (df_1["fecha"] >= "7/2/2020" ) & (df_1["fecha"] <= "7/4/2020" )
measures_3_post = df_1[measures_3_post]

prom_2_post = (df_1["fecha"] >= "7/28/2020" ) & (df_1["fecha"] <= "7/30/2020" )
prom_2_post = df_1[prom_2_post]

fest_2_post = (df_1["fecha"] >= "9/17/2020" ) & (df_1["fecha"] <= "9/19/2020" )
fest_2_post = df_1[fest_2_post]

prom_3_post = (df_1["fecha"] >= "9/21/2020" ) & (df_1["fecha"] <= "9/23/2020" )
prom_3_post = df_1[prom_3_post]

prom_4_post = (df_1["fecha"] >= "11/27/2020" ) & (df_1["fecha"] <= "11/29/2020" )
prom_4_post = df_1[prom_4_post]

measures_2_ll_post = (df_2["fecha"] >= "6/2/2020" ) & (df_2["fecha"] <= "6/4/2020" )
measures_2_ll_post = df_2[measures_2_ll_post]

earth_vs_1_ll_post = (df_2["fecha"] >= "6/24/2020" ) & (df_2["fecha"] <= "6/26/2020" )
earth_vs_1_ll_post = df_2[earth_vs_1_ll_post]

anounc_3_ll_post = (df_2["fecha"] >= "6/28/2020" ) & (df_2["fecha"] <= "7/1/2020" )
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



print("Anouncement_1")
#Anxiety
#Anx_1
anounc_1_anx_1_pre = anounc_1_pre["54 Durante las últimas 2 semanas Me he sentido nerviosa(o), ansiosa(o) o con los nervios de punta"]
anounc_1_anx_1_post = anounc_1_post["54 Durante las últimas 2 semanas Me he sentido nerviosa(o), ansiosa(o) o con los nervios de punta"]
r1 = md.anova(anounc_1_anx_1_pre, anounc_1_anx_1_post)
#print(r1)


#Anx_2
anounc_1_anx_2_pre = anounc_1_pre["55 Durante las últimas 2 semanas Me he sentido incapaz de controlar mis preocupaciones"]
anounc_1_anx_2_post = anounc_1_post["55 Durante las últimas 2 semanas Me he sentido incapaz de controlar mis preocupaciones"]
r2 = md.anova(anounc_1_anx_2_pre, anounc_1_anx_2_post)
#print(r2)


#Anx_3
anounc_1_anx_3_pre = anounc_1_pre["56 Durante las últimas 2 semanas Me he sentido tan inquieta(o) que no he podido quedarme quieta(o)"]
anounc_1_anx_3_post = anounc_1_post["56 Durante las últimas 2 semanas Me he sentido tan inquieta(o) que no he podido quedarme quieta(o)"]
r3 = md.anova(anounc_1_anx_3_pre, anounc_1_anx_3_post)
#print(r3)

#Anx_4
anounc_1_anx_4_pre = anounc_1_pre["57 Durante las últimas 2 semanas He tenido dificultad para relajarme"]
anounc_1_anx_4_post = anounc_1_post["57 Durante las últimas 2 semanas He tenido dificultad para relajarme"]
r4 = md.anova(anounc_1_anx_4_pre, anounc_1_anx_4_post)
#print(r4)


#Anx_5
anounc_1_anx_5_pre = anounc_1_pre["67 Durante las últimas 2 semanas Siento poco interés o placer en hacer cosas"]
anounc_1_anx_5_post = anounc_1_post["67 Durante las últimas 2 semanas Siento poco interés o placer en hacer cosas"]
r5 = md.anova(anounc_1_anx_5_pre, anounc_1_anx_5_post)
#print(r5)


#Anx_6
anounc_1_anx_6_pre = anounc_1_pre["68Durante las últimas 2 semanas Me he sentido decaída(o) deprimida(o) o sin esperanzas"]
anounc_1_anx_6_post = anounc_1_post["68Durante las últimas 2 semanas Me he sentido decaída(o) deprimida(o) o sin esperanzas"]
r6 = md.anova(anounc_1_anx_6_pre, anounc_1_anx_6_post)
#print(r6)

##############################################################################

#Stress

#Str_1
anounc_1_str_1_pre = anounc_1_pre["37. En el último mes Pienso o imagino, repetidamente, que voy a enfermar"]
anounc_1_str_1_post = anounc_1_post["37. En el último mes Pienso o imagino, repetidamente, que voy a enfermar"]
r7 = md.anova(anounc_1_str_1_pre, anounc_1_str_1_post)
#print(r7)


#Str_2
anounc_1_str_2_pre = anounc_1_pre["38. En el último mes Tengo pesadillas que se repiten acerca de la enfermedad"]
anounc_1_str_2_post = anounc_1_post["38. En el último mes Tengo pesadillas que se repiten acerca de la enfermedad"]
r8 = md.anova(anounc_1_str_2_pre, anounc_1_str_2_post)
#print(r8)


#Str_3
anounc_1_str_3_pre = anounc_1_pre["39 En el último mes Me siento preocupada(o) cuando se menciona la enfermedad"]
anounc_1_str_3_post = anounc_1_post["39 En el último mes Me siento preocupada(o) cuando se menciona la enfermedad"]
r9 = md.anova(anounc_1_str_3_pre, anounc_1_str_3_post)
#print(r9)

#Str_4
anounc_1_str_4_pre = anounc_1_pre["40 En el último mes Tengo reacciones físicas desagradable cuando pienso en la enfermedad (por ejemplo, latidos cardiacos muy fuertes, problemas para respirar, sudoración)"]
anounc_1_str_4_post = anounc_1_post["40 En el último mes Tengo reacciones físicas desagradable cuando pienso en la enfermedad (por ejemplo, latidos cardiacos muy fuertes, problemas para respirar, sudoración)"]
r10 = md.anova(anounc_1_str_4_pre, anounc_1_str_4_post)
#print(r10)


#Str_5
anounc_1_str_5_pre = anounc_1_pre["44 En el último mes Pienso que si me enfermo o se enferma alguien de mi familia, es por mi culpa"]
anounc_1_str_5_post = anounc_1_post["44 En el último mes Pienso que si me enfermo o se enferma alguien de mi familia, es por mi culpa"]
r11 = md.anova(anounc_1_str_5_pre, anounc_1_str_5_post)
#print(r11)


#Str_6
anounc_1_str_6_pre = anounc_1_pre["48 En el último mes Siento que mi futuro es incierto a partir de que comenzó el riesgo a padecer esta enfermedad"]
anounc_1_str_6_post = anounc_1_post["48 En el último mes Siento que mi futuro es incierto a partir de que comenzó el riesgo a padecer esta enfermedad"]
r12 = md.anova(anounc_1_str_6_pre, anounc_1_str_6_post)
#print(r12)

#Str_7
anounc_1_str_7_pre = anounc_1_pre["53 En el último mes Me siento asustada(o) por los riesgos a padecer esta enfermedad"]
anounc_1_str_7_post = anounc_1_post["53 En el último mes Me siento asustada(o) por los riesgos a padecer esta enfermedad"]
r13 = md.anova(anounc_1_str_7_pre, anounc_1_str_7_post)
#print(r13)


#################################################################################
#Avoidance
#Avo_1
anounc_1_avo_1_pre = anounc_1_pre["41.En el último mes Evito pensar, sentir o hablar sobre la enfermedad"]
anounc_1_avo_1_post = anounc_1_post["41.En el último mes Evito pensar, sentir o hablar sobre la enfermedad"]
r14 = md.anova(anounc_1_avo_1_pre, anounc_1_avo_1_post)
#print(r14)


#Avo_2
anounc_1_avo_2_pre = anounc_1_pre["42. En el último mes Evito ver o recurrir a información oficial sobre la enfermedad"]
anounc_1_avo_2_post = anounc_1_post["42. En el último mes Evito ver o recurrir a información oficial sobre la enfermedad"]
r15 = md.anova(anounc_1_avo_2_pre, anounc_1_avo_2_post)
#print(r15)


#Avo_3
anounc_1_avo_3_pre = anounc_1_pre["43. En el último mes Tengo dificultad para recordar lo que recomiendan las autoridades para enfrentar el riesgo o la enfermedad"]
anounc_1_avo_3_post = anounc_1_post["43. En el último mes Tengo dificultad para recordar lo que recomiendan las autoridades para enfrentar el riesgo o la enfermedad"]
r16 = md.anova(anounc_1_avo_3_pre, anounc_1_avo_3_post)
#print(r16)

###################################################################################

#Distancing
#Dis_1
anounc_1_dis_1_pre = anounc_1_pre["45. En el último mes He perdido interés por las actividades que antes disfrutaba"]
anounc_1_dis_1_post = anounc_1_post["45. En el último mes He perdido interés por las actividades que antes disfrutaba"]
r17 = md.anova(anounc_1_dis_1_pre, anounc_1_dis_1_post)
#print(r17)


#Dis_2
anounc_1_dis_2_pre = anounc_1_pre["46. En el último mes Me siento distante de las personas con quienes convivo, a partir de que inició el riesgo de esta enfermedad"]
anounc_1_dis_2_post = anounc_1_post["46. En el último mes Me siento distante de las personas con quienes convivo, a partir de que inició el riesgo de esta enfermedad"]
r18 = md.anova(anounc_1_dis_2_pre, anounc_1_dis_2_post)
#print(r18)


#Dis_3
anounc_1_dis_3_pre = anounc_1_pre["49. En el último mes Siento que deseo hacer cosas para hacerme daño"]
anounc_1_dis_3_post = anounc_1_post["49. En el último mes Siento que deseo hacer cosas para hacerme daño"]
r19 = md.anova(anounc_1_dis_3_pre, anounc_1_dis_3_post)
#print(r19)

#Dis_4
anounc_1_dis_4_pre = anounc_1_pre["50. En el último mes Tengo dificultad para quedarme dormido o seguir durmiendo"]
anounc_1_dis_4_post = anounc_1_post["50. En el último mes Tengo dificultad para quedarme dormido o seguir durmiendo"]
r20 = md.anova(anounc_1_dis_4_pre, anounc_1_dis_4_post)
#print(r20)


#Dis_5
anounc_1_dis_5_pre = anounc_1_pre["51. En el último mes Me siento enojada (o)"]
anounc_1_dis_5_post = anounc_1_post["51. En el último mes Me siento enojada (o)"]
r21 = md.anova(anounc_1_dis_5_pre, anounc_1_dis_5_post)
#print(r21)

#########################################################################


#Information seeking
#Inf_1
anounc_1_inf_1_pre = anounc_1_pre["64. Actualmente Leo (o me intereso por programas de televisión o radio) sobre enfermedades físicas graves"]
anounc_1_inf_1_post = anounc_1_post["64. Actualmente Leo (o me intereso por programas de televisión o radio) sobre enfermedades físicas graves"]
r22 = md.anova(anounc_1_inf_1_pre, anounc_1_inf_1_post)
#print(r22)

#Somatization
#Som_1
anounc_1_som_1_pre = anounc_1_pre["62. Actualmente Creo que padezco alguna enfermedad física grave (aunque no me la han confirmado)"]
anounc_1_som_1_post = anounc_1_post["62. Actualmente Creo que padezco alguna enfermedad física grave (aunque no me la han confirmado)"]
r23 = md.anova(anounc_1_som_1_pre, anounc_1_som_1_post)
#print(r23)


######################################################################
print("measures_1")
#measures_1
#Anxiety
#Anx_1
measures_1_anx_1_pre = measures_1_pre["54 Durante las últimas 2 semanas Me he sentido nerviosa(o), ansiosa(o) o con los nervios de punta"]
measures_1_anx_1_post = measures_1_post["54 Durante las últimas 2 semanas Me he sentido nerviosa(o), ansiosa(o) o con los nervios de punta"]
r1 = md.anova(measures_1_anx_1_pre, measures_1_anx_1_post)
#print(r1)


#Anx_2
measures_1_anx_2_pre = measures_1_pre["55 Durante las últimas 2 semanas Me he sentido incapaz de controlar mis preocupaciones"]
measures_1_anx_2_post = measures_1_post["55 Durante las últimas 2 semanas Me he sentido incapaz de controlar mis preocupaciones"]
r2 = md.anova(measures_1_anx_2_pre, measures_1_anx_2_post)
#print(r2)


#Anx_3
measures_1_anx_3_pre = measures_1_pre["56 Durante las últimas 2 semanas Me he sentido tan inquieta(o) que no he podido quedarme quieta(o)"]
measures_1_anx_3_post = measures_1_post["56 Durante las últimas 2 semanas Me he sentido tan inquieta(o) que no he podido quedarme quieta(o)"]
r3 = md.anova(measures_1_anx_3_pre, measures_1_anx_3_post)
#print(r3)

#Anx_4
measures_1_anx_4_pre = measures_1_pre["57 Durante las últimas 2 semanas He tenido dificultad para relajarme"]
measures_1_anx_4_post = measures_1_post["57 Durante las últimas 2 semanas He tenido dificultad para relajarme"]
r4 = md.anova(measures_1_anx_4_pre, measures_1_anx_4_post)
#print(r4)


#Anx_5
measures_1_anx_5_pre = measures_1_pre["67 Durante las últimas 2 semanas Siento poco interés o placer en hacer cosas"]
measures_1_anx_5_post = measures_1_post["67 Durante las últimas 2 semanas Siento poco interés o placer en hacer cosas"]
r5 = md.anova(measures_1_anx_5_pre, measures_1_anx_5_post)
#print(r5)


#Anx_6
measures_1_anx_6_pre = measures_1_pre["68Durante las últimas 2 semanas Me he sentido decaída(o) deprimida(o) o sin esperanzas"]
measures_1_anx_6_post = measures_1_post["68Durante las últimas 2 semanas Me he sentido decaída(o) deprimida(o) o sin esperanzas"]
r6 = md.anova(measures_1_anx_6_pre, measures_1_anx_6_post)
#print(r6)

##############################################################################

#Stress

#Str_1
measures_1_str_1_pre = measures_1_pre["37. En el último mes Pienso o imagino, repetidamente, que voy a enfermar"]
measures_1_str_1_post = measures_1_post["37. En el último mes Pienso o imagino, repetidamente, que voy a enfermar"]
r7 = md.anova(measures_1_str_1_pre, measures_1_str_1_post)
#print(r7)


#Str_2
measures_1_str_2_pre = measures_1_pre["38. En el último mes Tengo pesadillas que se repiten acerca de la enfermedad"]
measures_1_str_2_post = measures_1_post["38. En el último mes Tengo pesadillas que se repiten acerca de la enfermedad"]
r8 = md.anova(measures_1_str_2_pre, measures_1_str_2_post)
#print(r8)


#Str_3
measures_1_str_3_pre = measures_1_pre["39 En el último mes Me siento preocupada(o) cuando se menciona la enfermedad"]
measures_1_str_3_post = measures_1_post["39 En el último mes Me siento preocupada(o) cuando se menciona la enfermedad"]
r9 = md.anova(measures_1_str_3_pre, measures_1_str_3_post)
#print(r9)

#Str_4
measures_1_str_4_pre = measures_1_pre["40 En el último mes Tengo reacciones físicas desagradable cuando pienso en la enfermedad (por ejemplo, latidos cardiacos muy fuertes, problemas para respirar, sudoración)"]
measures_1_str_4_post = measures_1_post["40 En el último mes Tengo reacciones físicas desagradable cuando pienso en la enfermedad (por ejemplo, latidos cardiacos muy fuertes, problemas para respirar, sudoración)"]
r10 = md.anova(measures_1_str_4_pre, measures_1_str_4_post)
#print(r10)


#Str_5
measures_1_str_5_pre = measures_1_pre["44 En el último mes Pienso que si me enfermo o se enferma alguien de mi familia, es por mi culpa"]
measures_1_str_5_post = measures_1_post["44 En el último mes Pienso que si me enfermo o se enferma alguien de mi familia, es por mi culpa"]
r11 = md.anova(measures_1_str_5_pre, measures_1_str_5_post)
#print(r11)


#Str_6
measures_1_str_6_pre = measures_1_pre["48 En el último mes Siento que mi futuro es incierto a partir de que comenzó el riesgo a padecer esta enfermedad"]
measures_1_str_6_post = measures_1_post["48 En el último mes Siento que mi futuro es incierto a partir de que comenzó el riesgo a padecer esta enfermedad"]
r12 = md.anova(measures_1_str_6_pre, measures_1_str_6_post)
#print(r12)

#Str_7
measures_1_str_7_pre = measures_1_pre["53 En el último mes Me siento asustada(o) por los riesgos a padecer esta enfermedad"]
measures_1_str_7_post = measures_1_post["53 En el último mes Me siento asustada(o) por los riesgos a padecer esta enfermedad"]
r13 = md.anova(measures_1_str_7_pre, measures_1_str_7_post)
#print(r13)


#################################################################################
#Avoidance
#Avo_1
measures_1_avo_1_pre = measures_1_pre["41.En el último mes Evito pensar, sentir o hablar sobre la enfermedad"]
measures_1_avo_1_post = measures_1_post["41.En el último mes Evito pensar, sentir o hablar sobre la enfermedad"]
r14 = md.anova(measures_1_avo_1_pre, measures_1_avo_1_post)
#print(r14)


#Avo_2
measures_1_avo_2_pre = measures_1_pre["42. En el último mes Evito ver o recurrir a información oficial sobre la enfermedad"]
measures_1_avo_2_post = measures_1_post["42. En el último mes Evito ver o recurrir a información oficial sobre la enfermedad"]
r15 = md.anova(measures_1_avo_2_pre, measures_1_avo_2_post)
#print(r15)


#Avo_3
measures_1_avo_3_pre = measures_1_pre["43. En el último mes Tengo dificultad para recordar lo que recomiendan las autoridades para enfrentar el riesgo o la enfermedad"]
measures_1_avo_3_post = measures_1_post["43. En el último mes Tengo dificultad para recordar lo que recomiendan las autoridades para enfrentar el riesgo o la enfermedad"]
r16 = md.anova(measures_1_avo_3_pre, measures_1_avo_3_post)
#print(r16)

###################################################################################

#Distancing
#Dis_1
measures_1_dis_1_pre = measures_1_pre["45. En el último mes He perdido interés por las actividades que antes disfrutaba"]
measures_1_dis_1_post = measures_1_post["45. En el último mes He perdido interés por las actividades que antes disfrutaba"]
r17 = md.anova(measures_1_dis_1_pre, measures_1_dis_1_post)
#print(r17)


#Dis_2
measures_1_dis_2_pre = measures_1_pre["46. En el último mes Me siento distante de las personas con quienes convivo, a partir de que inició el riesgo de esta enfermedad"]
measures_1_dis_2_post = measures_1_post["46. En el último mes Me siento distante de las personas con quienes convivo, a partir de que inició el riesgo de esta enfermedad"]
r18 = md.anova(measures_1_dis_2_pre, measures_1_dis_2_post)
#print(r18)


#Dis_3
measures_1_dis_3_pre = measures_1_pre["49. En el último mes Siento que deseo hacer cosas para hacerme daño"]
measures_1_dis_3_post = measures_1_post["49. En el último mes Siento que deseo hacer cosas para hacerme daño"]
r19 = md.anova(measures_1_dis_3_pre, measures_1_dis_3_post)
#print(r19)

#Dis_4
measures_1_dis_4_pre = measures_1_pre["50. En el último mes Tengo dificultad para quedarme dormido o seguir durmiendo"]
measures_1_dis_4_post = measures_1_post["50. En el último mes Tengo dificultad para quedarme dormido o seguir durmiendo"]
r20 = md.anova(measures_1_dis_4_pre, measures_1_dis_4_post)
#print(r20)


#Dis_5
measures_1_dis_5_pre = measures_1_pre["51. En el último mes Me siento enojada (o)"]
measures_1_dis_5_post = measures_1_post["51. En el último mes Me siento enojada (o)"]
r21 = md.anova(measures_1_dis_5_pre, measures_1_dis_5_post)
#print(r21)

#########################################################################


#Information seeking
#Inf_1
measures_1_inf_1_pre = measures_1_pre["64. Actualmente Leo (o me intereso por programas de televisión o radio) sobre enfermedades físicas graves"]
measures_1_inf_1_post = measures_1_post["64. Actualmente Leo (o me intereso por programas de televisión o radio) sobre enfermedades físicas graves"]
r22 = md.anova(measures_1_inf_1_pre, measures_1_inf_1_post)
#print(r22)

#Somatization
#Som_1
measures_1_som_1_pre = measures_1_pre["62. Actualmente Creo que padezco alguna enfermedad física grave (aunque no me la han confirmado)"]
measures_1_som_1_post = measures_1_post["62. Actualmente Creo que padezco alguna enfermedad física grave (aunque no me la han confirmado)"]
r23 = md.anova(measures_1_som_1_pre, measures_1_som_1_post)
#print(r23)


###############################################################################
print("prom_1")
#prom_1
#Anxiety
#Anx_1
prom_1_anx_1_pre = prom_1_pre["54 Durante las últimas 2 semanas Me he sentido nerviosa(o), ansiosa(o) o con los nervios de punta"]
prom_1_anx_1_post = prom_1_post["54 Durante las últimas 2 semanas Me he sentido nerviosa(o), ansiosa(o) o con los nervios de punta"]
r1 = md.anova(prom_1_anx_1_pre, prom_1_anx_1_post)
#print(r1)


#Anx_2
prom_1_anx_2_pre = prom_1_pre["55 Durante las últimas 2 semanas Me he sentido incapaz de controlar mis preocupaciones"]
prom_1_anx_2_post = prom_1_post["55 Durante las últimas 2 semanas Me he sentido incapaz de controlar mis preocupaciones"]
r2 = md.anova(prom_1_anx_2_pre, prom_1_anx_2_post)
#print(r2)


#Anx_3
prom_1_anx_3_pre = prom_1_pre["56 Durante las últimas 2 semanas Me he sentido tan inquieta(o) que no he podido quedarme quieta(o)"]
prom_1_anx_3_post = prom_1_post["56 Durante las últimas 2 semanas Me he sentido tan inquieta(o) que no he podido quedarme quieta(o)"]
r3 = md.anova(prom_1_anx_3_pre, prom_1_anx_3_post)
#print(r3)

#Anx_4
prom_1_anx_4_pre = prom_1_pre["57 Durante las últimas 2 semanas He tenido dificultad para relajarme"]
prom_1_anx_4_post = prom_1_post["57 Durante las últimas 2 semanas He tenido dificultad para relajarme"]
r4 = md.anova(prom_1_anx_4_pre, prom_1_anx_4_post)
#print(r4)


#Anx_5
prom_1_anx_5_pre = prom_1_pre["67 Durante las últimas 2 semanas Siento poco interés o placer en hacer cosas"]
prom_1_anx_5_post = prom_1_post["67 Durante las últimas 2 semanas Siento poco interés o placer en hacer cosas"]
r5 = md.anova(prom_1_anx_5_pre, prom_1_anx_5_post)
#print(r5)


#Anx_6
prom_1_anx_6_pre = prom_1_pre["68Durante las últimas 2 semanas Me he sentido decaída(o) deprimida(o) o sin esperanzas"]
prom_1_anx_6_post = prom_1_post["68Durante las últimas 2 semanas Me he sentido decaída(o) deprimida(o) o sin esperanzas"]
r6 = md.anova(prom_1_anx_6_pre, prom_1_anx_6_post)
#print(r6)

##############################################################################

#Stress

#Str_1
prom_1_str_1_pre = prom_1_pre["37. En el último mes Pienso o imagino, repetidamente, que voy a enfermar"]
prom_1_str_1_post = prom_1_post["37. En el último mes Pienso o imagino, repetidamente, que voy a enfermar"]
r7 = md.anova(prom_1_str_1_pre, prom_1_str_1_post)
#print(r7)


#Str_2
prom_1_str_2_pre = prom_1_pre["38. En el último mes Tengo pesadillas que se repiten acerca de la enfermedad"]
prom_1_str_2_post = prom_1_post["38. En el último mes Tengo pesadillas que se repiten acerca de la enfermedad"]
r8 = md.anova(prom_1_str_2_pre, prom_1_str_2_post)
#print(r8)


#Str_3
prom_1_str_3_pre = prom_1_pre["39 En el último mes Me siento preocupada(o) cuando se menciona la enfermedad"]
prom_1_str_3_post = prom_1_post["39 En el último mes Me siento preocupada(o) cuando se menciona la enfermedad"]
r9 = md.anova(prom_1_str_3_pre, prom_1_str_3_post)
#print(r9)

#Str_4
prom_1_str_4_pre = prom_1_pre["40 En el último mes Tengo reacciones físicas desagradable cuando pienso en la enfermedad (por ejemplo, latidos cardiacos muy fuertes, problemas para respirar, sudoración)"]
prom_1_str_4_post = prom_1_post["40 En el último mes Tengo reacciones físicas desagradable cuando pienso en la enfermedad (por ejemplo, latidos cardiacos muy fuertes, problemas para respirar, sudoración)"]
r10 = md.anova(prom_1_str_4_pre, prom_1_str_4_post)
#print(r10)


#Str_5
prom_1_str_5_pre = prom_1_pre["44 En el último mes Pienso que si me enfermo o se enferma alguien de mi familia, es por mi culpa"]
prom_1_str_5_post = prom_1_post["44 En el último mes Pienso que si me enfermo o se enferma alguien de mi familia, es por mi culpa"]
r11 = md.anova(prom_1_str_5_pre, prom_1_str_5_post)
#print(r11)


#Str_6
prom_1_str_6_pre = prom_1_pre["48 En el último mes Siento que mi futuro es incierto a partir de que comenzó el riesgo a padecer esta enfermedad"]
prom_1_str_6_post = prom_1_post["48 En el último mes Siento que mi futuro es incierto a partir de que comenzó el riesgo a padecer esta enfermedad"]
r12 = md.anova(prom_1_str_6_pre, prom_1_str_6_post)
#print(r12)

#Str_7
prom_1_str_7_pre = prom_1_pre["53 En el último mes Me siento asustada(o) por los riesgos a padecer esta enfermedad"]
prom_1_str_7_post = prom_1_post["53 En el último mes Me siento asustada(o) por los riesgos a padecer esta enfermedad"]
r13 = md.anova(prom_1_str_7_pre, prom_1_str_7_post)
#print(r13)


#################################################################################
#Avoidance
#Avo_1
prom_1_avo_1_pre = prom_1_pre["41.En el último mes Evito pensar, sentir o hablar sobre la enfermedad"]
prom_1_avo_1_post = prom_1_post["41.En el último mes Evito pensar, sentir o hablar sobre la enfermedad"]
r14 = md.anova(prom_1_avo_1_pre, prom_1_avo_1_post)
#print(r14)


#Avo_2
prom_1_avo_2_pre = prom_1_pre["42. En el último mes Evito ver o recurrir a información oficial sobre la enfermedad"]
prom_1_avo_2_post = prom_1_post["42. En el último mes Evito ver o recurrir a información oficial sobre la enfermedad"]
r15 = md.anova(prom_1_avo_2_pre, prom_1_avo_2_post)
#print(r15)


#Avo_3
prom_1_avo_3_pre = prom_1_pre["43. En el último mes Tengo dificultad para recordar lo que recomiendan las autoridades para enfrentar el riesgo o la enfermedad"]
prom_1_avo_3_post = prom_1_post["43. En el último mes Tengo dificultad para recordar lo que recomiendan las autoridades para enfrentar el riesgo o la enfermedad"]
r16 = md.anova(prom_1_avo_3_pre, prom_1_avo_3_post)
#print(r16)

###################################################################################

#Distancing
#Dis_1
prom_1_dis_1_pre = prom_1_pre["45. En el último mes He perdido interés por las actividades que antes disfrutaba"]
prom_1_dis_1_post = prom_1_post["45. En el último mes He perdido interés por las actividades que antes disfrutaba"]
r17 = md.anova(prom_1_dis_1_pre, prom_1_dis_1_post)
#print(r17)


#Dis_2
prom_1_dis_2_pre = prom_1_pre["46. En el último mes Me siento distante de las personas con quienes convivo, a partir de que inició el riesgo de esta enfermedad"]
prom_1_dis_2_post = prom_1_post["46. En el último mes Me siento distante de las personas con quienes convivo, a partir de que inició el riesgo de esta enfermedad"]
r18 = md.anova(prom_1_dis_2_pre, prom_1_dis_2_post)
#print(r18)


#Dis_3
prom_1_dis_3_pre = prom_1_pre["49. En el último mes Siento que deseo hacer cosas para hacerme daño"]
prom_1_dis_3_post = prom_1_post["49. En el último mes Siento que deseo hacer cosas para hacerme daño"]
r19 = md.anova(prom_1_dis_3_pre, prom_1_dis_3_post)
#print(r19)

#Dis_4
prom_1_dis_4_pre = prom_1_pre["50. En el último mes Tengo dificultad para quedarme dormido o seguir durmiendo"]
prom_1_dis_4_post = prom_1_post["50. En el último mes Tengo dificultad para quedarme dormido o seguir durmiendo"]
r20 = md.anova(prom_1_dis_4_pre, prom_1_dis_4_post)
#print(r20)


#Dis_5
prom_1_dis_5_pre = prom_1_pre["51. En el último mes Me siento enojada (o)"]
prom_1_dis_5_post = prom_1_post["51. En el último mes Me siento enojada (o)"]
r21 = md.anova(prom_1_dis_5_pre, prom_1_dis_5_post)
#print(r21)

#########################################################################


#Information seeking
#Inf_1
prom_1_inf_1_pre = prom_1_pre["64. Actualmente Leo (o me intereso por programas de televisión o radio) sobre enfermedades físicas graves"]
prom_1_inf_1_post = prom_1_post["64. Actualmente Leo (o me intereso por programas de televisión o radio) sobre enfermedades físicas graves"]
r22 = md.anova(prom_1_inf_1_pre, prom_1_inf_1_post)
#print(r22)

#Somatization
#Som_1
prom_1_som_1_pre = prom_1_pre["62. Actualmente Creo que padezco alguna enfermedad física grave (aunque no me la han confirmado)"]
prom_1_som_1_post = prom_1_post["62. Actualmente Creo que padezco alguna enfermedad física grave (aunque no me la han confirmado)"]
r23 = md.anova(prom_1_som_1_pre, prom_1_som_1_post)
#print(r23)

#########################################################################
print("fest_1")

#fest_1
#Anxiety
#Anx_1
fest_1_anx_1_pre = fest_1_pre["54 Durante las últimas 2 semanas Me he sentido nerviosa(o), ansiosa(o) o con los nervios de punta"]
fest_1_anx_1_post = fest_1_post["54 Durante las últimas 2 semanas Me he sentido nerviosa(o), ansiosa(o) o con los nervios de punta"]
r1 = md.anova(fest_1_anx_1_pre, fest_1_anx_1_post)
#print(r1)


#Anx_2
fest_1_anx_2_pre = fest_1_pre["55 Durante las últimas 2 semanas Me he sentido incapaz de controlar mis preocupaciones"]
fest_1_anx_2_post = fest_1_post["55 Durante las últimas 2 semanas Me he sentido incapaz de controlar mis preocupaciones"]
r2 = md.anova(fest_1_anx_2_pre, fest_1_anx_2_post)
#print(r2)


#Anx_3
fest_1_anx_3_pre = fest_1_pre["56 Durante las últimas 2 semanas Me he sentido tan inquieta(o) que no he podido quedarme quieta(o)"]
fest_1_anx_3_post = fest_1_post["56 Durante las últimas 2 semanas Me he sentido tan inquieta(o) que no he podido quedarme quieta(o)"]
r3 = md.anova(fest_1_anx_3_pre, fest_1_anx_3_post)
#print(r3)

#Anx_4
fest_1_anx_4_pre = fest_1_pre["57 Durante las últimas 2 semanas He tenido dificultad para relajarme"]
fest_1_anx_4_post = fest_1_post["57 Durante las últimas 2 semanas He tenido dificultad para relajarme"]
r4 = md.anova(fest_1_anx_4_pre, fest_1_anx_4_post)
#print(r4)


#Anx_5
fest_1_anx_5_pre = fest_1_pre["67 Durante las últimas 2 semanas Siento poco interés o placer en hacer cosas"]
fest_1_anx_5_post = fest_1_post["67 Durante las últimas 2 semanas Siento poco interés o placer en hacer cosas"]
r5 = md.anova(fest_1_anx_5_pre, fest_1_anx_5_post)
#print(r5)


#Anx_6
fest_1_anx_6_pre = fest_1_pre["68Durante las últimas 2 semanas Me he sentido decaída(o) deprimida(o) o sin esperanzas"]
fest_1_anx_6_post = fest_1_post["68Durante las últimas 2 semanas Me he sentido decaída(o) deprimida(o) o sin esperanzas"]
r6 = md.anova(fest_1_anx_6_pre, fest_1_anx_6_post)
#print(r6)

##############################################################################

#Stress

#Str_1
fest_1_str_1_pre = fest_1_pre["37. En el último mes Pienso o imagino, repetidamente, que voy a enfermar"]
fest_1_str_1_post = fest_1_post["37. En el último mes Pienso o imagino, repetidamente, que voy a enfermar"]
r7 = md.anova(fest_1_str_1_pre, fest_1_str_1_post)
#print(r7)


#Str_2
fest_1_str_2_pre = fest_1_pre["38. En el último mes Tengo pesadillas que se repiten acerca de la enfermedad"]
fest_1_str_2_post = fest_1_post["38. En el último mes Tengo pesadillas que se repiten acerca de la enfermedad"]
r8 = md.anova(fest_1_str_2_pre, fest_1_str_2_post)
#print(r8)


#Str_3
fest_1_str_3_pre = fest_1_pre["39 En el último mes Me siento preocupada(o) cuando se menciona la enfermedad"]
fest_1_str_3_post = fest_1_post["39 En el último mes Me siento preocupada(o) cuando se menciona la enfermedad"]
r9 = md.anova(fest_1_str_3_pre, fest_1_str_3_post)
#print(r9)

#Str_4
fest_1_str_4_pre = fest_1_pre["40 En el último mes Tengo reacciones físicas desagradable cuando pienso en la enfermedad (por ejemplo, latidos cardiacos muy fuertes, problemas para respirar, sudoración)"]
fest_1_str_4_post = fest_1_post["40 En el último mes Tengo reacciones físicas desagradable cuando pienso en la enfermedad (por ejemplo, latidos cardiacos muy fuertes, problemas para respirar, sudoración)"]
r10 = md.anova(fest_1_str_4_pre, fest_1_str_4_post)
#print(r10)


#Str_5
fest_1_str_5_pre = fest_1_pre["44 En el último mes Pienso que si me enfermo o se enferma alguien de mi familia, es por mi culpa"]
fest_1_str_5_post = fest_1_post["44 En el último mes Pienso que si me enfermo o se enferma alguien de mi familia, es por mi culpa"]
r11 = md.anova(fest_1_str_5_pre, fest_1_str_5_post)
#print(r11)


#Str_6
fest_1_str_6_pre = fest_1_pre["48 En el último mes Siento que mi futuro es incierto a partir de que comenzó el riesgo a padecer esta enfermedad"]
fest_1_str_6_post = fest_1_post["48 En el último mes Siento que mi futuro es incierto a partir de que comenzó el riesgo a padecer esta enfermedad"]
r12 = md.anova(fest_1_str_6_pre, fest_1_str_6_post)
#print(r12)

#Str_7
fest_1_str_7_pre = fest_1_pre["53 En el último mes Me siento asustada(o) por los riesgos a padecer esta enfermedad"]
fest_1_str_7_post = fest_1_post["53 En el último mes Me siento asustada(o) por los riesgos a padecer esta enfermedad"]
r13 = md.anova(fest_1_str_7_pre, fest_1_str_7_post)
#print(r13)


#################################################################################
#Avoidance
#Avo_1
fest_1_avo_1_pre = fest_1_pre["41.En el último mes Evito pensar, sentir o hablar sobre la enfermedad"]
fest_1_avo_1_post = fest_1_post["41.En el último mes Evito pensar, sentir o hablar sobre la enfermedad"]
r14 = md.anova(fest_1_avo_1_pre, fest_1_avo_1_post)
#print(r14)


#Avo_2
fest_1_avo_2_pre = fest_1_pre["42. En el último mes Evito ver o recurrir a información oficial sobre la enfermedad"]
fest_1_avo_2_post = fest_1_post["42. En el último mes Evito ver o recurrir a información oficial sobre la enfermedad"]
r15 = md.anova(fest_1_avo_2_pre, fest_1_avo_2_post)
#print(r15)


#Avo_3
fest_1_avo_3_pre = fest_1_pre["43. En el último mes Tengo dificultad para recordar lo que recomiendan las autoridades para enfrentar el riesgo o la enfermedad"]
fest_1_avo_3_post = fest_1_post["43. En el último mes Tengo dificultad para recordar lo que recomiendan las autoridades para enfrentar el riesgo o la enfermedad"]
r16 = md.anova(fest_1_avo_3_pre, fest_1_avo_3_post)
##print(r16)

###################################################################################

#Distancing
#Dis_1
fest_1_dis_1_pre = fest_1_pre["45. En el último mes He perdido interés por las actividades que antes disfrutaba"]
fest_1_dis_1_post = fest_1_post["45. En el último mes He perdido interés por las actividades que antes disfrutaba"]
r17 = md.anova(fest_1_dis_1_pre, fest_1_dis_1_post)
#print(r17)


#Dis_2
fest_1_dis_2_pre = fest_1_pre["46. En el último mes Me siento distante de las personas con quienes convivo, a partir de que inició el riesgo de esta enfermedad"]
fest_1_dis_2_post = fest_1_post["46. En el último mes Me siento distante de las personas con quienes convivo, a partir de que inició el riesgo de esta enfermedad"]
r18 = md.anova(fest_1_dis_2_pre, fest_1_dis_2_post)
#print(r18)


#Dis_3
fest_1_dis_3_pre = fest_1_pre["49. En el último mes Siento que deseo hacer cosas para hacerme daño"]
fest_1_dis_3_post = fest_1_post["49. En el último mes Siento que deseo hacer cosas para hacerme daño"]
r19 = md.anova(fest_1_dis_3_pre, fest_1_dis_3_post)
#print(r19)

#Dis_4
fest_1_dis_4_pre = fest_1_pre["50. En el último mes Tengo dificultad para quedarme dormido o seguir durmiendo"]
fest_1_dis_4_post = fest_1_post["50. En el último mes Tengo dificultad para quedarme dormido o seguir durmiendo"]
r20 = md.anova(fest_1_dis_4_pre, fest_1_dis_4_post)
#print(r20)


#Dis_5
fest_1_dis_5_pre = fest_1_pre["51. En el último mes Me siento enojada (o)"]
fest_1_dis_5_post = fest_1_post["51. En el último mes Me siento enojada (o)"]
r21 = md.anova(fest_1_dis_5_pre, fest_1_dis_5_post)
#print(r21)

#########################################################################


#Information seeking
#Inf_1
fest_1_inf_1_pre = fest_1_pre["64. Actualmente Leo (o me intereso por programas de televisión o radio) sobre enfermedades físicas graves"]
fest_1_inf_1_post = fest_1_post["64. Actualmente Leo (o me intereso por programas de televisión o radio) sobre enfermedades físicas graves"]
r22 = md.anova(fest_1_inf_1_pre, fest_1_inf_1_post)
#print(r22)

#Somatization
#Som_1
fest_1_som_1_pre = fest_1_pre["62. Actualmente Creo que padezco alguna enfermedad física grave (aunque no me la han confirmado)"]
fest_1_som_1_post = fest_1_post["62. Actualmente Creo que padezco alguna enfermedad física grave (aunque no me la han confirmado)"]
r23 = md.anova(fest_1_som_1_pre, fest_1_som_1_post)
#print(r23)

#############################################################################

print("anounc_2")

#anounc_2
#Anxiety
#Anx_1
anounc_2_anx_1_pre = anounc_2_pre["54 Durante las últimas 2 semanas Me he sentido nerviosa(o), ansiosa(o) o con los nervios de punta"]
anounc_2_anx_1_post = anounc_2_post["54 Durante las últimas 2 semanas Me he sentido nerviosa(o), ansiosa(o) o con los nervios de punta"]
r1 = md.anova(anounc_2_anx_1_pre, anounc_2_anx_1_post)
#print(r1)


#Anx_2
anounc_2_anx_2_pre = anounc_2_pre["55 Durante las últimas 2 semanas Me he sentido incapaz de controlar mis preocupaciones"]
anounc_2_anx_2_post = anounc_2_post["55 Durante las últimas 2 semanas Me he sentido incapaz de controlar mis preocupaciones"]
r2 = md.anova(anounc_2_anx_2_pre, anounc_2_anx_2_post)
#print(r2)


#Anx_3
anounc_2_anx_3_pre = anounc_2_pre["56 Durante las últimas 2 semanas Me he sentido tan inquieta(o) que no he podido quedarme quieta(o)"]
anounc_2_anx_3_post = anounc_2_post["56 Durante las últimas 2 semanas Me he sentido tan inquieta(o) que no he podido quedarme quieta(o)"]
r3 = md.anova(anounc_2_anx_3_pre, anounc_2_anx_3_post)
#print(r3)

#Anx_4
anounc_2_anx_4_pre = anounc_2_pre["57 Durante las últimas 2 semanas He tenido dificultad para relajarme"]
anounc_2_anx_4_post = anounc_2_post["57 Durante las últimas 2 semanas He tenido dificultad para relajarme"]
r4 = md.anova(anounc_2_anx_4_pre, anounc_2_anx_4_post)
#print(r4)


#Anx_5
anounc_2_anx_5_pre = anounc_2_pre["67 Durante las últimas 2 semanas Siento poco interés o placer en hacer cosas"]
anounc_2_anx_5_post = anounc_2_post["67 Durante las últimas 2 semanas Siento poco interés o placer en hacer cosas"]
r5 = md.anova(anounc_2_anx_5_pre, anounc_2_anx_5_post)
#print(r5)


#Anx_6
anounc_2_anx_6_pre = anounc_2_pre["68Durante las últimas 2 semanas Me he sentido decaída(o) deprimida(o) o sin esperanzas"]
anounc_2_anx_6_post = anounc_2_post["68Durante las últimas 2 semanas Me he sentido decaída(o) deprimida(o) o sin esperanzas"]
r6 = md.anova(anounc_2_anx_6_pre, anounc_2_anx_6_post)
#print(r6)

##############################################################################

#Stress

#Str_1
anounc_2_str_1_pre = anounc_2_pre["37. En el último mes Pienso o imagino, repetidamente, que voy a enfermar"]
anounc_2_str_1_post = anounc_2_post["37. En el último mes Pienso o imagino, repetidamente, que voy a enfermar"]
r7 = md.anova(anounc_2_str_1_pre, anounc_2_str_1_post)
#print(r7)


#Str_2
anounc_2_str_2_pre = anounc_2_pre["38. En el último mes Tengo pesadillas que se repiten acerca de la enfermedad"]
anounc_2_str_2_post = anounc_2_post["38. En el último mes Tengo pesadillas que se repiten acerca de la enfermedad"]
r8 = md.anova(anounc_2_str_2_pre, anounc_2_str_2_post)
#print(r8)


#Str_3
anounc_2_str_3_pre = anounc_2_pre["39 En el último mes Me siento preocupada(o) cuando se menciona la enfermedad"]
anounc_2_str_3_post = anounc_2_post["39 En el último mes Me siento preocupada(o) cuando se menciona la enfermedad"]
r9 = md.anova(anounc_2_str_3_pre, anounc_2_str_3_post)
#print(r9)

#Str_4
anounc_2_str_4_pre = anounc_2_pre["40 En el último mes Tengo reacciones físicas desagradable cuando pienso en la enfermedad (por ejemplo, latidos cardiacos muy fuertes, problemas para respirar, sudoración)"]
anounc_2_str_4_post = anounc_2_post["40 En el último mes Tengo reacciones físicas desagradable cuando pienso en la enfermedad (por ejemplo, latidos cardiacos muy fuertes, problemas para respirar, sudoración)"]
r10 = md.anova(anounc_2_str_4_pre, anounc_2_str_4_post)
#print(r10)


#Str_5
anounc_2_str_5_pre = anounc_2_pre["44 En el último mes Pienso que si me enfermo o se enferma alguien de mi familia, es por mi culpa"]
anounc_2_str_5_post = anounc_2_post["44 En el último mes Pienso que si me enfermo o se enferma alguien de mi familia, es por mi culpa"]
r11 = md.anova(anounc_2_str_5_pre, anounc_2_str_5_post)
#print(r11)


#Str_6
anounc_2_str_6_pre = anounc_2_pre["48 En el último mes Siento que mi futuro es incierto a partir de que comenzó el riesgo a padecer esta enfermedad"]
anounc_2_str_6_post = anounc_2_post["48 En el último mes Siento que mi futuro es incierto a partir de que comenzó el riesgo a padecer esta enfermedad"]
r12 = md.anova(anounc_2_str_6_pre, anounc_2_str_6_post)
#print(r12)

#Str_7
anounc_2_str_7_pre = anounc_2_pre["53 En el último mes Me siento asustada(o) por los riesgos a padecer esta enfermedad"]
anounc_2_str_7_post = anounc_2_post["53 En el último mes Me siento asustada(o) por los riesgos a padecer esta enfermedad"]
r13 = md.anova(anounc_2_str_7_pre, anounc_2_str_7_post)
#print(r13)


#################################################################################
#Avoidance
#Avo_1
anounc_2_avo_1_pre = anounc_2_pre["41.En el último mes Evito pensar, sentir o hablar sobre la enfermedad"]
anounc_2_avo_1_post = anounc_2_post["41.En el último mes Evito pensar, sentir o hablar sobre la enfermedad"]
r14 = md.anova(anounc_2_avo_1_pre, anounc_2_avo_1_post)
#print(r14)


#Avo_2
anounc_2_avo_2_pre = anounc_2_pre["42. En el último mes Evito ver o recurrir a información oficial sobre la enfermedad"]
anounc_2_avo_2_post = anounc_2_post["42. En el último mes Evito ver o recurrir a información oficial sobre la enfermedad"]
r15 = md.anova(anounc_2_avo_2_pre, anounc_2_avo_2_post)
#print(r15)


#Avo_3
anounc_2_avo_3_pre = anounc_2_pre["43. En el último mes Tengo dificultad para recordar lo que recomiendan las autoridades para enfrentar el riesgo o la enfermedad"]
anounc_2_avo_3_post = anounc_2_post["43. En el último mes Tengo dificultad para recordar lo que recomiendan las autoridades para enfrentar el riesgo o la enfermedad"]
r16 = md.anova(anounc_2_avo_3_pre, anounc_2_avo_3_post)
#print(r16)

###################################################################################

#Distancing
#Dis_1
anounc_2_dis_1_pre = anounc_2_pre["45. En el último mes He perdido interés por las actividades que antes disfrutaba"]
anounc_2_dis_1_post = anounc_2_post["45. En el último mes He perdido interés por las actividades que antes disfrutaba"]
r17 = md.anova(anounc_2_dis_1_pre, anounc_2_dis_1_post)
#print(r17)


#Dis_2
anounc_2_dis_2_pre = anounc_2_pre["46. En el último mes Me siento distante de las personas con quienes convivo, a partir de que inició el riesgo de esta enfermedad"]
anounc_2_dis_2_post = anounc_2_post["46. En el último mes Me siento distante de las personas con quienes convivo, a partir de que inició el riesgo de esta enfermedad"]
r18 = md.anova(anounc_2_dis_2_pre, anounc_2_dis_2_post)
#print(r18)


#Dis_3
anounc_2_dis_3_pre = anounc_2_pre["49. En el último mes Siento que deseo hacer cosas para hacerme daño"]
anounc_2_dis_3_post = anounc_2_post["49. En el último mes Siento que deseo hacer cosas para hacerme daño"]
r19 = md.anova(anounc_2_dis_3_pre, anounc_2_dis_3_post)
#print(r19)

#Dis_4
anounc_2_dis_4_pre = anounc_2_pre["50. En el último mes Tengo dificultad para quedarme dormido o seguir durmiendo"]
anounc_2_dis_4_post = anounc_2_post["50. En el último mes Tengo dificultad para quedarme dormido o seguir durmiendo"]
r20 = md.anova(anounc_2_dis_4_pre, anounc_2_dis_4_post)
#print(r20)


#Dis_5
anounc_2_dis_5_pre = anounc_2_pre["51. En el último mes Me siento enojada (o)"]
anounc_2_dis_5_post = anounc_2_post["51. En el último mes Me siento enojada (o)"]
r21 = md.anova(anounc_2_dis_5_pre, anounc_2_dis_5_post)
#print(r21)

#########################################################################


#Information seeking
#Inf_1
anounc_2_inf_1_pre = anounc_2_pre["64. Actualmente Leo (o me intereso por programas de televisión o radio) sobre enfermedades físicas graves"]
anounc_2_inf_1_post = anounc_2_post["64. Actualmente Leo (o me intereso por programas de televisión o radio) sobre enfermedades físicas graves"]
r22 = md.anova(anounc_2_inf_1_pre, anounc_2_inf_1_post)
#print(r22)

#Somatization
#Som_1
anounc_2_som_1_pre = anounc_2_pre["62. Actualmente Creo que padezco alguna enfermedad física grave (aunque no me la han confirmado)"]
anounc_2_som_1_post = anounc_2_post["62. Actualmente Creo que padezco alguna enfermedad física grave (aunque no me la han confirmado)"]
r23 = md.anova(anounc_2_som_1_pre, anounc_2_som_1_post)
#print(r23)

##########################################################################

print("measures_2")

#measures_2
#Anxiety
#Anx_1
measures_2_anx_1_pre = measures_2_pre["54 Durante las últimas 2 semanas Me he sentido nerviosa(o), ansiosa(o) o con los nervios de punta"]
measures_2_anx_1_post = measures_2_post["54 Durante las últimas 2 semanas Me he sentido nerviosa(o), ansiosa(o) o con los nervios de punta"]
r1 = md.anova(measures_2_anx_1_pre, measures_2_anx_1_post)
#print(r1)


#Anx_2
measures_2_anx_2_pre = measures_2_pre["55 Durante las últimas 2 semanas Me he sentido incapaz de controlar mis preocupaciones"]
measures_2_anx_2_post = measures_2_post["55 Durante las últimas 2 semanas Me he sentido incapaz de controlar mis preocupaciones"]
r2 = md.anova(measures_2_anx_2_pre, measures_2_anx_2_post)
#print(r2)


#Anx_3
measures_2_anx_3_pre = measures_2_pre["56 Durante las últimas 2 semanas Me he sentido tan inquieta(o) que no he podido quedarme quieta(o)"]
measures_2_anx_3_post = measures_2_post["56 Durante las últimas 2 semanas Me he sentido tan inquieta(o) que no he podido quedarme quieta(o)"]
r3 = md.anova(measures_2_anx_3_pre, measures_2_anx_3_post)
#print(r3)

#Anx_4
measures_2_anx_4_pre = measures_2_pre["57 Durante las últimas 2 semanas He tenido dificultad para relajarme"]
measures_2_anx_4_post = measures_2_post["57 Durante las últimas 2 semanas He tenido dificultad para relajarme"]
r4 = md.anova(measures_2_anx_4_pre, measures_2_anx_4_post)
#print(r4)


#Anx_5
measures_2_anx_5_pre = measures_2_pre["67 Durante las últimas 2 semanas Siento poco interés o placer en hacer cosas"]
measures_2_anx_5_post = measures_2_post["67 Durante las últimas 2 semanas Siento poco interés o placer en hacer cosas"]
r5 = md.anova(measures_2_anx_5_pre, measures_2_anx_5_post)
#print(r5)


#Anx_6
measures_2_anx_6_pre = measures_2_pre["68Durante las últimas 2 semanas Me he sentido decaída(o) deprimida(o) o sin esperanzas"]
measures_2_anx_6_post = measures_2_post["68Durante las últimas 2 semanas Me he sentido decaída(o) deprimida(o) o sin esperanzas"]
r6 = md.anova(measures_2_anx_6_pre, measures_2_anx_6_post)
#print(r6)

##############################################################################

#Stress

#Str_1
measures_2_str_1_pre = measures_2_pre["37. En el último mes Pienso o imagino, repetidamente, que voy a enfermar"]
measures_2_str_1_post = measures_2_post["37. En el último mes Pienso o imagino, repetidamente, que voy a enfermar"]
r7 = md.anova(measures_2_str_1_pre, measures_2_str_1_post)
#print(r7)


#Str_2
measures_2_str_2_pre = measures_2_pre["38. En el último mes Tengo pesadillas que se repiten acerca de la enfermedad"]
measures_2_str_2_post = measures_2_post["38. En el último mes Tengo pesadillas que se repiten acerca de la enfermedad"]
r8 = md.anova(measures_2_str_2_pre, measures_2_str_2_post)
#print(r8)


#Str_3
measures_2_str_3_pre = measures_2_pre["39 En el último mes Me siento preocupada(o) cuando se menciona la enfermedad"]
measures_2_str_3_post = measures_2_post["39 En el último mes Me siento preocupada(o) cuando se menciona la enfermedad"]
r9 = md.anova(measures_2_str_3_pre, measures_2_str_3_post)
#print(r9)

#Str_4
measures_2_str_4_pre = measures_2_pre["40 En el último mes Tengo reacciones físicas desagradable cuando pienso en la enfermedad (por ejemplo, latidos cardiacos muy fuertes, problemas para respirar, sudoración)"]
measures_2_str_4_post = measures_2_post["40 En el último mes Tengo reacciones físicas desagradable cuando pienso en la enfermedad (por ejemplo, latidos cardiacos muy fuertes, problemas para respirar, sudoración)"]
r10 = md.anova(measures_2_str_4_pre, measures_2_str_4_post)
#print(r10)


#Str_5
measures_2_str_5_pre = measures_2_pre["44 En el último mes Pienso que si me enfermo o se enferma alguien de mi familia, es por mi culpa"]
measures_2_str_5_post = measures_2_post["44 En el último mes Pienso que si me enfermo o se enferma alguien de mi familia, es por mi culpa"]
r11 = md.anova(measures_2_str_5_pre, measures_2_str_5_post)
#print(r11)


#Str_6
measures_2_str_6_pre = measures_2_pre["48 En el último mes Siento que mi futuro es incierto a partir de que comenzó el riesgo a padecer esta enfermedad"]
measures_2_str_6_post = measures_2_post["48 En el último mes Siento que mi futuro es incierto a partir de que comenzó el riesgo a padecer esta enfermedad"]
r12 = md.anova(measures_2_str_6_pre, measures_2_str_6_post)
#print(r12)

#Str_7
measures_2_str_7_pre = measures_2_pre["53 En el último mes Me siento asustada(o) por los riesgos a padecer esta enfermedad"]
measures_2_str_7_post = measures_2_post["53 En el último mes Me siento asustada(o) por los riesgos a padecer esta enfermedad"]
r13 = md.anova(measures_2_str_7_pre, measures_2_str_7_post)
#print(r13)


#################################################################################
#Avoidance
#Avo_1
measures_2_avo_1_pre = measures_2_pre["41.En el último mes Evito pensar, sentir o hablar sobre la enfermedad"]
measures_2_avo_1_post = measures_2_post["41.En el último mes Evito pensar, sentir o hablar sobre la enfermedad"]
r14 = md.anova(measures_2_avo_1_pre, measures_2_avo_1_post)
#print(r14)


#Avo_2
measures_2_avo_2_pre = measures_2_pre["42. En el último mes Evito ver o recurrir a información oficial sobre la enfermedad"]
measures_2_avo_2_post = measures_2_post["42. En el último mes Evito ver o recurrir a información oficial sobre la enfermedad"]
r15 = md.anova(measures_2_avo_2_pre, measures_2_avo_2_post)
#print(r15)


#Avo_3
measures_2_avo_3_pre = measures_2_pre["43. En el último mes Tengo dificultad para recordar lo que recomiendan las autoridades para enfrentar el riesgo o la enfermedad"]
measures_2_avo_3_post = measures_2_post["43. En el último mes Tengo dificultad para recordar lo que recomiendan las autoridades para enfrentar el riesgo o la enfermedad"]
r16 = md.anova(measures_2_avo_3_pre, measures_2_avo_3_post)
#print(r16)

###################################################################################

#Distancing
#Dis_1
measures_2_dis_1_pre = measures_2_pre["45. En el último mes He perdido interés por las actividades que antes disfrutaba"]
measures_2_dis_1_post = measures_2_post["45. En el último mes He perdido interés por las actividades que antes disfrutaba"]
r17 = md.anova(measures_2_dis_1_pre, measures_2_dis_1_post)
#print(r17)


#Dis_2
measures_2_dis_2_pre = measures_2_pre["46. En el último mes Me siento distante de las personas con quienes convivo, a partir de que inició el riesgo de esta enfermedad"]
measures_2_dis_2_post = measures_2_post["46. En el último mes Me siento distante de las personas con quienes convivo, a partir de que inició el riesgo de esta enfermedad"]
r18 = md.anova(measures_2_dis_2_pre, measures_2_dis_2_post)
#print(r18)


#Dis_3
measures_2_dis_3_pre = measures_2_pre["49. En el último mes Siento que deseo hacer cosas para hacerme daño"]
measures_2_dis_3_post = measures_2_post["49. En el último mes Siento que deseo hacer cosas para hacerme daño"]
r19 = md.anova(measures_2_dis_3_pre, measures_2_dis_3_post)
#print(r19)

#Dis_4
measures_2_dis_4_pre = measures_2_pre["50. En el último mes Tengo dificultad para quedarme dormido o seguir durmiendo"]
measures_2_dis_4_post = measures_2_post["50. En el último mes Tengo dificultad para quedarme dormido o seguir durmiendo"]
r20 = md.anova(measures_2_dis_4_pre, measures_2_dis_4_post)
#print(r20)


#Dis_5
measures_2_dis_5_pre = measures_2_pre["51. En el último mes Me siento enojada (o)"]
measures_2_dis_5_post = measures_2_post["51. En el último mes Me siento enojada (o)"]
r21 = md.anova(measures_2_dis_5_pre, measures_2_dis_5_post)
#print(r21)

#########################################################################


#Information seeking
#Inf_1
measures_2_inf_1_pre = measures_2_pre["64. Actualmente Leo (o me intereso por programas de televisión o radio) sobre enfermedades físicas graves"]
measures_2_inf_1_post = measures_2_post["64. Actualmente Leo (o me intereso por programas de televisión o radio) sobre enfermedades físicas graves"]
r22 = md.anova(measures_2_inf_1_pre, measures_2_inf_1_post)
#print(r22)

#Somatization
#Som_1
measures_2_som_1_pre = measures_2_pre["62. Actualmente Creo que padezco alguna enfermedad física grave (aunque no me la han confirmado)"]
measures_2_som_1_post = measures_2_post["62. Actualmente Creo que padezco alguna enfermedad física grave (aunque no me la han confirmado)"]
r23 = md.anova(measures_2_som_1_pre, measures_2_som_1_post)
#print(r23)

#################################################################################
print("earth_vs_1")


#earth_vs_1
#Anxiety
#Anx_1
earth_vs_1_anx_1_pre = earth_vs_1_pre["54 Durante las últimas 2 semanas Me he sentido nerviosa(o), ansiosa(o) o con los nervios de punta"]
earth_vs_1_anx_1_post = earth_vs_1_post["54 Durante las últimas 2 semanas Me he sentido nerviosa(o), ansiosa(o) o con los nervios de punta"]
r1 = md.anova(earth_vs_1_anx_1_pre, earth_vs_1_anx_1_post)
#print(r1)


#Anx_2
earth_vs_1_anx_2_pre = earth_vs_1_pre["55 Durante las últimas 2 semanas Me he sentido incapaz de controlar mis preocupaciones"]
earth_vs_1_anx_2_post = earth_vs_1_post["55 Durante las últimas 2 semanas Me he sentido incapaz de controlar mis preocupaciones"]
r2 = md.anova(earth_vs_1_anx_2_pre, earth_vs_1_anx_2_post)
#print(r2)


#Anx_3
earth_vs_1_anx_3_pre = earth_vs_1_pre["56 Durante las últimas 2 semanas Me he sentido tan inquieta(o) que no he podido quedarme quieta(o)"]
earth_vs_1_anx_3_post = earth_vs_1_post["56 Durante las últimas 2 semanas Me he sentido tan inquieta(o) que no he podido quedarme quieta(o)"]
r3 = md.anova(earth_vs_1_anx_3_pre, earth_vs_1_anx_3_post)
#print(r3)

#Anx_4
earth_vs_1_anx_4_pre = earth_vs_1_pre["57 Durante las últimas 2 semanas He tenido dificultad para relajarme"]
earth_vs_1_anx_4_post = earth_vs_1_post["57 Durante las últimas 2 semanas He tenido dificultad para relajarme"]
r4 = md.anova(earth_vs_1_anx_4_pre, earth_vs_1_anx_4_post)
#print(r4)


#Anx_5
earth_vs_1_anx_5_pre = earth_vs_1_pre["67 Durante las últimas 2 semanas Siento poco interés o placer en hacer cosas"]
earth_vs_1_anx_5_post = earth_vs_1_post["67 Durante las últimas 2 semanas Siento poco interés o placer en hacer cosas"]
r5 = md.anova(earth_vs_1_anx_5_pre, earth_vs_1_anx_5_post)
#print(r5)


#Anx_6
earth_vs_1_anx_6_pre = earth_vs_1_pre["68Durante las últimas 2 semanas Me he sentido decaída(o) deprimida(o) o sin esperanzas"]
earth_vs_1_anx_6_post = earth_vs_1_post["68Durante las últimas 2 semanas Me he sentido decaída(o) deprimida(o) o sin esperanzas"]
r6 = md.anova(earth_vs_1_anx_6_pre, earth_vs_1_anx_6_post)
#print(r6)

##############################################################################

#Stress

#Str_1
earth_vs_1_str_1_pre = earth_vs_1_pre["37. En el último mes Pienso o imagino, repetidamente, que voy a enfermar"]
earth_vs_1_str_1_post = earth_vs_1_post["37. En el último mes Pienso o imagino, repetidamente, que voy a enfermar"]
r7 = md.anova(earth_vs_1_str_1_pre, earth_vs_1_str_1_post)
#print(r7)


#Str_2
earth_vs_1_str_2_pre = earth_vs_1_pre["38. En el último mes Tengo pesadillas que se repiten acerca de la enfermedad"]
earth_vs_1_str_2_post = earth_vs_1_post["38. En el último mes Tengo pesadillas que se repiten acerca de la enfermedad"]
r8 = md.anova(earth_vs_1_str_2_pre, earth_vs_1_str_2_post)
#print(r8)


#Str_3
earth_vs_1_str_3_pre = earth_vs_1_pre["39 En el último mes Me siento preocupada(o) cuando se menciona la enfermedad"]
earth_vs_1_str_3_post = earth_vs_1_post["39 En el último mes Me siento preocupada(o) cuando se menciona la enfermedad"]
r9 = md.anova(earth_vs_1_str_3_pre, earth_vs_1_str_3_post)
#print(r9)

#Str_4
earth_vs_1_str_4_pre = earth_vs_1_pre["40 En el último mes Tengo reacciones físicas desagradable cuando pienso en la enfermedad (por ejemplo, latidos cardiacos muy fuertes, problemas para respirar, sudoración)"]
earth_vs_1_str_4_post = earth_vs_1_post["40 En el último mes Tengo reacciones físicas desagradable cuando pienso en la enfermedad (por ejemplo, latidos cardiacos muy fuertes, problemas para respirar, sudoración)"]
r10 = md.anova(earth_vs_1_str_4_pre, earth_vs_1_str_4_post)
#print(r10)


#Str_5
earth_vs_1_str_5_pre = earth_vs_1_pre["44 En el último mes Pienso que si me enfermo o se enferma alguien de mi familia, es por mi culpa"]
earth_vs_1_str_5_post = earth_vs_1_post["44 En el último mes Pienso que si me enfermo o se enferma alguien de mi familia, es por mi culpa"]
r11 = md.anova(earth_vs_1_str_5_pre, earth_vs_1_str_5_post)
#print(r11)


#Str_6
earth_vs_1_str_6_pre = earth_vs_1_pre["48 En el último mes Siento que mi futuro es incierto a partir de que comenzó el riesgo a padecer esta enfermedad"]
earth_vs_1_str_6_post = earth_vs_1_post["48 En el último mes Siento que mi futuro es incierto a partir de que comenzó el riesgo a padecer esta enfermedad"]
r12 = md.anova(earth_vs_1_str_6_pre, earth_vs_1_str_6_post)
#print(r12)

#Str_7
earth_vs_1_str_7_pre = earth_vs_1_pre["53 En el último mes Me siento asustada(o) por los riesgos a padecer esta enfermedad"]
earth_vs_1_str_7_post = earth_vs_1_post["53 En el último mes Me siento asustada(o) por los riesgos a padecer esta enfermedad"]
r13 = md.anova(earth_vs_1_str_7_pre, earth_vs_1_str_7_post)
#print(r13)


#################################################################################
#Avoidance
#Avo_1
earth_vs_1_avo_1_pre = earth_vs_1_pre["41.En el último mes Evito pensar, sentir o hablar sobre la enfermedad"]
earth_vs_1_avo_1_post = earth_vs_1_post["41.En el último mes Evito pensar, sentir o hablar sobre la enfermedad"]
r14 = md.anova(earth_vs_1_avo_1_pre, earth_vs_1_avo_1_post)
#print(r14)


#Avo_2
earth_vs_1_avo_2_pre = earth_vs_1_pre["42. En el último mes Evito ver o recurrir a información oficial sobre la enfermedad"]
earth_vs_1_avo_2_post = earth_vs_1_post["42. En el último mes Evito ver o recurrir a información oficial sobre la enfermedad"]
r15 = md.anova(earth_vs_1_avo_2_pre, earth_vs_1_avo_2_post)
#print(r15)


#Avo_3
earth_vs_1_avo_3_pre = earth_vs_1_pre["43. En el último mes Tengo dificultad para recordar lo que recomiendan las autoridades para enfrentar el riesgo o la enfermedad"]
earth_vs_1_avo_3_post = earth_vs_1_post["43. En el último mes Tengo dificultad para recordar lo que recomiendan las autoridades para enfrentar el riesgo o la enfermedad"]
r16 = md.anova(earth_vs_1_avo_3_pre, earth_vs_1_avo_3_post)
#print(r16)

###################################################################################

#Distancing
#Dis_1
earth_vs_1_dis_1_pre = earth_vs_1_pre["45. En el último mes He perdido interés por las actividades que antes disfrutaba"]
earth_vs_1_dis_1_post = earth_vs_1_post["45. En el último mes He perdido interés por las actividades que antes disfrutaba"]
r17 = md.anova(earth_vs_1_dis_1_pre, earth_vs_1_dis_1_post)
#print(r17)


#Dis_2
earth_vs_1_dis_2_pre = earth_vs_1_pre["46. En el último mes Me siento distante de las personas con quienes convivo, a partir de que inició el riesgo de esta enfermedad"]
earth_vs_1_dis_2_post = earth_vs_1_post["46. En el último mes Me siento distante de las personas con quienes convivo, a partir de que inició el riesgo de esta enfermedad"]
r18 = md.anova(earth_vs_1_dis_2_pre, earth_vs_1_dis_2_post)
#print(r18)


#Dis_3
earth_vs_1_dis_3_pre = earth_vs_1_pre["49. En el último mes Siento que deseo hacer cosas para hacerme daño"]
earth_vs_1_dis_3_post = earth_vs_1_post["49. En el último mes Siento que deseo hacer cosas para hacerme daño"]
r19 = md.anova(earth_vs_1_dis_3_pre, earth_vs_1_dis_3_post)
#print(r19)

#Dis_4
earth_vs_1_dis_4_pre = earth_vs_1_pre["50. En el último mes Tengo dificultad para quedarme dormido o seguir durmiendo"]
earth_vs_1_dis_4_post = earth_vs_1_post["50. En el último mes Tengo dificultad para quedarme dormido o seguir durmiendo"]
r20 = md.anova(earth_vs_1_dis_4_pre, earth_vs_1_dis_4_post)
#print(r20)


#Dis_5
earth_vs_1_dis_5_pre = earth_vs_1_pre["51. En el último mes Me siento enojada (o)"]
earth_vs_1_dis_5_post = earth_vs_1_post["51. En el último mes Me siento enojada (o)"]
r21 = md.anova(earth_vs_1_dis_5_pre, earth_vs_1_dis_5_post)
#print(r21)

#########################################################################


#Information seeking
#Inf_1
earth_vs_1_inf_1_pre = earth_vs_1_pre["64. Actualmente Leo (o me intereso por programas de televisión o radio) sobre enfermedades físicas graves"]
earth_vs_1_inf_1_post = earth_vs_1_post["64. Actualmente Leo (o me intereso por programas de televisión o radio) sobre enfermedades físicas graves"]
r22 = md.anova(earth_vs_1_inf_1_pre, earth_vs_1_inf_1_post)
#print(r22)

#Somatization
#Som_1
earth_vs_1_som_1_pre = earth_vs_1_pre["62. Actualmente Creo que padezco alguna enfermedad física grave (aunque no me la han confirmado)"]
earth_vs_1_som_1_post = earth_vs_1_post["62. Actualmente Creo que padezco alguna enfermedad física grave (aunque no me la han confirmado)"]
r23 = md.anova(earth_vs_1_som_1_pre, earth_vs_1_som_1_post)
#print(r23)


###########################################################################

print("anounc_3")

#anounc_3
#Anxiety
#Anx_1
anounc_3_anx_1_pre = anounc_3_pre["54 Durante las últimas 2 semanas Me he sentido nerviosa(o), ansiosa(o) o con los nervios de punta"]
anounc_3_anx_1_post = anounc_3_post["54 Durante las últimas 2 semanas Me he sentido nerviosa(o), ansiosa(o) o con los nervios de punta"]
r1 = md.anova(anounc_3_anx_1_pre, anounc_3_anx_1_post)
#print(r1)


#Anx_2
anounc_3_anx_2_pre = anounc_3_pre["55 Durante las últimas 2 semanas Me he sentido incapaz de controlar mis preocupaciones"]
anounc_3_anx_2_post = anounc_3_post["55 Durante las últimas 2 semanas Me he sentido incapaz de controlar mis preocupaciones"]
r2 = md.anova(anounc_3_anx_2_pre, anounc_3_anx_2_post)
#print(r2)


#Anx_3
anounc_3_anx_3_pre = anounc_3_pre["56 Durante las últimas 2 semanas Me he sentido tan inquieta(o) que no he podido quedarme quieta(o)"]
anounc_3_anx_3_post = anounc_3_post["56 Durante las últimas 2 semanas Me he sentido tan inquieta(o) que no he podido quedarme quieta(o)"]
r3 = md.anova(anounc_3_anx_3_pre, anounc_3_anx_3_post)
#print(r3)

#Anx_4
anounc_3_anx_4_pre = anounc_3_pre["57 Durante las últimas 2 semanas He tenido dificultad para relajarme"]
anounc_3_anx_4_post = anounc_3_post["57 Durante las últimas 2 semanas He tenido dificultad para relajarme"]
r4 = md.anova(anounc_3_anx_4_pre, anounc_3_anx_4_post)
#print(r4)


#Anx_5
anounc_3_anx_5_pre = anounc_3_pre["67 Durante las últimas 2 semanas Siento poco interés o placer en hacer cosas"]
anounc_3_anx_5_post = anounc_3_post["67 Durante las últimas 2 semanas Siento poco interés o placer en hacer cosas"]
r5 = md.anova(anounc_3_anx_5_pre, anounc_3_anx_5_post)
#print(r5)


#Anx_6
anounc_3_anx_6_pre = anounc_3_pre["68Durante las últimas 2 semanas Me he sentido decaída(o) deprimida(o) o sin esperanzas"]
anounc_3_anx_6_post = anounc_3_post["68Durante las últimas 2 semanas Me he sentido decaída(o) deprimida(o) o sin esperanzas"]
r6 = md.anova(anounc_3_anx_6_pre, anounc_3_anx_6_post)
#print(r6)

##############################################################################

#Stress

#Str_1
anounc_3_str_1_pre = anounc_3_pre["37. En el último mes Pienso o imagino, repetidamente, que voy a enfermar"]
anounc_3_str_1_post = anounc_3_post["37. En el último mes Pienso o imagino, repetidamente, que voy a enfermar"]
r7 = md.anova(anounc_3_str_1_pre, anounc_3_str_1_post)
#print(r7)


#Str_2
anounc_3_str_2_pre = anounc_3_pre["38. En el último mes Tengo pesadillas que se repiten acerca de la enfermedad"]
anounc_3_str_2_post = anounc_3_post["38. En el último mes Tengo pesadillas que se repiten acerca de la enfermedad"]
r8 = md.anova(anounc_3_str_2_pre, anounc_3_str_2_post)
#print(r8)


#Str_3
anounc_3_str_3_pre = anounc_3_pre["39 En el último mes Me siento preocupada(o) cuando se menciona la enfermedad"]
anounc_3_str_3_post = anounc_3_post["39 En el último mes Me siento preocupada(o) cuando se menciona la enfermedad"]
r9 = md.anova(anounc_3_str_3_pre, anounc_3_str_3_post)
#print(r9)

#Str_4
anounc_3_str_4_pre = anounc_3_pre["40 En el último mes Tengo reacciones físicas desagradable cuando pienso en la enfermedad (por ejemplo, latidos cardiacos muy fuertes, problemas para respirar, sudoración)"]
anounc_3_str_4_post = anounc_3_post["40 En el último mes Tengo reacciones físicas desagradable cuando pienso en la enfermedad (por ejemplo, latidos cardiacos muy fuertes, problemas para respirar, sudoración)"]
r10 = md.anova(anounc_3_str_4_pre, anounc_3_str_4_post)
#print(r10)


#Str_5
anounc_3_str_5_pre = anounc_3_pre["44 En el último mes Pienso que si me enfermo o se enferma alguien de mi familia, es por mi culpa"]
anounc_3_str_5_post = anounc_3_post["44 En el último mes Pienso que si me enfermo o se enferma alguien de mi familia, es por mi culpa"]
r11 = md.anova(anounc_3_str_5_pre, anounc_3_str_5_post)
#print(r11)


#Str_6
anounc_3_str_6_pre = anounc_3_pre["48 En el último mes Siento que mi futuro es incierto a partir de que comenzó el riesgo a padecer esta enfermedad"]
anounc_3_str_6_post = anounc_3_post["48 En el último mes Siento que mi futuro es incierto a partir de que comenzó el riesgo a padecer esta enfermedad"]
r12 = md.anova(anounc_3_str_6_pre, anounc_3_str_6_post)
#print(r12)

#Str_7
anounc_3_str_7_pre = anounc_3_pre["53 En el último mes Me siento asustada(o) por los riesgos a padecer esta enfermedad"]
anounc_3_str_7_post = anounc_3_post["53 En el último mes Me siento asustada(o) por los riesgos a padecer esta enfermedad"]
r13 = md.anova(anounc_3_str_7_pre, anounc_3_str_7_post)
#print(r13)


#################################################################################
#Avoidance
#Avo_1
anounc_3_avo_1_pre = anounc_3_pre["41.En el último mes Evito pensar, sentir o hablar sobre la enfermedad"]
anounc_3_avo_1_post = anounc_3_post["41.En el último mes Evito pensar, sentir o hablar sobre la enfermedad"]
r14 = md.anova(anounc_3_avo_1_pre, anounc_3_avo_1_post)
#print(r14)


#Avo_2
anounc_3_avo_2_pre = anounc_3_pre["42. En el último mes Evito ver o recurrir a información oficial sobre la enfermedad"]
anounc_3_avo_2_post = anounc_3_post["42. En el último mes Evito ver o recurrir a información oficial sobre la enfermedad"]
r15 = md.anova(anounc_3_avo_2_pre, anounc_3_avo_2_post)
#print(r15)


#Avo_3
anounc_3_avo_3_pre = anounc_3_pre["43. En el último mes Tengo dificultad para recordar lo que recomiendan las autoridades para enfrentar el riesgo o la enfermedad"]
anounc_3_avo_3_post = anounc_3_post["43. En el último mes Tengo dificultad para recordar lo que recomiendan las autoridades para enfrentar el riesgo o la enfermedad"]
r16 = md.anova(anounc_3_avo_3_pre, anounc_3_avo_3_post)
#print(r16)

###################################################################################

#Distancing
#Dis_1
anounc_3_dis_1_pre = anounc_3_pre["45. En el último mes He perdido interés por las actividades que antes disfrutaba"]
anounc_3_dis_1_post = anounc_3_post["45. En el último mes He perdido interés por las actividades que antes disfrutaba"]
r17 = md.anova(anounc_3_dis_1_pre, anounc_3_dis_1_post)
#print(r17)


#Dis_2
anounc_3_dis_2_pre = anounc_3_pre["46. En el último mes Me siento distante de las personas con quienes convivo, a partir de que inició el riesgo de esta enfermedad"]
anounc_3_dis_2_post = anounc_3_post["46. En el último mes Me siento distante de las personas con quienes convivo, a partir de que inició el riesgo de esta enfermedad"]
r18 = md.anova(anounc_3_dis_2_pre, anounc_3_dis_2_post)
#print(r18)


#Dis_3
anounc_3_dis_3_pre = anounc_3_pre["49. En el último mes Siento que deseo hacer cosas para hacerme daño"]
anounc_3_dis_3_post = anounc_3_post["49. En el último mes Siento que deseo hacer cosas para hacerme daño"]
r19 = md.anova(anounc_3_dis_3_pre, anounc_3_dis_3_post)
#print(r19)

#Dis_4
anounc_3_dis_4_pre = anounc_3_pre["50. En el último mes Tengo dificultad para quedarme dormido o seguir durmiendo"]
anounc_3_dis_4_post = anounc_3_post["50. En el último mes Tengo dificultad para quedarme dormido o seguir durmiendo"]
r20 = md.anova(anounc_3_dis_4_pre, anounc_3_dis_4_post)
#print(r20)


#Dis_5
anounc_3_dis_5_pre = anounc_3_pre["51. En el último mes Me siento enojada (o)"]
anounc_3_dis_5_post = anounc_3_post["51. En el último mes Me siento enojada (o)"]
r21 = md.anova(anounc_3_dis_5_pre, anounc_3_dis_5_post)
#print(r21)

#########################################################################


#Information seeking
#Inf_1
anounc_3_inf_1_pre = anounc_3_pre["64. Actualmente Leo (o me intereso por programas de televisión o radio) sobre enfermedades físicas graves"]
anounc_3_inf_1_post = anounc_3_post["64. Actualmente Leo (o me intereso por programas de televisión o radio) sobre enfermedades físicas graves"]
r22 = md.anova(anounc_3_inf_1_pre, anounc_3_inf_1_post)
#print(r22)

#Somatization
#Som_1
anounc_3_som_1_pre = anounc_3_pre["62. Actualmente Creo que padezco alguna enfermedad física grave (aunque no me la han confirmado)"]
anounc_3_som_1_post = anounc_3_post["62. Actualmente Creo que padezco alguna enfermedad física grave (aunque no me la han confirmado)"]
r23 = md.anova(anounc_3_som_1_pre, anounc_3_som_1_post)
#print(r23)


##############################################################################
print("measures_3")

#measures_3
#Anxiety
#Anx_1
measures_3_anx_1_pre = measures_3_pre["54 Durante las últimas 2 semanas Me he sentido nerviosa(o), ansiosa(o) o con los nervios de punta"]
measures_3_anx_1_post = measures_3_post["54 Durante las últimas 2 semanas Me he sentido nerviosa(o), ansiosa(o) o con los nervios de punta"]
r1 = md.anova(measures_3_anx_1_pre, measures_3_anx_1_post)
#print(r1)


#Anx_2
measures_3_anx_2_pre = measures_3_pre["55 Durante las últimas 2 semanas Me he sentido incapaz de controlar mis preocupaciones"]
measures_3_anx_2_post = measures_3_post["55 Durante las últimas 2 semanas Me he sentido incapaz de controlar mis preocupaciones"]
r2 = md.anova(measures_3_anx_2_pre, measures_3_anx_2_post)
#print(r2)


#Anx_3
measures_3_anx_3_pre = measures_3_pre["56 Durante las últimas 2 semanas Me he sentido tan inquieta(o) que no he podido quedarme quieta(o)"]
measures_3_anx_3_post = measures_3_post["56 Durante las últimas 2 semanas Me he sentido tan inquieta(o) que no he podido quedarme quieta(o)"]
r3 = md.anova(measures_3_anx_3_pre, measures_3_anx_3_post)
#print(r3)

#Anx_4
measures_3_anx_4_pre = measures_3_pre["57 Durante las últimas 2 semanas He tenido dificultad para relajarme"]
measures_3_anx_4_post = measures_3_post["57 Durante las últimas 2 semanas He tenido dificultad para relajarme"]
r4 = md.anova(measures_3_anx_4_pre, measures_3_anx_4_post)
#print(r4)


#Anx_5
measures_3_anx_5_pre = measures_3_pre["67 Durante las últimas 2 semanas Siento poco interés o placer en hacer cosas"]
measures_3_anx_5_post = measures_3_post["67 Durante las últimas 2 semanas Siento poco interés o placer en hacer cosas"]
r5 = md.anova(measures_3_anx_5_pre, measures_3_anx_5_post)
#print(r5)


#Anx_6
measures_3_anx_6_pre = measures_3_pre["68Durante las últimas 2 semanas Me he sentido decaída(o) deprimida(o) o sin esperanzas"]
measures_3_anx_6_post = measures_3_post["68Durante las últimas 2 semanas Me he sentido decaída(o) deprimida(o) o sin esperanzas"]
r6 = md.anova(measures_3_anx_6_pre, measures_3_anx_6_post)
#print(r6)

##############################################################################

#Stress

#Str_1
measures_3_str_1_pre = measures_3_pre["37. En el último mes Pienso o imagino, repetidamente, que voy a enfermar"]
measures_3_str_1_post = measures_3_post["37. En el último mes Pienso o imagino, repetidamente, que voy a enfermar"]
r7 = md.anova(measures_3_str_1_pre, measures_3_str_1_post)
#print(r7)


#Str_2
measures_3_str_2_pre = measures_3_pre["38. En el último mes Tengo pesadillas que se repiten acerca de la enfermedad"]
measures_3_str_2_post = measures_3_post["38. En el último mes Tengo pesadillas que se repiten acerca de la enfermedad"]
r8 = md.anova(measures_3_str_2_pre, measures_3_str_2_post)
#print(r8)


#Str_3
measures_3_str_3_pre = measures_3_pre["39 En el último mes Me siento preocupada(o) cuando se menciona la enfermedad"]
measures_3_str_3_post = measures_3_post["39 En el último mes Me siento preocupada(o) cuando se menciona la enfermedad"]
r9 = md.anova(measures_3_str_3_pre, measures_3_str_3_post)
#print(r9)

#Str_4
measures_3_str_4_pre = measures_3_pre["40 En el último mes Tengo reacciones físicas desagradable cuando pienso en la enfermedad (por ejemplo, latidos cardiacos muy fuertes, problemas para respirar, sudoración)"]
measures_3_str_4_post = measures_3_post["40 En el último mes Tengo reacciones físicas desagradable cuando pienso en la enfermedad (por ejemplo, latidos cardiacos muy fuertes, problemas para respirar, sudoración)"]
r10 = md.anova(measures_3_str_4_pre, measures_3_str_4_post)
#print(r10)


#Str_5
measures_3_str_5_pre = measures_3_pre["44 En el último mes Pienso que si me enfermo o se enferma alguien de mi familia, es por mi culpa"]
measures_3_str_5_post = measures_3_post["44 En el último mes Pienso que si me enfermo o se enferma alguien de mi familia, es por mi culpa"]
r11 = md.anova(measures_3_str_5_pre, measures_3_str_5_post)
#print(r11)


#Str_6
measures_3_str_6_pre = measures_3_pre["48 En el último mes Siento que mi futuro es incierto a partir de que comenzó el riesgo a padecer esta enfermedad"]
measures_3_str_6_post = measures_3_post["48 En el último mes Siento que mi futuro es incierto a partir de que comenzó el riesgo a padecer esta enfermedad"]
r12 = md.anova(measures_3_str_6_pre, measures_3_str_6_post)
#print(r12)

#Str_7
measures_3_str_7_pre = measures_3_pre["53 En el último mes Me siento asustada(o) por los riesgos a padecer esta enfermedad"]
measures_3_str_7_post = measures_3_post["53 En el último mes Me siento asustada(o) por los riesgos a padecer esta enfermedad"]
r13 = md.anova(measures_3_str_7_pre, measures_3_str_7_post)
#print(r13)


#################################################################################
#Avoidance
#Avo_1
measures_3_avo_1_pre = measures_3_pre["41.En el último mes Evito pensar, sentir o hablar sobre la enfermedad"]
measures_3_avo_1_post = measures_3_post["41.En el último mes Evito pensar, sentir o hablar sobre la enfermedad"]
r14 = md.anova(measures_3_avo_1_pre, measures_3_avo_1_post)
#print(r14)


#Avo_2
measures_3_avo_2_pre = measures_3_pre["42. En el último mes Evito ver o recurrir a información oficial sobre la enfermedad"]
measures_3_avo_2_post = measures_3_post["42. En el último mes Evito ver o recurrir a información oficial sobre la enfermedad"]
r15 = md.anova(measures_3_avo_2_pre, measures_3_avo_2_post)
#print(r15)


#Avo_3
measures_3_avo_3_pre = measures_3_pre["43. En el último mes Tengo dificultad para recordar lo que recomiendan las autoridades para enfrentar el riesgo o la enfermedad"]
measures_3_avo_3_post = measures_3_post["43. En el último mes Tengo dificultad para recordar lo que recomiendan las autoridades para enfrentar el riesgo o la enfermedad"]
r16 = md.anova(measures_3_avo_3_pre, measures_3_avo_3_post)
#print(r16)

###################################################################################

#Distancing
#Dis_1
measures_3_dis_1_pre = measures_3_pre["45. En el último mes He perdido interés por las actividades que antes disfrutaba"]
measures_3_dis_1_post = measures_3_post["45. En el último mes He perdido interés por las actividades que antes disfrutaba"]
r17 = md.anova(measures_3_dis_1_pre, measures_3_dis_1_post)
#print(r17)


#Dis_2
measures_3_dis_2_pre = measures_3_pre["46. En el último mes Me siento distante de las personas con quienes convivo, a partir de que inició el riesgo de esta enfermedad"]
measures_3_dis_2_post = measures_3_post["46. En el último mes Me siento distante de las personas con quienes convivo, a partir de que inició el riesgo de esta enfermedad"]
r18 = md.anova(measures_3_dis_2_pre, measures_3_dis_2_post)
#print(r18)


#Dis_3
measures_3_dis_3_pre = measures_3_pre["49. En el último mes Siento que deseo hacer cosas para hacerme daño"]
measures_3_dis_3_post = measures_3_post["49. En el último mes Siento que deseo hacer cosas para hacerme daño"]
r19 = md.anova(measures_3_dis_3_pre, measures_3_dis_3_post)
#print(r19)

#Dis_4
measures_3_dis_4_pre = measures_3_pre["50. En el último mes Tengo dificultad para quedarme dormido o seguir durmiendo"]
measures_3_dis_4_post = measures_3_post["50. En el último mes Tengo dificultad para quedarme dormido o seguir durmiendo"]
r20 = md.anova(measures_3_dis_4_pre, measures_3_dis_4_post)
#print(r20)


#Dis_5
measures_3_dis_5_pre = measures_3_pre["51. En el último mes Me siento enojada (o)"]
measures_3_dis_5_post = measures_3_post["51. En el último mes Me siento enojada (o)"]
r21 = md.anova(measures_3_dis_5_pre, measures_3_dis_5_post)
#print(r21)

#########################################################################


#Information seeking
#Inf_1
measures_3_inf_1_pre = measures_3_pre["64. Actualmente Leo (o me intereso por programas de televisión o radio) sobre enfermedades físicas graves"]
measures_3_inf_1_post = measures_3_post["64. Actualmente Leo (o me intereso por programas de televisión o radio) sobre enfermedades físicas graves"]
r22 = md.anova(measures_3_inf_1_pre, measures_3_inf_1_post)
#print(r22)

#Somatization
#Som_1
measures_3_som_1_pre = measures_3_pre["62. Actualmente Creo que padezco alguna enfermedad física grave (aunque no me la han confirmado)"]
measures_3_som_1_post = measures_3_post["62. Actualmente Creo que padezco alguna enfermedad física grave (aunque no me la han confirmado)"]
r23 = md.anova(measures_3_som_1_pre, measures_3_som_1_post)
#print(r23)

################################################################################
print("prom_2")

#prom_2
#Anxiety
#Anx_1
prom_2_anx_1_pre = prom_2_pre["54 Durante las últimas 2 semanas Me he sentido nerviosa(o), ansiosa(o) o con los nervios de punta"]
prom_2_anx_1_post = prom_2_post["54 Durante las últimas 2 semanas Me he sentido nerviosa(o), ansiosa(o) o con los nervios de punta"]
r1 = md.anova(prom_2_anx_1_pre, prom_2_anx_1_post)
#print(r1)


#Anx_2
prom_2_anx_2_pre = prom_2_pre["55 Durante las últimas 2 semanas Me he sentido incapaz de controlar mis preocupaciones"]
prom_2_anx_2_post = prom_2_post["55 Durante las últimas 2 semanas Me he sentido incapaz de controlar mis preocupaciones"]
r2 = md.anova(prom_2_anx_2_pre, prom_2_anx_2_post)
#print(r2)


#Anx_3
prom_2_anx_3_pre = prom_2_pre["56 Durante las últimas 2 semanas Me he sentido tan inquieta(o) que no he podido quedarme quieta(o)"]
prom_2_anx_3_post = prom_2_post["56 Durante las últimas 2 semanas Me he sentido tan inquieta(o) que no he podido quedarme quieta(o)"]
r3 = md.anova(prom_2_anx_3_pre, prom_2_anx_3_post)
#print(r3)

#Anx_4
prom_2_anx_4_pre = prom_2_pre["57 Durante las últimas 2 semanas He tenido dificultad para relajarme"]
prom_2_anx_4_post = prom_2_post["57 Durante las últimas 2 semanas He tenido dificultad para relajarme"]
r4 = md.anova(prom_2_anx_4_pre, prom_2_anx_4_post)
#print(r4)


#Anx_5
prom_2_anx_5_pre = prom_2_pre["67 Durante las últimas 2 semanas Siento poco interés o placer en hacer cosas"]
prom_2_anx_5_post = prom_2_post["67 Durante las últimas 2 semanas Siento poco interés o placer en hacer cosas"]
r5 = md.anova(prom_2_anx_5_pre, prom_2_anx_5_post)
#print(r5)


#Anx_6
prom_2_anx_6_pre = prom_2_pre["68Durante las últimas 2 semanas Me he sentido decaída(o) deprimida(o) o sin esperanzas"]
prom_2_anx_6_post = prom_2_post["68Durante las últimas 2 semanas Me he sentido decaída(o) deprimida(o) o sin esperanzas"]
r6 = md.anova(prom_2_anx_6_pre, prom_2_anx_6_post)
#print(r6)

##############################################################################

#Stress

#Str_1
prom_2_str_1_pre = prom_2_pre["37. En el último mes Pienso o imagino, repetidamente, que voy a enfermar"]
prom_2_str_1_post = prom_2_post["37. En el último mes Pienso o imagino, repetidamente, que voy a enfermar"]
r7 = md.anova(prom_2_str_1_pre, prom_2_str_1_post)
#print(r7)


#Str_2
prom_2_str_2_pre = prom_2_pre["38. En el último mes Tengo pesadillas que se repiten acerca de la enfermedad"]
prom_2_str_2_post = prom_2_post["38. En el último mes Tengo pesadillas que se repiten acerca de la enfermedad"]
r8 = md.anova(prom_2_str_2_pre, prom_2_str_2_post)
#print(r8)


#Str_3
prom_2_str_3_pre = prom_2_pre["39 En el último mes Me siento preocupada(o) cuando se menciona la enfermedad"]
prom_2_str_3_post = prom_2_post["39 En el último mes Me siento preocupada(o) cuando se menciona la enfermedad"]
r9 = md.anova(prom_2_str_3_pre, prom_2_str_3_post)
#print(r9)

#Str_4
prom_2_str_4_pre = prom_2_pre["40 En el último mes Tengo reacciones físicas desagradable cuando pienso en la enfermedad (por ejemplo, latidos cardiacos muy fuertes, problemas para respirar, sudoración)"]
prom_2_str_4_post = prom_2_post["40 En el último mes Tengo reacciones físicas desagradable cuando pienso en la enfermedad (por ejemplo, latidos cardiacos muy fuertes, problemas para respirar, sudoración)"]
r10 = md.anova(prom_2_str_4_pre, prom_2_str_4_post)
#print(r10)


#Str_5
prom_2_str_5_pre = prom_2_pre["44 En el último mes Pienso que si me enfermo o se enferma alguien de mi familia, es por mi culpa"]
prom_2_str_5_post = prom_2_post["44 En el último mes Pienso que si me enfermo o se enferma alguien de mi familia, es por mi culpa"]
r11 = md.anova(prom_2_str_5_pre, prom_2_str_5_post)
#print(r11)


#Str_6
prom_2_str_6_pre = prom_2_pre["48 En el último mes Siento que mi futuro es incierto a partir de que comenzó el riesgo a padecer esta enfermedad"]
prom_2_str_6_post = prom_2_post["48 En el último mes Siento que mi futuro es incierto a partir de que comenzó el riesgo a padecer esta enfermedad"]
r12 = md.anova(prom_2_str_6_pre, prom_2_str_6_post)
#print(r12)

#Str_7
prom_2_str_7_pre = prom_2_pre["53 En el último mes Me siento asustada(o) por los riesgos a padecer esta enfermedad"]
prom_2_str_7_post = prom_2_post["53 En el último mes Me siento asustada(o) por los riesgos a padecer esta enfermedad"]
r13 = md.anova(prom_2_str_7_pre, prom_2_str_7_post)
#print(r13)


#################################################################################
#Avoidance
#Avo_1
prom_2_avo_1_pre = prom_2_pre["41.En el último mes Evito pensar, sentir o hablar sobre la enfermedad"]
prom_2_avo_1_post = prom_2_post["41.En el último mes Evito pensar, sentir o hablar sobre la enfermedad"]
r14 = md.anova(prom_2_avo_1_pre, prom_2_avo_1_post)
#print(r14)


#Avo_2
prom_2_avo_2_pre = prom_2_pre["42. En el último mes Evito ver o recurrir a información oficial sobre la enfermedad"]
prom_2_avo_2_post = prom_2_post["42. En el último mes Evito ver o recurrir a información oficial sobre la enfermedad"]
r15 = md.anova(prom_2_avo_2_pre, prom_2_avo_2_post)
#print(r15)


#Avo_3
prom_2_avo_3_pre = prom_2_pre["43. En el último mes Tengo dificultad para recordar lo que recomiendan las autoridades para enfrentar el riesgo o la enfermedad"]
prom_2_avo_3_post = prom_2_post["43. En el último mes Tengo dificultad para recordar lo que recomiendan las autoridades para enfrentar el riesgo o la enfermedad"]
r16 = md.anova(prom_2_avo_3_pre, prom_2_avo_3_post)
#print(r16)

###################################################################################

#Distancing
#Dis_1
prom_2_dis_1_pre = prom_2_pre["45. En el último mes He perdido interés por las actividades que antes disfrutaba"]
prom_2_dis_1_post = prom_2_post["45. En el último mes He perdido interés por las actividades que antes disfrutaba"]
r17 = md.anova(prom_2_dis_1_pre, prom_2_dis_1_post)
#print(r17)


#Dis_2
prom_2_dis_2_pre = prom_2_pre["46. En el último mes Me siento distante de las personas con quienes convivo, a partir de que inició el riesgo de esta enfermedad"]
prom_2_dis_2_post = prom_2_post["46. En el último mes Me siento distante de las personas con quienes convivo, a partir de que inició el riesgo de esta enfermedad"]
r18 = md.anova(prom_2_dis_2_pre, prom_2_dis_2_post)
#print(r18)


#Dis_3
prom_2_dis_3_pre = prom_2_pre["49. En el último mes Siento que deseo hacer cosas para hacerme daño"]
prom_2_dis_3_post = prom_2_post["49. En el último mes Siento que deseo hacer cosas para hacerme daño"]
r19 = md.anova(prom_2_dis_3_pre, prom_2_dis_3_post)
#print(r19)

#Dis_4
prom_2_dis_4_pre = prom_2_pre["50. En el último mes Tengo dificultad para quedarme dormido o seguir durmiendo"]
prom_2_dis_4_post = prom_2_post["50. En el último mes Tengo dificultad para quedarme dormido o seguir durmiendo"]
r20 = md.anova(prom_2_dis_4_pre, prom_2_dis_4_post)
#print(r20)


#Dis_5
prom_2_dis_5_pre = prom_2_pre["51. En el último mes Me siento enojada (o)"]
prom_2_dis_5_post = prom_2_post["51. En el último mes Me siento enojada (o)"]
r21 = md.anova(prom_2_dis_5_pre, prom_2_dis_5_post)
#print(r21)

#########################################################################


#Information seeking
#Inf_1
prom_2_inf_1_pre = prom_2_pre["64. Actualmente Leo (o me intereso por programas de televisión o radio) sobre enfermedades físicas graves"]
prom_2_inf_1_post = prom_2_post["64. Actualmente Leo (o me intereso por programas de televisión o radio) sobre enfermedades físicas graves"]
r22 = md.anova(prom_2_inf_1_pre, prom_2_inf_1_post)
#print(r22)

#Somatization
#Som_1
prom_2_som_1_pre = prom_2_pre["62. Actualmente Creo que padezco alguna enfermedad física grave (aunque no me la han confirmado)"]
prom_2_som_1_post = prom_2_post["62. Actualmente Creo que padezco alguna enfermedad física grave (aunque no me la han confirmado)"]
r23 = md.anova(prom_2_som_1_pre, prom_2_som_1_post)
#print(r23)

##########################################################################
print("fest_2")

#fest_2
#Anxiety
#Anx_1
fest_2_anx_1_pre = fest_2_pre["54 Durante las últimas 2 semanas Me he sentido nerviosa(o), ansiosa(o) o con los nervios de punta"]
fest_2_anx_1_post = fest_2_post["54 Durante las últimas 2 semanas Me he sentido nerviosa(o), ansiosa(o) o con los nervios de punta"]
r1 = md.anova(fest_2_anx_1_pre, fest_2_anx_1_post)
#print(r1)


#Anx_2
fest_2_anx_2_pre = fest_2_pre["55 Durante las últimas 2 semanas Me he sentido incapaz de controlar mis preocupaciones"]
fest_2_anx_2_post = fest_2_post["55 Durante las últimas 2 semanas Me he sentido incapaz de controlar mis preocupaciones"]
r2 = md.anova(fest_2_anx_2_pre, fest_2_anx_2_post)
#print(r2)


#Anx_3
fest_2_anx_3_pre = fest_2_pre["56 Durante las últimas 2 semanas Me he sentido tan inquieta(o) que no he podido quedarme quieta(o)"]
fest_2_anx_3_post = fest_2_post["56 Durante las últimas 2 semanas Me he sentido tan inquieta(o) que no he podido quedarme quieta(o)"]
r3 = md.anova(fest_2_anx_3_pre, fest_2_anx_3_post)
#print(r3)

#Anx_4
fest_2_anx_4_pre = fest_2_pre["57 Durante las últimas 2 semanas He tenido dificultad para relajarme"]
fest_2_anx_4_post = fest_2_post["57 Durante las últimas 2 semanas He tenido dificultad para relajarme"]
r4 = md.anova(fest_2_anx_4_pre, fest_2_anx_4_post)
#print(r4)


#Anx_5
fest_2_anx_5_pre = fest_2_pre["67 Durante las últimas 2 semanas Siento poco interés o placer en hacer cosas"]
fest_2_anx_5_post = fest_2_post["67 Durante las últimas 2 semanas Siento poco interés o placer en hacer cosas"]
r5 = md.anova(fest_2_anx_5_pre, fest_2_anx_5_post)
#print(r5)


#Anx_6
fest_2_anx_6_pre = fest_2_pre["68Durante las últimas 2 semanas Me he sentido decaída(o) deprimida(o) o sin esperanzas"]
fest_2_anx_6_post = fest_2_post["68Durante las últimas 2 semanas Me he sentido decaída(o) deprimida(o) o sin esperanzas"]
r6 = md.anova(fest_2_anx_6_pre, fest_2_anx_6_post)
#print(r6)

##############################################################################

#Stress

#Str_1
fest_2_str_1_pre = fest_2_pre["37. En el último mes Pienso o imagino, repetidamente, que voy a enfermar"]
fest_2_str_1_post = fest_2_post["37. En el último mes Pienso o imagino, repetidamente, que voy a enfermar"]
r7 = md.anova(fest_2_str_1_pre, fest_2_str_1_post)
#print(r7)


#Str_2
fest_2_str_2_pre = fest_2_pre["38. En el último mes Tengo pesadillas que se repiten acerca de la enfermedad"]
fest_2_str_2_post = fest_2_post["38. En el último mes Tengo pesadillas que se repiten acerca de la enfermedad"]
r8 = md.anova(fest_2_str_2_pre, fest_2_str_2_post)
#print(r8)


#Str_3
fest_2_str_3_pre = fest_2_pre["39 En el último mes Me siento preocupada(o) cuando se menciona la enfermedad"]
fest_2_str_3_post = fest_2_post["39 En el último mes Me siento preocupada(o) cuando se menciona la enfermedad"]
r9 = md.anova(fest_2_str_3_pre, fest_2_str_3_post)
#print(r9)

#Str_4
fest_2_str_4_pre = fest_2_pre["40 En el último mes Tengo reacciones físicas desagradable cuando pienso en la enfermedad (por ejemplo, latidos cardiacos muy fuertes, problemas para respirar, sudoración)"]
fest_2_str_4_post = fest_2_post["40 En el último mes Tengo reacciones físicas desagradable cuando pienso en la enfermedad (por ejemplo, latidos cardiacos muy fuertes, problemas para respirar, sudoración)"]
r10 = md.anova(fest_2_str_4_pre, fest_2_str_4_post)
#print(r10)


#Str_5
fest_2_str_5_pre = fest_2_pre["44 En el último mes Pienso que si me enfermo o se enferma alguien de mi familia, es por mi culpa"]
fest_2_str_5_post = fest_2_post["44 En el último mes Pienso que si me enfermo o se enferma alguien de mi familia, es por mi culpa"]
r11 = md.anova(fest_2_str_5_pre, fest_2_str_5_post)
#print(r11)


#Str_6
fest_2_str_6_pre = fest_2_pre["48 En el último mes Siento que mi futuro es incierto a partir de que comenzó el riesgo a padecer esta enfermedad"]
fest_2_str_6_post = fest_2_post["48 En el último mes Siento que mi futuro es incierto a partir de que comenzó el riesgo a padecer esta enfermedad"]
r12 = md.anova(fest_2_str_6_pre, fest_2_str_6_post)
#print(r12)

#Str_7
fest_2_str_7_pre = fest_2_pre["53 En el último mes Me siento asustada(o) por los riesgos a padecer esta enfermedad"]
fest_2_str_7_post = fest_2_post["53 En el último mes Me siento asustada(o) por los riesgos a padecer esta enfermedad"]
r13 = md.anova(fest_2_str_7_pre, fest_2_str_7_post)
#print(r13)


#################################################################################
#Avoidance
#Avo_1
fest_2_avo_1_pre = fest_2_pre["41.En el último mes Evito pensar, sentir o hablar sobre la enfermedad"]
fest_2_avo_1_post = fest_2_post["41.En el último mes Evito pensar, sentir o hablar sobre la enfermedad"]
r14 = md.anova(fest_2_avo_1_pre, fest_2_avo_1_post)
#print(r14)


#Avo_2
fest_2_avo_2_pre = fest_2_pre["42. En el último mes Evito ver o recurrir a información oficial sobre la enfermedad"]
fest_2_avo_2_post = fest_2_post["42. En el último mes Evito ver o recurrir a información oficial sobre la enfermedad"]
r15 = md.anova(fest_2_avo_2_pre, fest_2_avo_2_post)
#print(r15)


#Avo_3
fest_2_avo_3_pre = fest_2_pre["43. En el último mes Tengo dificultad para recordar lo que recomiendan las autoridades para enfrentar el riesgo o la enfermedad"]
fest_2_avo_3_post = fest_2_post["43. En el último mes Tengo dificultad para recordar lo que recomiendan las autoridades para enfrentar el riesgo o la enfermedad"]
r16 = md.anova(fest_2_avo_3_pre, fest_2_avo_3_post)
#print(r16)

###################################################################################

#Distancing
#Dis_1
fest_2_dis_1_pre = fest_2_pre["45. En el último mes He perdido interés por las actividades que antes disfrutaba"]
fest_2_dis_1_post = fest_2_post["45. En el último mes He perdido interés por las actividades que antes disfrutaba"]
r17 = md.anova(fest_2_dis_1_pre, fest_2_dis_1_post)
#print(r17)


#Dis_2
fest_2_dis_2_pre = fest_2_pre["46. En el último mes Me siento distante de las personas con quienes convivo, a partir de que inició el riesgo de esta enfermedad"]
fest_2_dis_2_post = fest_2_post["46. En el último mes Me siento distante de las personas con quienes convivo, a partir de que inició el riesgo de esta enfermedad"]
r18 = md.anova(fest_2_dis_2_pre, fest_2_dis_2_post)
#print(r18)


#Dis_3
fest_2_dis_3_pre = fest_2_pre["49. En el último mes Siento que deseo hacer cosas para hacerme daño"]
fest_2_dis_3_post = fest_2_post["49. En el último mes Siento que deseo hacer cosas para hacerme daño"]
r19 = md.anova(fest_2_dis_3_pre, fest_2_dis_3_post)
#print(r19)

#Dis_4
fest_2_dis_4_pre = fest_2_pre["50. En el último mes Tengo dificultad para quedarme dormido o seguir durmiendo"]
fest_2_dis_4_post = fest_2_post["50. En el último mes Tengo dificultad para quedarme dormido o seguir durmiendo"]
r20 = md.anova(fest_2_dis_4_pre, fest_2_dis_4_post)
#print(r20)


#Dis_5
fest_2_dis_5_pre = fest_2_pre["51. En el último mes Me siento enojada (o)"]
fest_2_dis_5_post = fest_2_post["51. En el último mes Me siento enojada (o)"]
r21 = md.anova(fest_2_dis_5_pre, fest_2_dis_5_post)
#print(r21)

#########################################################################


#Information seeking
#Inf_1
fest_2_inf_1_pre = fest_2_pre["64. Actualmente Leo (o me intereso por programas de televisión o radio) sobre enfermedades físicas graves"]
fest_2_inf_1_post = fest_2_post["64. Actualmente Leo (o me intereso por programas de televisión o radio) sobre enfermedades físicas graves"]
r22 = md.anova(fest_2_inf_1_pre, fest_2_inf_1_post)
#print(r22)

#Somatization
#Som_1
fest_2_som_1_pre = fest_2_pre["62. Actualmente Creo que padezco alguna enfermedad física grave (aunque no me la han confirmado)"]
fest_2_som_1_post = fest_2_post["62. Actualmente Creo que padezco alguna enfermedad física grave (aunque no me la han confirmado)"]
r23 = md.anova(fest_2_som_1_pre, fest_2_som_1_post)
#print(r23)

###################################################################################
print("prom_3")

#prom_3
#Anxiety
#Anx_1
prom_3_anx_1_pre = prom_3_pre["54 Durante las últimas 2 semanas Me he sentido nerviosa(o), ansiosa(o) o con los nervios de punta"]
prom_3_anx_1_post = prom_3_post["54 Durante las últimas 2 semanas Me he sentido nerviosa(o), ansiosa(o) o con los nervios de punta"]
r1 = md.anova(prom_3_anx_1_pre, prom_3_anx_1_post)
#print(r1)


#Anx_2
prom_3_anx_2_pre = prom_3_pre["55 Durante las últimas 2 semanas Me he sentido incapaz de controlar mis preocupaciones"]
prom_3_anx_2_post = prom_3_post["55 Durante las últimas 2 semanas Me he sentido incapaz de controlar mis preocupaciones"]
r2 = md.anova(prom_3_anx_2_pre, prom_3_anx_2_post)
#print(r2)


#Anx_3
prom_3_anx_3_pre = prom_3_pre["56 Durante las últimas 2 semanas Me he sentido tan inquieta(o) que no he podido quedarme quieta(o)"]
prom_3_anx_3_post = prom_3_post["56 Durante las últimas 2 semanas Me he sentido tan inquieta(o) que no he podido quedarme quieta(o)"]
r3 = md.anova(prom_3_anx_3_pre, prom_3_anx_3_post)
#print(r3)

#Anx_4
prom_3_anx_4_pre = prom_3_pre["57 Durante las últimas 2 semanas He tenido dificultad para relajarme"]
prom_3_anx_4_post = prom_3_post["57 Durante las últimas 2 semanas He tenido dificultad para relajarme"]
r4 = md.anova(prom_3_anx_4_pre, prom_3_anx_4_post)
#print(r4)


#Anx_5
prom_3_anx_5_pre = prom_3_pre["67 Durante las últimas 2 semanas Siento poco interés o placer en hacer cosas"]
prom_3_anx_5_post = prom_3_post["67 Durante las últimas 2 semanas Siento poco interés o placer en hacer cosas"]
r5 = md.anova(prom_3_anx_5_pre, prom_3_anx_5_post)
#print(r5)


#Anx_6
prom_3_anx_6_pre = prom_3_pre["68Durante las últimas 2 semanas Me he sentido decaída(o) deprimida(o) o sin esperanzas"]
prom_3_anx_6_post = prom_3_post["68Durante las últimas 2 semanas Me he sentido decaída(o) deprimida(o) o sin esperanzas"]
r6 = md.anova(prom_3_anx_6_pre, prom_3_anx_6_post)
#print(r6)

##############################################################################

#Stress

#Str_1
prom_3_str_1_pre = prom_3_pre["37. En el último mes Pienso o imagino, repetidamente, que voy a enfermar"]
prom_3_str_1_post = prom_3_post["37. En el último mes Pienso o imagino, repetidamente, que voy a enfermar"]
r7 = md.anova(prom_3_str_1_pre, prom_3_str_1_post)
#print(r7)


#Str_2
prom_3_str_2_pre = prom_3_pre["38. En el último mes Tengo pesadillas que se repiten acerca de la enfermedad"]
prom_3_str_2_post = prom_3_post["38. En el último mes Tengo pesadillas que se repiten acerca de la enfermedad"]
r8 = md.anova(prom_3_str_2_pre, prom_3_str_2_post)
#print(r8)


#Str_3
prom_3_str_3_pre = prom_3_pre["39 En el último mes Me siento preocupada(o) cuando se menciona la enfermedad"]
prom_3_str_3_post = prom_3_post["39 En el último mes Me siento preocupada(o) cuando se menciona la enfermedad"]
r9 = md.anova(prom_3_str_3_pre, prom_3_str_3_post)
#print(r9)

#Str_4
prom_3_str_4_pre = prom_3_pre["40 En el último mes Tengo reacciones físicas desagradable cuando pienso en la enfermedad (por ejemplo, latidos cardiacos muy fuertes, problemas para respirar, sudoración)"]
prom_3_str_4_post = prom_3_post["40 En el último mes Tengo reacciones físicas desagradable cuando pienso en la enfermedad (por ejemplo, latidos cardiacos muy fuertes, problemas para respirar, sudoración)"]
r10 = md.anova(prom_3_str_4_pre, prom_3_str_4_post)
#print(r10)


#Str_5
prom_3_str_5_pre = prom_3_pre["44 En el último mes Pienso que si me enfermo o se enferma alguien de mi familia, es por mi culpa"]
prom_3_str_5_post = prom_3_post["44 En el último mes Pienso que si me enfermo o se enferma alguien de mi familia, es por mi culpa"]
r11 = md.anova(prom_3_str_5_pre, prom_3_str_5_post)
#print(r11)


#Str_6
prom_3_str_6_pre = prom_3_pre["48 En el último mes Siento que mi futuro es incierto a partir de que comenzó el riesgo a padecer esta enfermedad"]
prom_3_str_6_post = prom_3_post["48 En el último mes Siento que mi futuro es incierto a partir de que comenzó el riesgo a padecer esta enfermedad"]
r12 = md.anova(prom_3_str_6_pre, prom_3_str_6_post)
#print(r12)

#Str_7
prom_3_str_7_pre = prom_3_pre["53 En el último mes Me siento asustada(o) por los riesgos a padecer esta enfermedad"]
prom_3_str_7_post = prom_3_post["53 En el último mes Me siento asustada(o) por los riesgos a padecer esta enfermedad"]
r13 = md.anova(prom_3_str_7_pre, prom_3_str_7_post)
#print(r13)


#################################################################################
#Avoidance
#Avo_1
prom_3_avo_1_pre = prom_3_pre["41.En el último mes Evito pensar, sentir o hablar sobre la enfermedad"]
prom_3_avo_1_post = prom_3_post["41.En el último mes Evito pensar, sentir o hablar sobre la enfermedad"]
r14 = md.anova(prom_3_avo_1_pre, prom_3_avo_1_post)
#print(r14)


#Avo_2
prom_3_avo_2_pre = prom_3_pre["42. En el último mes Evito ver o recurrir a información oficial sobre la enfermedad"]
prom_3_avo_2_post = prom_3_post["42. En el último mes Evito ver o recurrir a información oficial sobre la enfermedad"]
r15 = md.anova(prom_3_avo_2_pre, prom_3_avo_2_post)
#print(r15)


#Avo_3
prom_3_avo_3_pre = prom_3_pre["43. En el último mes Tengo dificultad para recordar lo que recomiendan las autoridades para enfrentar el riesgo o la enfermedad"]
prom_3_avo_3_post = prom_3_post["43. En el último mes Tengo dificultad para recordar lo que recomiendan las autoridades para enfrentar el riesgo o la enfermedad"]
r16 = md.anova(prom_3_avo_3_pre, prom_3_avo_3_post)
#print(r16)

###################################################################################

#Distancing
#Dis_1
prom_3_dis_1_pre = prom_3_pre["45. En el último mes He perdido interés por las actividades que antes disfrutaba"]
prom_3_dis_1_post = prom_3_post["45. En el último mes He perdido interés por las actividades que antes disfrutaba"]
r17 = md.anova(prom_3_dis_1_pre, prom_3_dis_1_post)
#print(r17)


#Dis_2
prom_3_dis_2_pre = prom_3_pre["46. En el último mes Me siento distante de las personas con quienes convivo, a partir de que inició el riesgo de esta enfermedad"]
prom_3_dis_2_post = prom_3_post["46. En el último mes Me siento distante de las personas con quienes convivo, a partir de que inició el riesgo de esta enfermedad"]
r18 = md.anova(prom_3_dis_2_pre, prom_3_dis_2_post)
#print(r18)


#Dis_3
prom_3_dis_3_pre = prom_3_pre["49. En el último mes Siento que deseo hacer cosas para hacerme daño"]
prom_3_dis_3_post = prom_3_post["49. En el último mes Siento que deseo hacer cosas para hacerme daño"]
r19 = md.anova(prom_3_dis_3_pre, prom_3_dis_3_post)
#print(r19)

#Dis_4
prom_3_dis_4_pre = prom_3_pre["50. En el último mes Tengo dificultad para quedarme dormido o seguir durmiendo"]
prom_3_dis_4_post = prom_3_post["50. En el último mes Tengo dificultad para quedarme dormido o seguir durmiendo"]
r20 = md.anova(prom_3_dis_4_pre, prom_3_dis_4_post)
#print(r20)


#Dis_5
prom_3_dis_5_pre = prom_3_pre["51. En el último mes Me siento enojada (o)"]
prom_3_dis_5_post = prom_3_post["51. En el último mes Me siento enojada (o)"]
r21 = md.anova(prom_3_dis_5_pre, prom_3_dis_5_post)
#print(r21)

#########################################################################


#Information seeking
#Inf_1
prom_3_inf_1_pre = prom_3_pre["64. Actualmente Leo (o me intereso por programas de televisión o radio) sobre enfermedades físicas graves"]
prom_3_inf_1_post = prom_3_post["64. Actualmente Leo (o me intereso por programas de televisión o radio) sobre enfermedades físicas graves"]
r22 = md.anova(prom_3_inf_1_pre, prom_3_inf_1_post)
#print(r22)

#Somatization
#Som_1
prom_3_som_1_pre = prom_3_pre["62. Actualmente Creo que padezco alguna enfermedad física grave (aunque no me la han confirmado)"]
prom_3_som_1_post = prom_3_post["62. Actualmente Creo que padezco alguna enfermedad física grave (aunque no me la han confirmado)"]
r23 = md.anova(prom_3_som_1_pre, prom_3_som_1_post)
#print(r23)


#############################################################################
print("prom_4")

#prom_4
#Anxiety
#Anx_1
prom_4_anx_1_pre = prom_4_pre["54 Durante las últimas 2 semanas Me he sentido nerviosa(o), ansiosa(o) o con los nervios de punta"]
prom_4_anx_1_post = prom_4_post["54 Durante las últimas 2 semanas Me he sentido nerviosa(o), ansiosa(o) o con los nervios de punta"]
r1 = md.anova(prom_4_anx_1_pre, prom_4_anx_1_post)
#print(r1)


#Anx_2
prom_4_anx_2_pre = prom_4_pre["55 Durante las últimas 2 semanas Me he sentido incapaz de controlar mis preocupaciones"]
prom_4_anx_2_post = prom_4_post["55 Durante las últimas 2 semanas Me he sentido incapaz de controlar mis preocupaciones"]
r2 = md.anova(prom_4_anx_2_pre, prom_4_anx_2_post)
#print(r2)


#Anx_3
prom_4_anx_3_pre = prom_4_pre["56 Durante las últimas 2 semanas Me he sentido tan inquieta(o) que no he podido quedarme quieta(o)"]
prom_4_anx_3_post = prom_4_post["56 Durante las últimas 2 semanas Me he sentido tan inquieta(o) que no he podido quedarme quieta(o)"]
r3 = md.anova(prom_4_anx_3_pre, prom_4_anx_3_post)
#print(r3)

#Anx_4
prom_4_anx_4_pre = prom_4_pre["57 Durante las últimas 2 semanas He tenido dificultad para relajarme"]
prom_4_anx_4_post = prom_4_post["57 Durante las últimas 2 semanas He tenido dificultad para relajarme"]
r4 = md.anova(prom_4_anx_4_pre, prom_4_anx_4_post)
#print(r4)


#Anx_5
prom_4_anx_5_pre = prom_4_pre["67 Durante las últimas 2 semanas Siento poco interés o placer en hacer cosas"]
prom_4_anx_5_post = prom_4_post["67 Durante las últimas 2 semanas Siento poco interés o placer en hacer cosas"]
r5 = md.anova(prom_4_anx_5_pre, prom_4_anx_5_post)
#print(r5)


#Anx_6
prom_4_anx_6_pre = prom_4_pre["68Durante las últimas 2 semanas Me he sentido decaída(o) deprimida(o) o sin esperanzas"]
prom_4_anx_6_post = prom_4_post["68Durante las últimas 2 semanas Me he sentido decaída(o) deprimida(o) o sin esperanzas"]
r6 = md.anova(prom_4_anx_6_pre, prom_4_anx_6_post)
#print(r6)

##############################################################################

#Stress

#Str_1
prom_4_str_1_pre = prom_4_pre["37. En el último mes Pienso o imagino, repetidamente, que voy a enfermar"]
prom_4_str_1_post = prom_4_post["37. En el último mes Pienso o imagino, repetidamente, que voy a enfermar"]
r7 = md.anova(prom_4_str_1_pre, prom_4_str_1_post)
#print(r7)


#Str_2
prom_4_str_2_pre = prom_4_pre["38. En el último mes Tengo pesadillas que se repiten acerca de la enfermedad"]
prom_4_str_2_post = prom_4_post["38. En el último mes Tengo pesadillas que se repiten acerca de la enfermedad"]
r8 = md.anova(prom_4_str_2_pre, prom_4_str_2_post)
#print(r8)


#Str_3
prom_4_str_3_pre = prom_4_pre["39 En el último mes Me siento preocupada(o) cuando se menciona la enfermedad"]
prom_4_str_3_post = prom_4_post["39 En el último mes Me siento preocupada(o) cuando se menciona la enfermedad"]
r9 = md.anova(prom_4_str_3_pre, prom_4_str_3_post)
#print(r9)

#Str_4
prom_4_str_4_pre = prom_4_pre["40 En el último mes Tengo reacciones físicas desagradable cuando pienso en la enfermedad (por ejemplo, latidos cardiacos muy fuertes, problemas para respirar, sudoración)"]
prom_4_str_4_post = prom_4_post["40 En el último mes Tengo reacciones físicas desagradable cuando pienso en la enfermedad (por ejemplo, latidos cardiacos muy fuertes, problemas para respirar, sudoración)"]
r10 = md.anova(prom_4_str_4_pre, prom_4_str_4_post)
#print(r10)


#Str_5
prom_4_str_5_pre = prom_4_pre["44 En el último mes Pienso que si me enfermo o se enferma alguien de mi familia, es por mi culpa"]
prom_4_str_5_post = prom_4_post["44 En el último mes Pienso que si me enfermo o se enferma alguien de mi familia, es por mi culpa"]
r11 = md.anova(prom_4_str_5_pre, prom_4_str_5_post)
#print(r11)


#Str_6
prom_4_str_6_pre = prom_4_pre["48 En el último mes Siento que mi futuro es incierto a partir de que comenzó el riesgo a padecer esta enfermedad"]
prom_4_str_6_post = prom_4_post["48 En el último mes Siento que mi futuro es incierto a partir de que comenzó el riesgo a padecer esta enfermedad"]
r12 = md.anova(prom_4_str_6_pre, prom_4_str_6_post)
#print(r12)

#Str_7
prom_4_str_7_pre = prom_4_pre["53 En el último mes Me siento asustada(o) por los riesgos a padecer esta enfermedad"]
prom_4_str_7_post = prom_4_post["53 En el último mes Me siento asustada(o) por los riesgos a padecer esta enfermedad"]
r13 = md.anova(prom_4_str_7_pre, prom_4_str_7_post)
#print(r13)


#################################################################################
#Avoidance
#Avo_1
prom_4_avo_1_pre = prom_4_pre["41.En el último mes Evito pensar, sentir o hablar sobre la enfermedad"]
prom_4_avo_1_post = prom_4_post["41.En el último mes Evito pensar, sentir o hablar sobre la enfermedad"]
r14 = md.anova(prom_4_avo_1_pre, prom_4_avo_1_post)
#print(r14)


#Avo_2
prom_4_avo_2_pre = prom_4_pre["42. En el último mes Evito ver o recurrir a información oficial sobre la enfermedad"]
prom_4_avo_2_post = prom_4_post["42. En el último mes Evito ver o recurrir a información oficial sobre la enfermedad"]
r15 = md.anova(prom_4_avo_2_pre, prom_4_avo_2_post)
#print(r15)


#Avo_3
prom_4_avo_3_pre = prom_4_pre["43. En el último mes Tengo dificultad para recordar lo que recomiendan las autoridades para enfrentar el riesgo o la enfermedad"]
prom_4_avo_3_post = prom_4_post["43. En el último mes Tengo dificultad para recordar lo que recomiendan las autoridades para enfrentar el riesgo o la enfermedad"]
r16 = md.anova(prom_4_avo_3_pre, prom_4_avo_3_post)
#print(r16)

###################################################################################

#Distancing
#Dis_1
prom_4_dis_1_pre = prom_4_pre["45. En el último mes He perdido interés por las actividades que antes disfrutaba"]
prom_4_dis_1_post = prom_4_post["45. En el último mes He perdido interés por las actividades que antes disfrutaba"]
r17 = md.anova(prom_4_dis_1_pre, prom_4_dis_1_post)
#print(r17)


#Dis_2
prom_4_dis_2_pre = prom_4_pre["46. En el último mes Me siento distante de las personas con quienes convivo, a partir de que inició el riesgo de esta enfermedad"]
prom_4_dis_2_post = prom_4_post["46. En el último mes Me siento distante de las personas con quienes convivo, a partir de que inició el riesgo de esta enfermedad"]
r18 = md.anova(prom_4_dis_2_pre, prom_4_dis_2_post)
#print(r18)


#Dis_3
prom_4_dis_3_pre = prom_4_pre["49. En el último mes Siento que deseo hacer cosas para hacerme daño"]
prom_4_dis_3_post = prom_4_post["49. En el último mes Siento que deseo hacer cosas para hacerme daño"]
r19 = md.anova(prom_4_dis_3_pre, prom_4_dis_3_post)
#print(r19)

#Dis_4
prom_4_dis_4_pre = prom_4_pre["50. En el último mes Tengo dificultad para quedarme dormido o seguir durmiendo"]
prom_4_dis_4_post = prom_4_post["50. En el último mes Tengo dificultad para quedarme dormido o seguir durmiendo"]
r20 = md.anova(prom_4_dis_4_pre, prom_4_dis_4_post)
#print(r20)


#Dis_5
prom_4_dis_5_pre = prom_4_pre["51. En el último mes Me siento enojada (o)"]
prom_4_dis_5_post = prom_4_post["51. En el último mes Me siento enojada (o)"]
r21 = md.anova(prom_4_dis_5_pre, prom_4_dis_5_post)
#print(r21)

#########################################################################


#Information seeking
#Inf_1
prom_4_inf_1_pre = prom_4_pre["64. Actualmente Leo (o me intereso por programas de televisión o radio) sobre enfermedades físicas graves"]
prom_4_inf_1_post = prom_4_post["64. Actualmente Leo (o me intereso por programas de televisión o radio) sobre enfermedades físicas graves"]
r22 = md.anova(prom_4_inf_1_pre, prom_4_inf_1_post)
#print(r22)

#Somatization
#Som_1
prom_4_som_1_pre = prom_4_pre["62. Actualmente Creo que padezco alguna enfermedad física grave (aunque no me la han confirmado)"]
prom_4_som_1_post = prom_4_post["62. Actualmente Creo que padezco alguna enfermedad física grave (aunque no me la han confirmado)"]
r23 = md.anova(prom_4_som_1_pre, prom_4_som_1_post)
#print(r23)


###############################################################################


