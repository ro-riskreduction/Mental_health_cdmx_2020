import numpy as np
import pandas as pd
from scipy import stats

   
def anova(x,y):
    a = stats.f_oneway(x, y)
    a = np.around(a, 3)
    return a
    
    
def pre_post_ttest(x,y):
    t,p    = stats.ttest_rel(x, y)
    #t = np.around(t,3)
    #p = np.around(p, 3)
    print(t)
    print(p)
    
df_2 = pd.read_csv("Registros por dia.csv", parse_dates=["fecha"])
df_2.set_index("fecha")

print("Anova analysis")
print()

date_pairs = [
    [("5/29/2020", "5/31/2020"), ("6/2/2020","6/4/2020")],   # measures_2
    [("6/20/2020", "6/22/2020"), ("6/24/2020","6/26/2020")],   # earth_vs_1
    [("6/25/2020", "6/27/2020"), ("6/29/2020","7/1/2020")],   # anounc_3
    [("6/28/2020", "6/30/2020"), ("7/2/2020","7/4/2020")],   # measures_3
    [("7/24/2020", "7/26/2020"), ("7/28/2020","7/30/2020")],   #prom_2
    [("9/13/2020", "9/15/2020"), ("9/17/2020","9/19/2020")],   # fest_2
    [("9/17/2020", "9/19/2020"), ("9/21/2020","9/23/2020")],   # prom_3
    [("11/23/2020", "11/25/2020"), ("11/27/2020","11/29/2020")],   # prom_4  
    
    [("12/22/2020", "12/24/2020"), ("12/26/2020", "12/28/2020")],   # fest_3
    [("3/16/2021", "3/18/2021"), ("3/20/2021", "3/22/2021")],   # earth_l_1
    [("9/4/2021", "9/6/2021"), ("9/8/2021","9/10/2021")],   # earth_vs_2
    [("2/28/2022", "3/2/2022"), ("3/4/2022","3/6/2022")],   # earth_l_2
    [("3/15/2022", "3/17/2022"), ("3/19/2022", "3/21/2022")],   #earth_l_3
    [("8/9/2022", "8/11/2022"), ("8/13/2022", "8/15/2022")],   # earth_l_4
    [("9/16/2022", "9/18/2022"), ("9/20/2022", "9/22/2022")],   # earth_vs_3
    [("9/19/2022", "9/21/2022"), ("9/23/2022", "9/25/2022")],   # earth_s_1
    [("12/8/2022", "12/10/2022"), ("12/12/2022", "12/14/2022")],   # earth_m_1
    [("3/31/2023", "4/2/2023"), ("4/4/2023", "4/6/2023")],   # earth_m_2  
]



names = [
    "Enterqueue", "Connect", "Abandon", "Conectado - Tiempo de espera", "Abandono - Tiempo de espera", "Tiempo en llamada"
    
]


all = []
for (d0a,d0b),(d1a,d1b) in date_pairs:
    i0 = (df_2["fecha"] >= d0a)  &  (df_2["fecha"] <= d0b)  # pre
    i1 = (df_2["fecha"] >= d1a)  &  (df_2["fecha"] <= d1b)  # post
    for name in names:
        y0,y1     = df_2[i0][name], df_2[i1][name]
        r = anova(y0,y1)
        print( f' pre: {d0a},{d0b}  ;  post: {d1a},{d1b}' )
        print( f'    {name}'  )
        print(r)
        all.append(r)
    print('\n\n\n')
