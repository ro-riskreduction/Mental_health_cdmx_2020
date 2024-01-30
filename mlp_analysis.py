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
from sklearn import neighbors
from sklearn import svm
from sklearn.preprocessing import RobustScaler
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score
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


#scaling

scaler = preprocessing.StandardScaler()
scaler.fit(features_array)
features_scaled_standard = scaler.transform( features_array )
#print( features_scaled_standard )

#scaling with robustscaling to scale outliers

transformer_robust = RobustScaler().fit(features_array)
#transformer
#RobustScaler()
features_scaled_robust = transformer_robust.transform(features_array)
#print( features_scaled_robust )

#mapping using quantiles using standard scaling

transformer_quantiles = preprocessing.QuantileTransformer(output_distribution='normal')

features_quantile_mapping_standard  = transformer_quantiles.fit_transform( features_scaled_standard )

#print(features_quantile_mapping_standard)

#mapping using quantiles using robust scaling

transformer_quantiles_2 = preprocessing.QuantileTransformer(output_distribution='normal')

features_quantile_mapping_robust  = transformer_quantiles_2.fit_transform( features_scaled_robust )

#print(features_quantile_mapping_robust)

#machine learning first part
#raw

#separating it
x_train_raw, x_test_raw, labels_train_raw, labels_test_raw = train_test_split(features_array, ptsd, test_size=0.3, random_state=0)

#training it
mlp_0    = MLPClassifier(solver='lbfgs', max_iter=10000, alpha=0.5, hidden_layer_sizes=(5, 2), random_state=0)
mlp_0.fit(x_train_raw, labels_train_raw)

#evaluating the CRs for the training and test sets":
labels_pred_train_raw = mlp_0.predict(x_train_raw)
labels_pred_test_raw  = mlp_0.predict(x_test_raw)
cr_train          = accuracy_score(labels_train_raw, labels_pred_train_raw)
cr_test           = accuracy_score(labels_test_raw, labels_pred_test_raw)
print( f'Classification rate (training_raw) = {cr_train}' )
print( f'Classification rate (test_raw)     = {cr_test}' )

#iterating it 
niter = 10
cr_g_0  = []

for i in range(niter):
    x_train_raw, x_test_raw, labels_train_raw, labels_test_raw = train_test_split(features_array, ptsd, test_size=0.3, random_state=i)
    mlp_0    = MLPClassifier(solver='lbfgs', max_iter=10000, alpha=0.5, hidden_layer_sizes=(5, 2), random_state=0)
    mlp_0.fit(x_train_raw, labels_train_raw)
    
    labels_pred_test_raw  = mlp_0.predict(x_test_raw)
    cr_train = sklearn.metrics.accuracy_score(labels_test_raw, labels_pred_test_raw)
    cr_g_0.append(cr_train)
    
print(f'Overall classification rate: {np.mean(cr_g_0)}')

plt.figure()
plt.hist(cr_g_0)
plt.xlabel("Clasification rate")
plt.ylabel("Number of simulations")
plt.show()

#Second case
#normalized

#separating it
x_train_nor, x_test_nor, labels_train_nor, labels_test_nor = train_test_split(features_array, ptsd, test_size=0.3, random_state=0)

#normalizing
normalizer = preprocessing.Normalizer()
normalizer.fit(x_train_nor) #just bypass data,does not fits anything

x_train_nor  = normalizer.transform( x_train_nor )
x_test_nor   = normalizer.transform( x_test_nor )

#training it
mlp_1    = MLPClassifier(solver='lbfgs', max_iter=10000, alpha=0.5, hidden_layer_sizes=(5, 2), random_state=0)
mlp_1.fit(x_train_nor, labels_train_nor)

#evaluating the CRs for the training and test sets":
labels_pred_train_nor = mlp_1.predict(x_train_nor)
labels_pred_test_nor  = mlp_1.predict(x_test_nor)
cr_train          = accuracy_score(labels_train_nor, labels_pred_train_nor)
cr_test           = accuracy_score(labels_test_nor, labels_pred_test_nor)
print( f'Classification rate (training_nor) = {cr_train}' )
print( f'Classification rate (test_nor)     = {cr_test}' )

#iterating it 
niter = 10
cr_g_1  = []

for i in range(niter):
    x_train_nor, x_test_nor, labels_train_nor, labels_test_nor = train_test_split(features_array, ptsd, test_size=0.3, random_state=i)
    
    mlp_1    = MLPClassifier(solver='lbfgs', max_iter=10000, alpha=0.5, hidden_layer_sizes=(5, 2), random_state=0)
    mlp_1.fit(x_train_nor, labels_train_nor)
    normalizer = preprocessing.Normalizer()
    normalizer.fit(x_train_nor)
    x_train_nor  = normalizer.transform( x_train_nor )
    x_test_nor   = normalizer.transform( x_test_nor )
    labels_pred_test_nor  = mlp_1.predict(x_test_nor)
    cr_train = sklearn.metrics.accuracy_score(labels_test_nor, labels_pred_test_nor)
    cr_g_1.append(cr_train)
    
print(f'Overall classification rate: {np.mean(cr_g_1)}')

plt.figure()
plt.hist(cr_g_1)
plt.xlabel("Clasification rate")
plt.ylabel("Number of simulations")
plt.show()

#third case
#standard scaling

#separating it
x_train_standard, x_test_standard, labels_train_standard, labels_test_standard = train_test_split(features_quantile_mapping_standard, ptsd, test_size=0.3, random_state=0)

#training it
mlp_2    = MLPClassifier(solver='lbfgs', max_iter=10000, alpha=0.5, hidden_layer_sizes=(5, 2), random_state=0)
mlp_2.fit(features_quantile_mapping_standard, ptsd)

#evaluating the CRs for the training and test sets":
labels_pred_train_standard = mlp_2.predict(x_train_standard)
labels_pred_test_standard  = mlp_2.predict(x_test_standard)
cr_train          = accuracy_score(labels_train_standard, labels_pred_train_standard)
cr_test           = accuracy_score(labels_test_standard, labels_pred_test_standard)
print( f'Classification rate (training_standard) = {cr_train}' )
print( f'Classification rate (test_standard)     = {cr_test}' )

#iterating it 
niter = 10
cr_g_2  = []

for i in range(niter):
    x_train_standard, x_test_standard, labels_train_standard, labels_test_standard = train_test_split(features_quantile_mapping_standard, ptsd, test_size=0.3, random_state=i)
    mlp_2    = MLPClassifier(solver='lbfgs', max_iter=10000, alpha=0.5, hidden_layer_sizes=(5, 2), random_state=0)
    mlp_2.fit(x_train_standard, labels_train_standard)
    
    labels_pred_test_standard  = mlp_2.predict(x_test_standard)
    cr_train = sklearn.metrics.accuracy_score(labels_test_standard, labels_pred_test_standard)
    cr_g_2.append(cr_train)
    
print(f'Overall classification rate: {np.mean(cr_g_2)}')

plt.figure()
plt.hist(cr_g_2)
plt.xlabel("Clasification rate")
plt.ylabel("Number of simulations")
plt.show()

#fourthcase
#robust scaling

#separating it
x_train_robust, x_test_robust, labels_train_robust, labels_test_robust = train_test_split(features_quantile_mapping_robust, ptsd, test_size=0.3, random_state=0)

#training it
mlp_3    = MLPClassifier(solver='lbfgs', max_iter=10000, alpha=0.5, hidden_layer_sizes=(5, 2), random_state=0)
mlp_3.fit(features_quantile_mapping_robust, ptsd)

#evaluating the CRs for the training and test sets":
labels_pred_train_robust = mlp_3.predict(x_train_robust)
labels_pred_test_robust  = mlp_3.predict(x_test_robust)
cr_train          = accuracy_score(labels_train_robust, labels_pred_train_robust)
cr_test           = accuracy_score(labels_test_robust, labels_pred_test_robust)
print( f'Classification rate (training_robust) = {cr_train}' )
print( f'Classification rate (test_robust)     = {cr_test}' )

#iterating it 
niter = 10
cr_g_3  = []

for i in range(niter):
    x_train_robust, x_test_robust, labels_train_robust, labels_test_robust = train_test_split(features_quantile_mapping_robust, ptsd, test_size=0.3, random_state=i)
    mlp_3    = MLPClassifier(solver='lbfgs', max_iter=10000, alpha=0.5, hidden_layer_sizes=(5, 2), random_state=0)
    mlp_3.fit(x_train_robust, labels_train_robust)
    
    labels_pred_test_robust  = mlp_3.predict(x_test_robust)
    cr_train = sklearn.metrics.accuracy_score(labels_test_robust, labels_pred_test_robust)
    cr_g_3.append(cr_train)
    
print(f'Overall classification rate: {np.mean(cr_g_3)}')

plt.figure()
plt.hist(cr_g_3)
plt.xlabel("Clasification rate")
plt.ylabel("Number of simulations")
plt.show()
