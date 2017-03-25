import numpy as np
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble.forest import RandomForestRegressor
from sklearn.feature_selection import SelectKBest, f_classif, f_regression
#from sklearn.linear_model import LinearRegressor



def normalise_df(df_input):
	norm = (df_input - df_input.min()) / (df_input.max() - df_input.min())
	return norm

def normalise_df_col(df_input,col_idx):
	df_output = df_input
	df_input[col_idx] = df_input[col_idx].apply(lambda x: (x - x.mean()) / (x.max() - x.min()))
	for col in col_idx:
		df_input_col = df_input[col]
		norm = (df_input_col - df_input_col.min()) / (df_input_col.max() - df_input_col.min())
		df_output[col] = norm
	return df_output

def GetPercentage_df_col(df_input,col_idx, denominator_col):
	df_output = df_input
	df_output[col_idx] = df_input[col_idx].apply(lambda x: x / df_input[denominator_col])
	return df_output

workbook = pd.ExcelFile('pandas_simple_updated.xlsx') 
merge_df = workbook.parse("Sheet1") 



feats_of_interest = [
'income', 'cycling',
 'fp_rate', 'White',
'Gypsy / Traveller / Irish Traveller', 'Mixed / Multiple Ethnic Groups',
'Asian / Asian British: Indian', 'Asian / Asian British: Pakistani',
'Asian / Asian British: Bangladeshi', 'Asian / Asian British: Chinese',
'Asian / Asian British: Other Asian',
'Black / African / Caribbean / Black British', 'Other Ethnic Group']

food_feats1 = ['Food and non-alc', 'Food', 'Bread, rice and cereals', 'Pasta products',
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

predictors = feats_of_interest  + food_feats1 + food_feats2
target = "admitted"

#print len(predictors)

# you can change rf to linear_model.LinearRegression() ... RandomForestRegressor() is another version
rf = RandomForestRegressor()
X = merge_df[predictors]
Y = merge_df[target]
Y = np.array(Y)
## split data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25)
#print rf.fit(X_train, Y_train)
#print np.mean((rf.predict(X_test) - Y_test) ** 2)
# regressor for all persons as target
#print regr.fit(X_train, Y_train)
#print regr.coef_
#print np.mean((regr.predict(X_test) - Y_test) ** 2)
# regressor for male as target
#print merge_df.columns

#perform random forest with top k features, print the predictor error
for selectorK in range(1,len(predictors)):
	selector = SelectKBest(f_regression, k=selectorK)
	selector.fit(X_train, Y_train)
	X_train_k = selector.transform(X_train)
	X_test_k = selector.transform(X_test)
	#print X_train_k.shape
	#weight = -np.log10(selector.pvalues_)
	#print selector.pvalues_
	rf.fit(X_train_k, Y_train)
	print np.mean((rf.predict(X_test_k) - Y_test) ** 2)






