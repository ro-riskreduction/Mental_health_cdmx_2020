import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


data_gen_1 = {"Hours" :[12,
36.00,
36.00,
36.00,
36.00,
39.00,
42.00,
44.00,
48.00,
60.00,
54.00
],
        "Percentual change" :[1339.3985,
27.508,
22.6665,
-1.54175,
58.496,
76.074375,
165.934,
21.60133333,
31.42116667,
34.9565,
10.21175
], "events":["Complex earthquake in pandemic",
"Announcements",
"Earthquake medium",
"Earthquake light",
"Stacked event 3 (Earthquake very strong/strong)",
"Promotion of mental health measures",
"Stacked event 2 (Independence day/Promotion onf mental health)",
"Festivities",
"Measures",
"Earthquake VS",
"Stacked event 1 (Announcement and implementation of end of lockdown)"
]}
 
df_gen_1 = pd.DataFrame(data_gen_1)

fig, ax = plt.subplots(figsize=(8, 8))
sns.barplot(x='Hours', y='Percentual change', data=df_gen_1, hue='events')
plt.title("Mean of percentual change of the different events")
plt.xlabel('''Percentual change

Effects along time according to type of events''')
plt.legend(bbox_to_anchor=(1.25, 1), borderaxespad=0)
#fig.text(0.5, 0.0, 'Figure 33. Effects alomg time according to type of events', ha='center')
plt.show()

data_gen_2 = {"Hours" :[
36.00,
36.00,
36.00,
36.00,
39.00,
42.00,
44.00,
48.00,
60.00,
54.00],
        "Percentual change" :[
27.508,
22.6665,
-1.54175,
58.496,
76.074375,
165.934,
21.60133333,
31.42116667,
34.9565,
10.21175], "events":[
"Announcements",
"Earthquake medium",
"Earthquake light",
"Stacked event 3 (Earthquake very strong/strong)",
"Promotion of mental health measures",
"Stacked event 2 (Independence day/Promotion onf mental health)",
"Festivities",
"Measures",
"Earthquake very strong",
"Stacked event 1 (Announcement and implementation of end of lockdown)"
]}
 
df_gen_2 = pd.DataFrame(data_gen_2)
fig, ax = plt.subplots(figsize=(8, 8))    
sns.barplot(x='Hours', y='Percentual change', data=df_gen_2, hue='events')
plt.title("Mean of percentual change of the different events")
plt.xlabel('''Percentual change

Effects along time according to type of events without complex ones 
for better visualization''')
plt.legend(bbox_to_anchor=(1.25, 1), borderaxespad=0)
#fig.text(0.5, 0.0, 'Figure 33. Effects alomg time according to type of events', ha='center')
plt.show()
