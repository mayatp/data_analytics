#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:38:26 2017

@author: clairekelleher


Feature ranking with recursive feature elimination 
and cross-validated selection of the best number of features.

Reference: http://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html


"""

from sklearn.svm import SVC
from sklearn.cross_validation import StratifiedKFold
from sklearn.feature_selection import RFECV
from sklearn.datasets import make_classification
from sklearn.preprocessing import normalize
from sklearn.datasets import make_friedman1
from sklearn.feature_selection import RFECV
from sklearn.svm import SVR

#Upload data
dictionary = {}
dictionary.clear()
workbook = pd.ExcelFile('annual_all_features_last.xlsx') 
for sheet_name in workbook.sheet_names:
	df = workbook.parse(sheet_name) 
	dictionary[sheet_name] = df


predictors = ['yr', '2_all_ages', '2_under_16', '2_16_24', '2_25_34', '2_35_44', '2_45_54', '2_55_64', '2_65_74', '2_75_over', '2_unknown_age', 'n_jobs', 'annual_income', 'annual_income_m', 'annual_income_f', 'full_time', 'part_time', 'Cycling_E12000001']
X = df[predictors]
y = df["E12000001"]

estimator = SVR(kernel="linear")

selector = RFECV(estimator, step=1, cv=5)
selector = selector.fit(X, y)

selector.support_

#Ranks features 
selector.ranking_