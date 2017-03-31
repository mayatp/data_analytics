import numpy as np
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble.forest import RandomForestRegressor
from sklearn.feature_selection import SelectKBest, f_classif, f_regression
import matplotlib.pyplot as plt
from sklearn import tree

def correlation_matrix(df,lb,tit):
    from matplotlib import pyplot as plt
    from matplotlib import cm as cm
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    cmap = cm.get_cmap('jet', 30)
    cax = ax1.imshow(df.corr(), interpolation="nearest", cmap=cmap)
    #ax1.grid(True)
    plt.title(tit)
    labels=lb
    #ax1.set_xticklabels(labels,fontsize=6)
    #ax1.set_yticklabels(labels,fontsize=6)
    # Add colorbar, make sure to specify tick locations to match desired ticklabels
    fig.colorbar(cax, ticks=np.divide(range(-10,11,1),10.))
    plt.show()

#from sklearn.linear_model import LinearRegressor

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
print len(predictors)
target = "admitted"

X = merge_df[predictors]
Y = merge_df[target]
Y = np.array(Y)

correlation_matrix(merge_df[['income', 'cycling','fp_rate'] + food_feats1], feats_of_interest, 'Non-food features')
    
