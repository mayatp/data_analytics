#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 13:27:25 2017

@author: mayapetranova
"""

import pandas as pd

names = ['yr', '2_all_ages', '2_under_16', '2_16_24', '2_25_34', '2_35_44', '2_45_54', '2_55_64', '2_65_74', '2_75_over', '2_unknown_age', 'n_jobs', 'annual_income', 'annual_income_m', 'annual_income_f', 'full_time', 'part_time', 'Cycling_E12000001', 'Cycling_E12000002', 'Cycling_E12000003', 'Cycling_E12000004', 'Cycling_E12000005', 'Cycling_E12000006', 'Cycling_E12000007', 'Cycling_E12000008', 'Cycling_E12000009', 'E12000001', 'E12000002', 'E12000003', 'E12000004', 'E12000005', 'E12000006', 'E12000007', 'E12000008', 'E12000009']
dataframe = pd.read_excel('annual_all_features_last.xlsx', 'new', names=names)

dataframe.mean() #creates the mean for every feature (later can fill the missing values with it)
full_data_fr = dataframe.fillna(dataframe.mean()) # fill in all the missing values with the mean