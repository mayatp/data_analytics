#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 21:11:26 2017

@author: mayapetranova
"""
#http://machinelearningmastery.com/feature-selection-machine-learning-python/
import pandas as pd
import numpy
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
# load data
names = ['yr','2_all_ages','2_under_16','2_16_24','2_25_34','2_35_44','2_45_54','2_55_64','2_65_74','2_75_over','obese']
dataframe = pd.read_excel('annual_maya.xlsx', 'all_in', names=names)
#print(dataframe)
#all_data.isnull().any() #check if any missing values

# Feature Extraction with RFE

from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

array = dataframe.values
X = array[:,0:9]
Y = array[:,9]
# feature extraction
model = LogisticRegression()
rfe = RFE(model, 3)
fit = rfe.fit(X, Y)
print(("Num Features: %d") % fit.n_features_)
print(("Selected Features: %s") % fit.support_)
print(("Feature Ranking: %s") % fit.ranking_)
print(names) #print features 
