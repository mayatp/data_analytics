#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 20:22:00 2017

@author: mayapetranova
"""

#http://machinelearningmastery.com/feature-selection-in-python-with-scikit-learn/

# Recursive Feature Elimination
from __future__ import division
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression 
from sklearn.cross_validation import KFold 
from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.feature_selection import SelectKBest, f_classif
import sys

import pandas 
import matplotlib.pyplot as plt
import numpy as np
import operator
import re


admissions_age = pd.read_excel('annual_maya.xlsx', 'admissions_age_gr_prim_sec')
jobs = pd.read_excel('annual_maya.xlsx', 'jobs')
admissions_gender = pd.read_excel('annual_maya.xlsx', 'adm')
annual = pd.read_excel('annual_maya.xlsx', 'admissioned_region_prim_sec_t77')
#cycling = pd.read_excel('annual_earnings_cleanedup.xlsx', 'cycling')
dataset = pd.merge(admissions_age, jobs, on='year')
dataset2 = pd.merge(dataset, admissions_gender, on='year')
all_data = pd.merge(dataset2, annual, on='year')
#print (data.sheet_names)
#all_data.isnull().any()
predictors = ['yr', 'E12000001',	'E12000002',	'E12000003',	'E12000004',	'E12000005',	'E12000006',	'E12000007',	'E12000008',	'E12000009', '2_all_ages',	'2_under_16', '2_16_24',	'2_25_34', '2_35_44',	'2_45_54',	'2_55_64',	'2_65_74',	'2_75_over',	'2_unknown_age', 'n_jobs', 'annual_income',	'annual_income_m',	'annual_income_f',	'full_time',	'part_time', 'all_m_f', 'male', 'female', 'no_gender']


selector = SelectKBest(f_classif, k=7)
selector.fit(all_data[predictors], all_data["obese"])
weight = -np.log10(selector.pvalues_)
plt.bar(range(len(predictors)), weight)
plt.xticks(range(len(predictors)), predictors, rotation="vertical")
plt.show()


