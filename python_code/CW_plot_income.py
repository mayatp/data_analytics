import numpy as np
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble.forest import RandomForestRegressor
from sklearn.feature_selection import SelectKBest, f_classif, f_regression
import matplotlib.pyplot as plt
from sklearn import tree, svm
from sklearn.model_selection import cross_val_score
import matplotlib.cm as cm

workbook = pd.ExcelFile('pandas_all_normalised.xlsx') 
merge_df = workbook.parse("Sheet1")

#X = merge_df['income']
ONS = []
Reg = ['North East','North West','Yorkshire and Humber','East Midlands','West Midlands','East of England','London','South East', 'South West']
x = np.arange(9)
ys = [i+x+(i*x)**2 for i in range(9)]
colors = cm.rainbow(np.linspace(0, 1, len(ys)))


for i in range(1,10):
    plt.plot(range(7),merge_df.loc[merge_df['ONS'] == 'E1200000'+str(i)]['income'],label = Reg[i-1], color = colors[i-1])

plt.xticks(range(7),["2008/09","2009/10","2010/11","2011/12","2012/13","2013/14","2014/15"])
plt.legend(Reg,loc='center left', bbox_to_anchor=(1, 0.5))
plt.title('Standardised annual income')
plt.ylabel('standard score - annual income')
plt.xlabel('year')
plt.show()


