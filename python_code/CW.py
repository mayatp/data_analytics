import numpy as np
import pandas as pd
from sklearn import linear_model


## All these use pd.ExcelFile.parse to read the file, index_col indicates which column which be used as index, otherwise it would use 0,1,2,3...
##### Read Target Table --  Master 2013-2015  #####
workbook = pd.ExcelFile('Obesity Admission.xlsx') 
target = {}
df_target_1314 = workbook.parse("year_1314") 
df_target_1415 = workbook.parse("year_1415") 
CountyONS = df_target_1314.index # obtain the County ONS in target data

##### Read Lookup Table - Lookup_ONS #####
# workbook = pd.ExcelFile('Lookup_ONS.xlsx') 
# df_lookup = workbook.parse("Lookup",index_col=2) 

##### Read Variable Table - Enthic Breakdown 2011 #####
workbook = pd.ExcelFile('Enthic breakdown_2011.xlsx') 
df_enthic = workbook.parse("ByCounty") 

##### Read Variable Table - Annual Income #####
workbook = pd.ExcelFile('annual_earnings_cleanedup.xlsx') 
df_annual_income = workbook.parse("Sheet1",index_col=0) 

# Just checking if all County ONS in target file is available in variable file
# you can replace df_enthic by other variables' dataframe for checking
for ONS in CountyONS:
	if ONS not in df_enthic.index:
		print "ONS not found in enthic list... : " + ONS
	#else:
		#print  df_enthic["White"][ONS]
print df_enthic.ix[ONS]

# This joins the 2 dataframes tgt, based on the County ONS
# but after joining some values become NaN

#df_target_concat = pd.concat([df_target_1314,df_target_1415])

merge_df = pd.merge(df_target_1314,df_enthic, on = 'County ONS', how = 'left').dropna(how='any')

# Import regressor
regr = linear_model.LinearRegression()


#In [5]: a.reset_index().merge(b, how="left").set_index('index')
# Get X, Y data (X: features, Y: target by county)
array = merge_df.values
X_train = array[:-10,11:].astype('float64')
X_test = array[-10:,11:].astype('float64')
Y_train = array[:-10,5].astype('float64')
Y_test = array[-10:,5].astype('float64')
# regressor for all persons as target
regr.fit(X_train, Y_train)
print regr.coef_
# regressor for male as target
Y_train = array[:-10,6].astype('float64')
regr.fit(X_train, Y_train)
print regr.coef_
# regressor for female as target
Y_train = array[:-10,7].astype('float64')
regr.fit(X_train, Y_train)
print regr.coef_
#print("Mean squared error: %.2f" np.mean((regr.predict(X_test) - Y_test) ** 2))
#print merge_df.columns


