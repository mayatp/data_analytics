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
#names represent different features, the order they are defined must match the order of the imported data
dataframe = pd.read_excel('annual_maya.xlsx', 'all_in', names=names)
#print(dataframe)


array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
# feature extraction
test = SelectKBest(score_func=chi2, k=4)
fit = test.fit(X, Y)
# summarize scores
numpy.set_printoptions(precision=3)
print(fit.scores_)
features = fit.transform(X)
# summarize selected features
print(features[0:5,:])
