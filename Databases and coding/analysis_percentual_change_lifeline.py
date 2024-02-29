import csv
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import modules as md
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

#date_1 = df_1["fecha"]
#date_1 = date_1.drop(date_1.index[[0]])

date_2 = df_2["fecha"]
date_2 = date_2.drop(date_2.index[[0]])

##################################################################################
#correct times_3
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

anounc_3 = (df_1["fecha"] >= "6/25/2020" ) & (df_1["fecha"] <= "7/1/2020" )
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

measures_2_pre = (df_1["fecha"] >= "5/29/2020" ) & (df_1["fecha"] <= "5/31/2020" )
measures_2_pre = df_1[measures_2_pre]

earth_vs_1_pre = (df_1["fecha"] >= "6/20/2020" ) & (df_1["fecha"] <= "6/22/2020" )
earth_vs_1_pre = df_1[earth_vs_1_pre]

anounc_3_pre = (df_1["fecha"] >= "6/25/2020" ) & (df_1["fecha"] <= "6/27/2020" )
anounc_3_pre = df_1[anounc_3_pre]

measures_3_pre = (df_1["fecha"] >= "6/28/2020" ) & (df_1["fecha"] <= "7/30/2020" )
measures_3_pre = df_1[measures_3_pre]

prom_2_pre = (df_1["fecha"] >= "7/24/2020" ) & (df_1["fecha"] <= "7/26/2020" )
prom_2_pre = df_1[prom_2_pre]

fest_2_pre = (df_1["fecha"] >= "9/13/2020" ) & (df_1["fecha"] <= "9/15/2020" )
fest_2_pre = df_1[fest_2_pre]

prom_3_pre = (df_1["fecha"] >= "9/17/2020" ) & (df_1["fecha"] <= "9/19/2020" )
prom_3_pre = df_1[prom_3_pre]

prom_4_pre = (df_1["fecha"] >= "11/23/2020" ) & (df_1["fecha"] <= "11/25/2020" )
prom_4_pre = df_1[prom_4_pre]

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

anounc_3_post = (df_1["fecha"] >= "6/29/2020" ) & (df_1["fecha"] <= "7/1/2020" )
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

print("Analysis of n uses")
print()

pre_dates = [] 

#comparing using lenght of both time samples

md.compare_means(anounc_1_pre, anounc_1_post)
md.compare_means(anounc_2_pre, anounc_2_post)
md.compare_means(anounc_3_pre, anounc_3_post)
anounc_gen_pre_1 = np.concatenate((anounc_1_pre, anounc_2_pre, anounc_3_pre))
anounc_gen_post_1 = np.concatenate((anounc_1_post, anounc_2_post, anounc_3_post))
md.compare_means(anounc_gen_pre_1, anounc_gen_post_1)



md.len_compare(measures_1_pre, measures_1_post)
md.len_compare(measures_2_pre, measures_2_post)
md.len_compare(measures_3_pre, measures_3_post)
measures_gen_pre_1 = np.concatenate((measures_1_pre, measures_2_pre, measures_3_pre))
measures_gen_post_1 = np.concatenate((measures_1_post, measures_2_post, measures_3_post))
md.len_compare(measures_gen_pre_1, measures_gen_post_1)



md.len_compare(prom_1_pre, prom_1_post)
md.len_compare(prom_2_pre, prom_2_post)
md.len_compare(prom_3_pre, prom_3_post)
md.len_compare(prom_4_pre, prom_4_post)
prom_gen_pre_1 = np.concatenate((prom_1_pre, prom_2_pre, prom_3_pre, prom_4_pre))
prom_gen_post_1 = np.concatenate((prom_1_post, prom_2_post, prom_3_post, prom_4_post))
md.len_compare(prom_gen_pre_1, prom_gen_post_1)




md.len_compare(fest_1_pre, fest_1_post)
md.len_compare(fest_2_pre, fest_2_post)
fest_gen_pre_1 = np.concatenate((fest_1_pre, fest_2_pre))
fest_gen_post_1 = np.concatenate((fest_1_post, fest_2_post))
md.len_compare(fest_gen_pre_1, fest_gen_post_1)


md.len_compare(earth_vs_1_pre, earth_vs_1_post)

#comparing the daily mean -72 hours against the max +72 hours


md.len_compare(anounc_1_pre, anounc_1_post)
md.len_compare(anounc_2_pre, anounc_2_post)
md.len_compare(anounc_3_pre, anounc_3_post)
anounc_gen_pre_1 = np.concatenate((anounc_1_pre, anounc_2_pre, anounc_3_pre))
anounc_gen_post_1 = np.concatenate((anounc_1_post, anounc_2_post, anounc_3_post))
md.len_compare(anounc_gen_pre_1, anounc_gen_post_1)



md.len_compare(measures_1_pre, measures_1_post)
md.len_compare(measures_2_pre, measures_2_post)
md.len_compare(measures_3_pre, measures_3_post)
measures_gen_pre_1 = np.concatenate((measures_1_pre, measures_2_pre, measures_3_pre))
measures_gen_post_1 = np.concatenate((measures_1_post, measures_2_post, measures_3_post))
md.len_compare(measures_gen_pre_1, measures_gen_post_1)



md.len_compare(prom_1_pre, prom_1_post)
md.len_compare(prom_2_pre, prom_2_post)
md.len_compare(prom_3_pre, prom_3_post)
md.len_compare(prom_4_pre, prom_4_post)
prom_gen_pre_1 = np.concatenate((prom_1_pre, prom_2_pre, prom_3_pre, prom_4_pre))
prom_gen_post_1 = np.concatenate((prom_1_post, prom_2_post, prom_3_post, prom_4_post))
md.len_compare(prom_gen_pre_1, prom_gen_post_1)




md.len_compare(fest_1_pre, fest_1_post)
md.len_compare(fest_2_pre, fest_2_post)
fest_gen_pre_1 = np.concatenate((fest_1_pre, fest_2_pre))
fest_gen_post_1 = np.concatenate((fest_1_post, fest_2_post))
md.len_compare(fest_gen_pre_1, fest_gen_post_1)


md.len_compare(earth_vs_1_pre, earth_vs_1_post)

