#identifying unique posibility answers
(anounc_1_pre["2. En el último mes hubo pérdida de familia/conocido"]).nunique()

#This loop makes a Paired t test for all the events after measuring the leng of all the pre and post groups per event

a = []
b = [anounc_1_pre,
anounc_2_pre,
anounc_3_pre,
measures_1_pre,
measures_2_pre,
measures_3_pre,
prom_1_pre,
prom_2_pre,
prom_3_pre,
prom_4_pre,
fest_1_pre,
fest_2_pre,
earth_vs_1_pre  
    ]
for event in b:
    c = len(event)
    a.append(c)
    
print(a)

a1 = []
b1 = [anounc_1_post,
anounc_2_post,
anounc_3_post,
measures_1_post,
measures_2_post,
measures_3_post,
prom_1_post,
prom_2_post,
prom_3_post,
prom_4_post,
fest_1_post,
fest_2_post,
earth_vs_1_post  
    ]
for event in b1:
    c = len(event)
    a1.append(c)
    
print(a1)

md.pre_post_ttest(a, a1)


#locating something

np.mean(anounc_1_pre["54 Durante las últimas 2 semanas Me he sentido nerviosa(o), ansiosa(o) o con los nervios de punta"])

#Selecting a specific date

eval_date = (df_1["fecha"] == "4/17/2020")
eval_date = df_1[eval_date]
print(len(eval_date["54 Durante las últimas 2 semanas Me he sentido nerviosa(o), ansiosa(o) o con los nervios de punta"]))

#or this way

eval_date = (df_1["fecha"] == "6/24/2020")
eval_date = df_1[eval_date]
print(len(eval_date))


#meassuring lenght of time periods
anounc_1
start_date = "4/14/2020"
end_date = "4/19/2020"
filtered_df = df_1[(df_1['fecha'] >= start_date) & (df_1['fecha'] <= end_date)]
lengths = filtered_df["54 Durante las últimas 2 semanas Me he sentido nerviosa(o), ansiosa(o) o con los nervios de punta"].apply(lambda x: np.linalg.norm(x))
print(lengths)

#for performing t-test using the max as comparison against the daily mean

a = []
max_post_72 = np.array([542, 195, 157, 569, 409, 175, 198, 176, 279, 55, 317, 76, 2531])
b = [anounc_1_pre,
anounc_2_pre,
anounc_3_pre,
measures_1_pre,
measures_2_pre,
measures_3_pre,
prom_1_pre,
prom_2_pre,
prom_3_pre,
prom_4_pre,
fest_1_pre,
fest_2_pre,
earth_vs_1_pre  
    ]
for event in b:
    c = len(event)/3
    c = np.around(c,3)
    a.append(c)

a = np.asarray(a)
print(a)
print(max_post_72)
md.pre_post_ttest(a, max_post_72)


#second option (for festivities and earthquakes it was imposible to use this test

daily_mean_pre = np.array([347, 303, 922.333, 256, 417, 195.667, 372, 61, 44.667, 58.333, 231.333, 38.333, 92]) 
max_post_72 = np.array([542, 195, 157, 569, 409, 175, 198, 176, 279, 55, 317, 76, 2531])

anouncement_daily_mean_pre = daily_mean_pre[0:2]
anouncement_max_post_72 = max_post_72[0:2]
anouncement = md.pre_post_ttest(anouncement_daily_mean_pre, anouncement_max_post_72)

measures_daily_mean_pre = daily_mean_pre[3:5]
measures_max_post_72 = max_post_72[3:5]
measures = md.pre_post_ttest(measures_daily_mean_pre, measures_max_post_72)

prom_daily_mean_pre = daily_mean_pre[6:9]
prom_max_post_72 = max_post_72[6:9]
promotion = md.pre_post_ttest(prom_daily_mean_pre, prom_max_post_72)


#for getting the percentage increment between daily media and maximus for by type of event

daily_mean_pre = np.array([347, 303, 922.333, 256, 417, 195.667, 372, 61, 44.667, 58.333, 231.333, 38.333, 92]) 
max_post_72 = np.array([542, 195, 157, 569, 409, 175, 198, 176, 279, 55, 317, 76, 2531])
md.compare_mean_max(daily_mean_pre, max_post_72)

anouncement_daily_mean_pre = sum(daily_mean_pre[0:2])
anouncement_max_post_72 = sum(max_post_72[0:2])
md.compare_mean_max(anouncement_daily_mean_pre, anouncement_max_post_72)

measures_daily_mean_pre = sum(daily_mean_pre[3:5])
measures_max_post_72 = sum(max_post_72[3:5])
md.compare_mean_max(measures_daily_mean_pre, measures_max_post_72)

prom_daily_mean_pre = sum(daily_mean_pre[6:9])
prom_max_post_72 = sum(max_post_72[6:9])
md.compare_mean_max(prom_daily_mean_pre, prom_max_post_72)

fest_daily_mean_pre = sum(daily_mean_pre[10:11])
fest_max_post_72 = sum(max_post_72[10:11])
md.compare_mean_max(fest_daily_mean_pre, fest_max_post_72)
