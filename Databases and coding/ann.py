import csv
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from matplotlib.colors import ListedColormap
import sklearn.metrics
from sklearn.model_selection import train_test_split
from mpl_toolkits import mplot3d
from sklearn import neighbors
from sklearn import svm
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import seaborn as sns

df_1 = pd.read_csv("analysis_clean.csv", parse_dates= ["fecha"] )
#df_2 = pd.read_csv("Registros por dia.csv", parse_dates=["fecha"])

#df_1 = pd.read_excel(r"analysis_clean.xlsx", parse_dates= ["fecha"] )
#df_2 = pd.read_excel(r"Registros por dia.xlsx", parse_dates=["fecha"])
#df_3 = pd.read_excel(r"Mobility_google_cdmx_2020.xlsx")
#df_4 = pd.read_excel(r'Defunciones cdmx.xlsx')
#df_5 = pd.read_csv('GT_Noticias.csv')
#df_6 = pd.read_csv('GT_Busqueda_Web.csv')

df_1.set_index("fecha")
#df_2.set_index("fecha")
#I will select the vectors for each quality and convert them to a numpy array

date_1 = df_1["fecha"]
date_1 = date_1.drop(date_1.index[[0]])

#date_2 = df_2["fecha"]
#date_2 = date_2.drop(date_2.index[[0]])


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


#Lost of love ones
lost = df_1["2. En el ultimo mes hubo pérdida de familia/conocido"]
lost = lost.drop(lost.index[[0]])
lost = np.array(lost, dtype=float)

#gender

sex = df_1["9. Sexo"]
sex = sex.drop(sex.index[[0]])
sex = np.array(sex, dtype=float)

#Label PTSD

ptsd = df_1["PTSD"]
ptsd = ptsd.drop(ptsd.index[[0]])
ptsd = np.array(ptsd, dtype=float)

#Label depression

dep = df_1["Depression"]
dep = dep.drop(dep.index[[0]])
dep = np.array(dep, dtype=float)

#Label anxiety

anx_lab = df_1["Axiety"]
anx_lab = anx_lab.drop(anx_lab.index[[0]])
anx_lab = np.array(anx_lab, dtype=float)



#create numpyarrays

anx_array = np.vstack( (anx_1, anx_2, anx_3, anx_4, anx_5, anx_6) ).T

str_array = np.vstack( (str_1, str_2, str_3, str_4, str_5, str_6, str_7) ).T

avo_array = np.vstack( (avo_1, avo_2, avo_3 ) ).T

dis_array = np.vstack( (dis_1, dis_2, dis_3, dis_4, dis_5 ) ).T

features_array = np.vstack( (anx_1, anx_2, anx_3, anx_4, anx_5, anx_6, str_1, str_2, str_3, str_4, str_5, str_6, str_7, avo_1, avo_2, avo_3, dis_1, dis_2, dis_3, dis_4, dis_5, som_1, inf_1  ) ).T

#max_post_72 = np.array([542, 195, 157, 569, 409, 175, 198, 176, 279, 55, 317, 76, 2531])

#daily_mean_pre = np.array([347, 303, 922.333, 256, 417, 195.667, 372, 61, 44.667, 58.333, 231.333, 38.333, 92]) 





#All definitions come from the open textbook located here https://github.com/0todd0000/OpenBook-DataAnalysisPracticeInPythonAndJupyter/blob/master/Lessons/Lesson10/4-ANN/ANN.ipynb

def plot_decision_surface(classifier, x, labels, ax=None, colors=None, n=50, alpha=0.3, marker_size=200, marker_alpha=0.9):
    nlabels   = np.unique( labels ).size
    colors    = plt.cm.viridis( np.linspace(0,1,nlabels) )  if (colors is None) else colors
    ax        = plt.gca() if (ax is None) else ax
    xmin,xmax = x.min(axis=0), x.max(axis=0)
    Xp,Yp     = np.meshgrid( np.linspace(xmin[0],xmax[0],n) , np.linspace(xmin[1],xmax[1],n) )
    xp        = np.vstack( [Xp.flatten(), Yp.flatten()] ).T
    labelsp   = classifier.predict(xp)
    Labelsp   = np.reshape(labelsp, Xp.shape)
    cmap      = ListedColormap(colors)
    for i,label in enumerate( np.unique(labels) ):
        xx   = x[labels==label]
        ax.scatter( xx[:,0], xx[:,1], color=colors[i], s=marker_size, alpha=marker_alpha, label=f'Label = {label}' )
    plt.pcolormesh(Xp, Yp, Labelsp, cmap=cmap, alpha=alpha)
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.axis('equal')
    ax.legend()

#Evaluating the most of love ones on "Y" axis and anx_1 on the "X" axis and using the labels for ptsd

anx_1_str_3 = np.vstack ( ( anx_1, str_3  ) ).T

#df_anx_1 = df_1["54 Durante las últimas 2 semanas Me he sentido nerviosa(o), ansiosa(o) o con los nervios de punta"]
#df_str_3 = df_1["39 En el último mes Me siento preocupada(o) cuando se menciona la enfermedad"]

#df_anx_1_str_3 = (df_anx_1,df_str_3)

    
x0 = anx_1_str_3[ptsd==0]
x1 = anx_1_str_3[ptsd==1]

knc = KNeighborsClassifier(n_neighbors=2)
knc.fit(anx_1_str_3, ptsd)
    
    
print( f'Data shape:    {anx_1_str_3.shape}'  )
print( f'Labels shape:  {ptsd.shape}'  )


print("Using the K neighbors classifier")
#If you want to plot a two dimension array and a label use the following

#plt.figure(figsize=(6,6))
#ax     = plt.axes()
#colors = ['b','r']
#ax.scatter( x0[:,0], x0[:,1], color=colors[0], s=100,  label='Label = 0' )
#ax.scatter( x1[:,0], x1[:,1], color=colors[1], s=100,  label='Label = 1' )

#ax.set_xlabel('Feature 0', alpha=0.05, size=14)
#ax.set_ylabel('Feature 1',alpha=0.05,  size=14)
#ax.axis('equal')
#ax.legend()
#plt.show()


plt.figure()
ax = plt.axes()
plot_decision_surface(knc, anx_1_str_3, ptsd, ax=ax)
plt.xlabel("Anxiety question 54")
plt.ylabel("Acute stress question 39")
plt.title("Example of the use of K neighbors over two features (anxiety and stress) and PTSD label, showing its decision surface")
plt.show()



