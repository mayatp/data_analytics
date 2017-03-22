#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:38:26 2017

@author: clairekelleher


Feature ranking (used code from Titanic - SelectKBest)
"""

# Recursive Feature Elimination

from sklearn.feature_selection import SelectKBest, f_classif



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Upload data
dictionary = {}
dictionary.clear()
workbook = pd.ExcelFile('all.xlsx') 
for sheet_name in workbook.sheet_names:
	df = workbook.parse(sheet_name) 
	dictionary[sheet_name] = df

features = [ 'year', 'All_Under_16', 'All_16_24', 'All_25_34', 'All_35_44', 'All_45_54', 'All_55_64', 'All_65_74', 'All_75_Over', 'income', 'income_m', 'income_f', 'ft', 'pt', 'cycling', 'fastfood_places', 'fp_rate', 'all_ethnic', 'White', 'Gypsy / Traveller / Irish Traveller', 'Mixed / Multiple Ethnic Groups',	'Asian / Asian British: Indian', 'Asian / Asian British: Pakistani', 'Asian / Asian British: Bangladeshi', 'Asian / Asian British: Chinese', 'Asian / Asian British: Other Asian', 'Black / African / Caribbean / Black British', 'Other Ethnic Group']
#predictors = ['yr', '2_all_ages', '2_under_16', '2_16_24', '2_25_34', '2_35_44', '2_45_54', '2_55_64', '2_65_74', '2_75_over', '2_unknown_age', 'n_jobs', 'annual_income', 'annual_income_m', 'annual_income_f', 'full_time', 'part_time', 'Cycling_E12000001']
data = df[features]
target = df["admitted"]

selector = SelectKBest(f_classif, k=7)
selector.fit(df[features], target)
weight = -np.log10(selector.pvalues_)
plt.bar(range(len(features)), weight)
plt.xticks(range(len(features)), features, rotation="vertical")
plt.show()



