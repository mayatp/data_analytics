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
workbook = pd.ExcelFile('byagegroup.xlsx') 
age_df = workbook.parse("Sheet1")

workbook = pd.ExcelFile('pythonUpload_PopAgeRegion.xlsx') 
population_by_year_df = workbook.parse("Upload")

ageGroup_idx = [u'All_Under_16', u'All_16_24', u'All_25_34',u'All_35_44', u'All_45_54', u'All_55_64', u'All_65_74', u'All_75_Over']
england_pop = population_by_year_df.groupby("Year").sum()
england_pop['Year'] = england_pop.index
merge_df = pd.merge(age_df,england_pop, how = 'left', on = 'Year', suffixes= ['','_pop'])
for age in ageGroup_idx:
    merge_df[age] = merge_df[age] / merge_df[age+'_pop'] * 100
    merge_df = merge_df.drop(age+'_pop', axis = 1)
    
merge_df.dropna(inplace=True) #dropping off empty values from the data frame
df = merge_df.drop('Unknown', 1) # fropping the unknown age people column from the data frame where 1 is the axis number (0 for rows and 1 for columns.)
df_no_all = df.drop('All_ages', axis=1) #Dropping off all ages columns
df_no_all.set_index('Year', inplace=True)

#plot all age groups
df_no_all.plot()
plt.legend(loc="upper left")
plt.xlim(0.5,4.5)
plt.xticks([1,2,3,4,5,6,7,8])
plt.ylabel('Rate')
plt.title('Admission rates over past years')
plt.gca().invert_xaxis()
plt.show()
#plt.savefig('admitted_all_ages.png')
