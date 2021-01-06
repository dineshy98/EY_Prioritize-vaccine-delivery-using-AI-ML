# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 19:19:53 2020

@author: dineshy86
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


main = pd.read_csv('S:/Hackathons/EY/datasets/main.csv')

main['state_population'] = pd.merge(main,main[['state' ,'population_x']].groupby(['state']).sum(),on= 'state')['population_x_y']
main['ccp_district'] = main['No.CCP']*(main['population_x']/main['state_population'])
main['cce_district'] = main['No.CCE']*(main['population_x']/main['state_population'])


cluster = pd.DataFrame(main['District_Key'])

cluster['conf/popu'] = main['Confirmed']/main['population_x']
cluster['district_density'] = main['density']

cluster['deaths'] = main['Deceased']


main.drop(main[main['state'] == 'Ladakh'].index,inplace = True)

cluster1 = pd.DataFrame(main[['population_x','Confirmed','Active','Deceased','cce_district','ccp_district']])

cluster1['Active'].plot()



fig = plt.figure(figsize = (15,15))
fig.subplots_adjust(wspace=0.5)
fig.subplots_adjust(hspace=0.5)

x = ['population_x','Confirmed','Active','Deceased','cce_district','ccp_district']

title = ['population_x','Confirmed','Active','Deceased','cce_district','ccp_district']


for i,j,title in zip(range(1,7),x,title):
    ax = fig.add_subplot(3, 2, i)
    dist_comp = cluster1[j].plot(kind = 'kde',ax = ax,title = title)

from sklearn.preprocessing import StandardScaler
ss1 = StandardScaler()
ss2 = StandardScaler()
ss3 = StandardScaler()
ss4 = StandardScaler()
ss5 = StandardScaler()
ss6 = StandardScaler()

cluster1['population_x'] = ss1.fit_transform(cluster1[['population_x']])
cluster1['Confirmed'] = ss1.fit_transform(cluster1[['Confirmed']])
cluster1['Active'] = ss1.fit_transform(cluster1[['Active']])
cluster1['Deceased'] = ss1.fit_transform(cluster1[['Deceased']])
cluster1['cce_district'] = ss1.fit_transform(cluster1[['cce_district']])
cluster1['ccp_district'] = ss1.fit_transform(cluster1[['ccp_district']])


#optimal clusters


X = pd.DataFrame(cluster1)
X = X.values
from sklearn.cluster import KMeans
wcss = []
for i in range(1,20):
    km = KMeans(n_clusters = i,init='k-means++', max_iter=300, n_init=10, random_state=0)
    km.fit(X)
    wcss.append(km.inertia_)
plt.plot(range(1,20),wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('wcss')
plt.show()


km8=KMeans(n_clusters=8,init='k-means++', max_iter=300, n_init=10, random_state=0)
y_means = km8.fit_predict(X)

cluster1['cluster'] = y_means
main['cluster'] = y_means











