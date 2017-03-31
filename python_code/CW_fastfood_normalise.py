import numpy as np
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble.forest import RandomForestRegressor
from sklearn.feature_selection import SelectKBest, f_classif, f_regression
import matplotlib.pyplot as plt
from sklearn import tree
#from sklearn.linear_model import LinearRegressor
workbook = pd.ExcelFile('Fast_food_metadata_and_summary_local_authority_data.xlsx') 
fastfood_df = workbook.parse("Local Authority Data",index_col=0, skiprows=3)
fastfood_df = fastfood_df.rename(columns=({ 'PHE Centre' : 'Region'}))

workbook = pd.ExcelFile('pythonUpload_PopAgeRegion.xlsx') 
population_by_year_df = workbook.parse("Upload")

workbook = pd.ExcelFile('ONS_Region_LookUp.xlsx') 
lookup = workbook.parse("Sheet1")

england_fastfood_df = fastfood_df.groupby("Region").sum()
england_fastfood_df["Region"] = england_fastfood_df.index
england_fastfood_df.reindex(['North East', 'North West', 'Yorkshire and the Humber', 'East Midlands', 'West Midlands', 'East of England', 'London', 'South East', 'South West'])

bar_w = 0.30
plt.barh(range(9) ,england_fastfood_df['Count of outlets'],bar_w)
plt.yticks(range(9),('North East', 'North West', 'Yorkshire and the Humber', 'East Midlands', 'West Midlands', 'East of England', 'London', 'South East', 'South West'), rotation=0)
plt.title('Count of fast food place')
plt.subplots_adjust(left = 0.3)
plt.savefig('fastfood_count.png')
plt.close()

england_fastfood_df = pd.merge(england_fastfood_df, lookup, how = 'left', on = 'Region')
england_fastfood_df = pd.merge(england_fastfood_df,population_by_year_df.loc[population_by_year_df["Year"]=="2010/11"],how='left',on = 'ONS')
england_fastfood_df['Count of outlets'] = england_fastfood_df['Count of outlets']/england_fastfood_df['All']*100000

bar_w = 0.30
plt.barh(range(9) ,england_fastfood_df['Count of outlets'],bar_w)
plt.yticks(range(9),('North East', 'North West', 'Yorkshire and the Humber', 'East Midlands', 'West Midlands', 'East of England', 'London', 'South East', 'South West'), rotation=0)
plt.title('Count of fast food place per 100,000 population')
plt.subplots_adjust(left = 0.3)
plt.savefig('fastfood_normalised.png')

writer = pd.ExcelWriter('normalised_fastfood.xlsx', engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
england_fastfood_df.to_excel(writer, sheet_name='Sheet1')
# Close the Pandas Excel writer and output the Excel file.
writer.save()

