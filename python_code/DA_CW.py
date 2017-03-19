import numpy as np
import pandas as pd

## All these use pd.ExcelFile.parse to read the file, index_col indicates which column which be used as index, otherwise it would use 0,1,2,3...
##### Read Target Table --  Master 2013-2015  #####
workbook = pd.ExcelFile('Obesity Admission.xlsx') 
target = {}
df_target = workbook.parse("Master 2013-2015",index_col=3) 
CountyONS = df_target.index # obtain the County ONS in target data

##### Read Lookup Table - Lookup_ONS #####
# workbook = pd.ExcelFile('Lookup_ONS.xlsx') 
# df_lookup = workbook.parse("Lookup",index_col=2) 

##### Read Variable Table - Enthic Breakdown 2011 #####
workbook = pd.ExcelFile('Enthic breakdown_2011.xlsx') 
df_enthic = workbook.parse("ByCounty",index_col=3) 

##### Read Variable Table - Annual Income #####
workbook = pd.ExcelFile('annual_earnings_cleanedup.xlsx') 
df_annual_income = workbook.parse("Sheet1",index_col=0) 

# Just checking if all County ONS in target file is available in variable file
# you can replace df_enthic by other variables' dataframe for checking
#for ONS in CountyONS:
#	if ONS not in df_enthic.index:
#		print "ONS not found in enthic list... : " + ONS
#	else:
#		print  df_enthic["White"][ONS]
#print df_enthic.ix[ONS]

# This joins the 2 dataframes tgt, based on the County ONS
# but after joining some values become NaN
merge_df = pd.merge(df_target,df_enthic, how = 'left')
print merge_df