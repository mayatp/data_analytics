#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 19:27:23 2017

@author: mayapetranova
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

workbook = pd.ExcelFile('food_places_admissions.xlsx') 
df_all = workbook.parse("Sheet1") 

# data to plot
n_groups = 9 # number of regions according the 

a = 'fp_rate'
b = 'adm'
c = 'food_and_non_alc'

ffp = df_all[a]
adm = df_all[b]
fna = df_all[c]

#normalising fast food places values
fast_food_places = []
for num in ffp:
    fast_food_places.append((num - min(ffp))/(max(ffp)-min(ffp)))
    

food_and_non_alc = []
for num in fna:
    food_and_non_alc.append((num - min(fna))/(max(fna)-min(fna)))


# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_w = 0.30 #setting up the bar width
opacity = 0.8
 
rects1 = plt.bar(index, adm, bar_w,
                 alpha=opacity,
                 color='r',
                 label='Admitted')
rects2 = plt.bar(index + bar_w, food_and_non_alc, bar_w,
                 alpha=opacity,
                 color='g',
                 label='Food spend')
rects3 = plt.bar(index + bar_w + bar_w, fast_food_places , bar_w,
                 alpha=opacity,
                 color='b',
                 label='Fast food stores')
 
plt.xlabel('England Regions')
plt.ylabel('Rate')
plt.title('Rates by region')
plt.xticks(index + bar_w, ('North East', 'North West', 'Yorkshire and the Humber', 'East Midlands', 'West Midlands', 'East of England', 'London', 'South East', 'South West'), rotation=90)
plt.legend(bbox_to_anchor=(1, -0.8))
 
plt.tight_layout()
#plt.show()
plt.savefig('food_places_admissions.png')