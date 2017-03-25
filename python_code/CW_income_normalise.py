import numpy as np
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble.forest import RandomForestRegressor
from sklearn.feature_selection import SelectKBest, f_classif, f_regression
#from sklearn.linear_model import LinearRegressor

workbook = pd.ExcelFile('all_with_expenditure.xlsx') 
df_all = workbook.parse("all") 

dg = df_all.groupby(['year']).agg({"income":{"income_mean": 'mean', 'income_std': 'std'}, "income_m":{"income_m_mean": 'mean', 'income_m_std': 'std'},"income_f":{"income_f_mean": 'mean', 'income_f_std': 'std'},"year": {"year": "max"}})
dg.columns = dg.columns.droplevel()
df_all_new = pd.merge(df_all, dg, on = "year")
df_all_new["income"] = (df_all_new["income"] - df_all_new["income_mean"]) / df_all_new["income_std"]
df_all_new["income_m"] = (df_all_new["income_m"] - df_all_new["income_m_mean"]) / df_all_new["income_m_std"]
df_all_new["income_f"] = (df_all_new["income_f"] - df_all_new["income_f_mean"]) / df_all_new["income_f_std"]

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_simple_updated.xlsx', engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
df_all_new.to_excel(writer, sheet_name='Sheet1')
# Close the Pandas Excel writer and output the Excel file.
writer.save()