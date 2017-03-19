#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 03:22:08 2017

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

from sklearn.decomposition import PCA

array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
# feature extraction
pca = PCA(n_components=3) #number of com
fit = pca.fit(X)
# summarize components
print(("Explained Variance: %s") % fit.explained_variance_ratio_)
print(fit.components_)

