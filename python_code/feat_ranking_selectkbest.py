#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:38:26 2017

@author: clairekelleher

"""
from sklearn.feature_selection import SelectKBest, f_regression

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Upload data
dictionary = {}
dictionary.clear()
workbook = pd.ExcelFile('pandas_simple_updated.xlsx') 
for sheet_name in workbook.sheet_names:
	df = workbook.parse(sheet_name) 
	dictionary[sheet_name] = df

target = df["admitted"]


#List of all features
df.columns

#####Feature removal#####
#Removed features that we didn't have number for, for the following year. Ie. All ages
#And features that wouldn't effect model. Ie All ethnics is the equivalent to total population. 
#'Food' is the total of all the sub food groups so it was also removed
#REMOVED:
#'ONS', 'year', 'admitted', 'All_Under_16', 'All_16_24', 'All_25_34',
#'All_35_44', 'All_45_54', 'All_55_64', 'All_65_74', 'All_75_Over',
#'income_m', 'income_f', 'ft', 'pt', 'Food', 'all_ethnic',

non_food_features = [
'income', 'cycling',
 'fp_rate', 'White',
'Gypsy / Traveller / Irish Traveller', 'Mixed / Multiple Ethnic Groups',
'Asian / Asian British: Indian', 'Asian / Asian British: Pakistani',
'Asian / Asian British: Bangladeshi', 'Asian / Asian British: Chinese',
'Asian / Asian British: Other Asian',
'Black / African / Caribbean / Black British', 'Other Ethnic Group']

selector = SelectKBest(f_regression, k=7) #Regresion selector
selector.fit(df[non_food_features], target)
selector.transform(df[non_food_features])
weight = -np.log10(selector.pvalues_)
plt.bar(range(len(non_food_features)), weight)
plt.xticks(range(len(non_food_features)), non_food_features, rotation="vertical")
plt.show()

food_feats1 = ['Bread, rice and cereals', 'Pasta products',
'Buns, cakes, biscuits etc', 'Pastry (savoury)',
'Beef (fresh, chilled or frozen)', 'Pork (fresh, chilled or frozen)',
'Lamb (fresh, chilled or frozen)', 'Poultry (fresh, chilled or frozen)',
'Bacon and ham', 'Other meat and meat preparations',
'Fish and fish products', 'Milk', 'Cheese and curd', 'Eggs',
'Other milk products', 'Butter',
'Margarine, other vegetable fats and peanut butter',
'Cooking oils and fats', 'Fresh fruit',
'Other fresh, chilled or frozen fruits', 'Dried fruit and nuts',
'Preserved fruit and fruit based products', 'Fresh vegetables',
'Dried vegetables', 'Other preserved or processed vegetables']

selector.fit(df[food_feats1], target)
selector.transform(df[food_feats1])
weight = -np.log10(selector.pvalues_)
plt.bar(range(len(food_feats1)), weight)
plt.xticks(range(len(food_feats1)), food_feats1, rotation="vertical")
plt.show()

food_feats2 = ['Potatoes', 'Other tubers and products of tuber vegetables',
'Sugar and sugar products', 'Jams, marmalades', 'Chocolate',
'Confectionery products', 'Edible ices and ice cream',
'Other food products', 'Non-alcoholic drinks', 'Coffee', 'Tea',
'Cocoa and powdered chocolate',
'Fruit and vegetable juices (inc. fruit squash)',
'Mineral or spring waters',
'Soft drinks (inc. fizzy and ready to drink fruit drinks)',
'Alcoholic drink, tobacco and narcotics', 'Alcoholic drinks',
'Spirits and liqueurs (brought home)',
'Wines, fortified wines (brought home)',
'Beer, lager, ciders and perry (brought home)',
'Alcopops (brought home)', 'Tobacco and narcotics1', 'Cigarettes',
'Cigars, other tobacco products and narcotics']

selector.fit(df[food_feats2], target)
selector.transform(df[food_feats2])
weight = -np.log10(selector.pvalues_)
plt.bar(range(len(food_feats2)), weight)
plt.xticks(range(len(food_feats2)), food_feats2, rotation="vertical")
plt.show()