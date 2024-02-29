
import numpy as np
import pandas as pd
from scipy import stats


def get_frequencies(y):
    return np.array( [(y==i).mean()  for i in range(5)] )
    

df_1 = pd.read_csv("analysis_clean.csv", parse_dates= ["fecha"] )
df_1.set_index("fecha")

print("Contingency analysis")
print()

date_pairs = [
    [("4/14/2020", "4/15/2020"), ("4/17/2020","4/19/2020")],   # anounc_1
    [("4/18/2020", "4/20/2020"), ("4/22/2020","4/24/2020")],   # measures_1
    [("4/23/2020", "4/25/2020"), ("4/27/2020" ,"4/29/2020")],   # prom_1
    [("5/7/2020", "5/9/2020"), ("5/11/2020","5/13/2020")],   
# fest_1
    [("5/10/2020", "5/12/2020"), ("5/14/2020","5/16/2020")],   # anounc_2
    [("5/29/2020", "5/31/2020"), ("6/2/2020","6/4/2020")],   # measures_2
    [("6/20/2020", "6/22/2020"), ("6/24/2020","6/26/2020")],   # earth_vs_1
    [("6/25/2020", "6/27/2020"), ("6/29/2020","7/1/2020")],   # anounc_3
    [("6/28/2020", "6/30/2020"), ("7/2/2020","7/4/2020")],   # measures_3
    [("7/24/2020", "7/26/2020"), ("7/28/2020","7/30/2020")],   #prom_2
    [("9/13/2020", "9/15/2020"), ("9/17/2020","9/19/2020")],   # fest_2
    [("9/17/2020", "9/19/2020"), ("9/21/2020","9/23/2020")],   # prom_3
    [("11/23/2020", "11/25/2020"), ("11/27/2020","11/29/2020")],   # prom_4  
]



names = [
    "54 Durante las últimas 2 semanas Me he sentido nerviosa(o), ansiosa(o) o con los nervios de punta",
    "55 Durante las últimas 2 semanas Me he sentido incapaz de controlar mis preocupaciones",
    "56 Durante las últimas 2 semanas Me he sentido tan inquieta(o) que no he podido quedarme quieta(o)",
    "57 Durante las últimas 2 semanas He tenido dificultad para relajarme",
    "67 Durante las últimas 2 semanas Siento poco interés o placer en hacer cosas",
    "68Durante las últimas 2 semanas Me he sentido decaída(o) deprimida(o) o sin esperanzas",
    "37. En el último mes Pienso o imagino, repetidamente, que voy a enfermar",
    "38. En el último mes Tengo pesadillas que se repiten acerca de la enfermedad",
    "39 En el último mes Me siento preocupada(o) cuando se menciona la enfermedad",
    "40 En el último mes Tengo reacciones físicas desagradable cuando pienso en la enfermedad (por ejemplo, latidos cardiacos muy fuertes, problemas para respirar, sudoración)",
    "44 En el último mes Pienso que si me enfermo o se enferma alguien de mi familia, es por mi culpa",
    "48 En el último mes Siento que mi futuro es incierto a partir de que comenzó el riesgo a padecer esta enfermedad",
    "53 En el último mes Me siento asustada(o) por los riesgos a padecer esta enfermedad",
    "41.En el último mes Evito pensar, sentir o hablar sobre la enfermedad",
    "42. En el último mes Evito ver o recurrir a información oficial sobre la enfermedad",
    "43. En el último mes Tengo dificultad para recordar lo que recomiendan las autoridades para enfrentar el riesgo o la enfermedad",
    "45. En el último mes He perdido interés por las actividades que antes disfrutaba",
    "46. En el último mes Me siento distante de las personas con quienes convivo, a partir de que inició el riesgo de esta enfermedad",
    "49. En el último mes Siento que deseo hacer cosas para hacerme daño",
    "50. En el último mes Tengo dificultad para quedarme dormido o seguir durmiendo",
    "51. En el último mes Me siento enojada (o)",
    "64. Actualmente Leo (o me intereso por programas de televisión o radio) sobre enfermedades físicas graves",
    "62. Actualmente Creo que padezco alguna enfermedad física grave (aunque no me la han confirmado)"
    
]


for (d0a,d0b),(d1a,d1b) in date_pairs:
    i0 = (df_1["fecha"] >= d0a)  &  (df_1["fecha"] <= d0b)  # pre
    i1 = (df_1["fecha"] >= d1a)  &  (df_1["fecha"] <= d1b)  # post
    for name in names:
        y0,y1     = df_1[i0][name], df_1[i1][name]
        f0,f1     = get_frequencies(y0), get_frequencies(y1)
        c         = np.vstack( [f0,f1] ).T  # contingency table
        x2,p,df,_ = stats.chi2_contingency(c)
        print( f' pre: {d0a},{d0b}  ;  post: {d1a},{d1b}' )
        print( f'    {name}'  )
        print( f'    x2={x2:.5f}, p={p:.5f}\n'  )
    print('\n\n\n')

