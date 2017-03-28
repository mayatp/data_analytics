#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 11:59:06 2017

@author: mayapetranova
"""

import pandas as pd
import numpy as np

data = pd.read_excel('pandas_simple_updated.xlsx')
col_idx = ['Bread, rice and cereals', 'Pasta products', 'Buns, cakes, biscuits etc', 'Pastry (savoury)', 'Beef (fresh, chilled or frozen)',	'Pork (fresh, chilled or frozen)',	'Lamb (fresh, chilled or frozen)',	'Poultry (fresh, chilled or frozen)',	'Bacon and ham',	'Other meat and meat preparations', 'Fish and fish products',	'Milk', 'Cheese and curd',	'Eggs',	'Other milk products', 'Butter', 'Margarine, other vegetable fats and peanut butter', 'Cooking oils and fats', 'Fresh fruit', 'Other fresh, chilled or frozen fruits', 'Dried fruit and nuts',	'Preserved fruit and fruit based products',	'Fresh vegetables', 'Dried vegetables',	'Other preserved or processed vegetables',	'Potatoes',	'Other tubers and products of tuber vegetables', 'Sugar and sugar products', 'Jams, marmalades', 'Chocolate', 'Confectionery products', 'Edible ices and ice cream', 'Other food products', 'Coffee', 'Tea', 'Cocoa and powdered chocolate',	'Fruit and vegetable juices (inc. fruit squash)', 'Mineral or spring waters', 'Soft drinks (inc. fizzy and ready to drink fruit drinks)', 'Spirits and liqueurs (brought home)', 'Wines, fortified wines (brought home)', 'Beer, lager, ciders and perry (brought home)',	'Alcopops (brought home)', 'Cigarettes', 'Cigars, other tobacco products and narcotics']

food = 'Food and non-alc'
drinks = 'Alcoholic drink, tobacco and narcotics'
food_drinks = data[food] + data[drinks] #getting the total for food and drinks totals for normalisation over all the food and drink products later

food_drinks_total = pd.Series.to_frame(food_drinks) #series to dataframe in order to join it later to the main dataframe
all_data = pd.DataFrame.join(data, food_drinks_total, how='left') #joining new results to the data frame
all_data = all_data.rename(columns={0: 'food_drinks_total'}) #rename a column

denominator_col = 'food_drinks_total'

def GetPercentage_df_col(df_input, col_idx, denominator_col):
	df_output = df_input
	df_output[col_idx] = df_input[col_idx].apply(lambda x: x / df_input[denominator_col])
	return df_output

DF_NEW = GetPercentage_df_col(all_data, col_idx, denominator_col) # we've got the new_data generated with the new column merged in
print(DF_NEW)

#ref http://xlsxwriter.readthedocs.io/example_pandas_simple.html
# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_all_normalised.xlsx', engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
DF_NEW.to_excel(writer, sheet_name='Sheet1')
# Close the Pandas Excel writer and output the Excel file.
writer.save()

