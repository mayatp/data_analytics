import numpy as np
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble.forest import RandomForestRegressor
from sklearn.feature_selection import SelectKBest, f_classif, f_regression
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.svm import SVR
from sklearn.model_selection import KFold

workbook = pd.ExcelFile('pandas_all_normalised.xlsx') 
merge_df = workbook.parse("Sheet1") 
feats_of_interest = [
'income', 'cycling',
 'fp_rate', 'White',
'Gypsy / Traveller / Irish Traveller', 'Mixed / Multiple Ethnic Groups',
'Asian / Asian British: Indian', 'Asian / Asian British: Pakistani',
'Asian / Asian British: Bangladeshi', 'Asian / Asian British: Chinese',
'Asian / Asian British: Other Asian',
'Black / African / Caribbean / Black British', 'Other Ethnic Group']
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
all_food = food_feats1 + food_feats2
target = "admitted"

X = merge_df[all_food]
Y = merge_df[target]
#this part selects the k best features on all food features, based on their weights return by SelectKBest()
#threshold is avg of the weights
selector = SelectKBest(f_regression, k=len(all_food))
selector.fit(X, Y)
weight = -np.log10(selector.pvalues_)
mean = weight.mean()
#for visualisation of weight
plt.barh(range(len(all_food)), weight)
plt.yticks(range(len(all_food)), all_food, rotation="horizontal")
#plt.show()
plt.close()
kBest = sum(weight>=mean) 
print 'Number of selected features:' + str(kBest)
#fit selector
selector = SelectKBest(f_regression, k=kBest)
selector.fit(X, Y)
X = selector.transform(X)
X = np.concatenate((X, merge_df[feats_of_interest]),axis = 1)
# use KFold validation, get average MSE
regr_error = 0.0;svr_error = 0.0;dt_error = 0.0;rf_error = 0.0
regr_error_all = 0.0;svr_error_all = 0.0;dt_error_all = 0.0; rf_error_all = 0.0
regr_error_food = 0.0;svr_error_food = 0.0;dt_error_food = 0.0;rf_error_food = 0.0
regr_error_non = 0.0;svr_error_non = 0.0;dt_error_non = 0.0; rf_error_non = 0.0
k = 3
kf = KFold(n_splits = k)
X_all = merge_df[predictors].as_matrix()
X_food = merge_df[all_food].as_matrix()
X_non = merge_df[feats_of_interest].as_matrix()
Y_mean = Y.mean()

for train,test in kf.split(X):
    ####### Selected features only ######
    X_train, X_test, Y_train, Y_test = X[train], X[test], Y[train], Y[test]
    #Linear regression
    regr = linear_model.LinearRegression()
    regr.fit(X_train, Y_train)
    regr_error  = regr_error + np.mean((regr.predict(X_test) - Y_test) ** 2)
    #SVM regression
    svr = SVR()
    svr.fit(X_train, Y_train)
    svr_error = svr_error + np.mean((svr.predict(X_test) - Y_test) ** 2)
    #Decision tree
    dt = tree.DecisionTreeRegressor(random_state = 74)
    dt.fit(X_train, Y_train)
    dt_error = dt_error + np.mean((dt.predict(X_test) - Y_test) ** 2)
    #Random forest
    rf = RandomForestRegressor(random_state = 88)
    rf.fit(X_train, Y_train)
    rf_error = rf_error + np.mean((rf.predict(X_test) - Y_test) ** 2)
    ####### All features ######
    X_train, X_test, Y_train, Y_test = X_all[train], X_all[test], Y[train], Y[test]
    #Linear regression
    regr = linear_model.LinearRegression()
    regr.fit(X_train, Y_train)
    regr_error_all  = regr_error_all + np.mean((regr.predict(X_test) - Y_test) ** 2)
    #SVM regression
    svr = SVR()
    svr.fit(X_train, Y_train)
    svr_error_all = svr_error_all + np.mean((svr.predict(X_test) - Y_test) ** 2)
    #Decision tree
    dt = tree.DecisionTreeRegressor(random_state = 111)
    dt.fit(X_train, Y_train)
    dt_error_all = dt_error_all + np.mean((dt.predict(X_test) - Y_test) ** 2)
    #Random forest
    rf = RandomForestRegressor(random_state = 0)
    rf.fit(X_train, Y_train)
    rf_error_all = rf_error_all + np.mean((rf.predict(X_test) - Y_test) ** 2)
    ####### Only food features ######
    X_train, X_test, Y_train, Y_test = X_food[train], X_food[test], Y[train], Y[test]
    #Linear regression
    regr = linear_model.LinearRegression()
    regr.fit(X_train, Y_train)
    regr_error_food  = regr_error_food + np.mean((regr.predict(X_test) - Y_test) ** 2)
    #SVM regression
    svr = SVR()
    svr.fit(X_train, Y_train)
    svr_error_food = svr_error_food + np.mean((svr.predict(X_test) - Y_test) ** 2)
    #Decision tree
    dt = tree.DecisionTreeRegressor(random_state = 105)
    dt.fit(X_train, Y_train)
    dt_error_food = dt_error_food + np.mean((dt.predict(X_test) - Y_test) ** 2)
    #Random forest
    rf = RandomForestRegressor(random_state = 125)
    rf.fit(X_train, Y_train)
    rf_error_food = rf_error_food + np.mean((rf.predict(X_test) - Y_test) ** 2)
    ####### Only non food features ######
    X_train, X_test, Y_train, Y_test = X_non[train], X_non[test], Y[train], Y[test]
    #Linear regression
    regr = linear_model.LinearRegression()
    regr.fit(X_train, Y_train)
    regr_error_non  = regr_error_non + np.mean((regr.predict(X_test) - Y_test) ** 2)
    #SVM regression
    svr = SVR()
    svr.fit(X_train, Y_train)
    svr_error_non = svr_error_non + np.mean((svr.predict(X_test) - Y_test) ** 2)
    #Decision tree
    dt = tree.DecisionTreeRegressor(random_state = 105)
    dt.fit(X_train, Y_train)
    dt_error_non = dt_error_non + np.mean((dt.predict(X_test) - Y_test) ** 2)
    #Random forest
    rf = RandomForestRegressor(random_state = 125)
    rf.fit(X_train, Y_train)
    rf_error_non = rf_error_non + np.mean((rf.predict(X_test) - Y_test) ** 2)

#Before anything else....
print "############### training with only selected features ###############"
print "Linear regression"
print "error: {0:.5f}".format(regr_error/k)
print "error percentage: {0:.5f}%".format(regr_error/k/Y_mean*100)
print "SVM regression"
print "error: {0:.5f}".format(svr_error/k)
print "error percentage: {0:.5f}%".format(svr_error/k/Y_mean*100)

print "decision tree"
print "error: {0:.5f}".format(dt_error/k)
print "error percentage: {0:.5f}%".format(dt_error/k/Y_mean*100)

print "random forest"
print "error: {0:.5f}".format(rf_error/k)
print "error percentage: {0:.5f}%".format(rf_error/k/Y_mean*100)

print "############### training with all features ###############"
print "Linear regression"
print "error: {0:.5f}".format(regr_error_all/k)
print "error percentage: {0:.5f}%".format(regr_error_all/k/Y_mean*100)

print "SVM regression"
print "error: {0:.5f}".format(svr_error_all/k)
print "error percentage: {0:.5f}%".format(svr_error_all/k/Y_mean*100)

print "decision tree"
print "error: {0:.5f}".format(dt_error_all/k)
print "error percentage: {0:.5f}%".format(dt_error_all/k/Y_mean*100)

print "random forest"
print "error: {0:.5f}".format(rf_error_all/k)
print "error percentage: {0:.5f}%".format(rf_error_all/k/Y_mean*100)

print "############### training with all food features ###############"
print "Linear regression"
print "error: {0:.5f}".format(regr_error_food/k)
print "error percentage: {0:.5f}%".format(regr_error_food/k/Y_mean*100)

print "SVM regression"
print "error: {0:.5f}".format(svr_error_food/k)
print "error percentage: {0:.5f}%".format(svr_error_food/k/Y_mean*100)

print "decision tree"
print "error: {0:.5f}".format(dt_error_food/k)
print "error percentage: {0:.5f}%".format(dt_error_food/k/Y_mean*100)

print "random forest"
print "error: {0:.5f}".format(rf_error_food/k)
print "error percentage: {0:.5f}%".format(rf_error_food/k/Y_mean*100)

print "############### training with all non food features ###############"

print "Linear regression"
print "error: {0:.5f}".format(regr_error_non/k)
print "error percentage: {0:.5f}%".format(regr_error_non/k/Y_mean*100)

print "SVM regression"
print "error: {0:.5f}".format(svr_error_non/k)
print "error percentage: {0:.5f}%".format(svr_error_non/k/Y_mean*100)

print "decision tree"
print "error: {0:.5f}".format(dt_error_non/k)
print "error percentage: {0:.5f}%".format(dt_error_non/k/Y_mean*100)

print "random forest"
print "error: {0:.5f}".format(rf_error_non/k)
print "error percentage: {0:.5f}%".format(rf_error_non/k/Y_mean*100)



