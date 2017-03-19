#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 07:07:14 2017

@author: mayapetranova
"""
#https://realpython.com/blog/python/analyzing-obesity-in-england-with-python/

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.ExcelFile("annual_maya.xlsx")
#print (data.sheet_names) #print sheet names

data_age = data.parse('admissions_age_gr_prim_sec')

data_age.set_index('year', inplace=True)

data_age_minus_total = data_age.drop('2_all_ages', axis=1) # Drop the total column and plot
print (data_age_minus_total)
data_age_minus_total.plot()
plt.gca().invert_xaxis() # inverting the axis to better plot the resuls

#kids vs adults (comparing any values)
plt.close()

data_age['2_under_16'].plot(label="Under 16")
data_age['2_35_44'].plot(label="35-44")
plt.legend(loc="upper right")
plt.gca().invert_xaxis()

#nonesense PREDICTIONS just fitting polynomial
#Here, we extract the values for children under 16. 
#For the x axis, the original graph had dates. 
#To simplify our graph, we’ll just be using the the numbers 0-10.
plt.close()
kids_values = data_age['2_under_16'].values
x_axis = range(len(kids_values))
poly_degree = 4
#higher values are tightly coupled to this graph, they make prediction useless
curve_fit = np.polyfit(x_axis, kids_values, poly_degree)
poly_interp = np.poly1d(curve_fit)
#using the numpy ployfit() function to fit the graph through the data
#ploy1d() function is called on the equation, generated to create a function
poly_fit_values = [] 

for i in range(len(x_axis)):
    poly_fit_values.append(poly_interp(i))
    #loop from 1-10, calling the function ploy_interp()
    
# plotting original and our data to check how the equation reached the real data
plt.plot(x_axis, poly_fit_values, "-r", label = "Fitted")
plt.plot(x_axis, kids_values, "-b", label = "Orig")
plt.legend(loc="upper right")
plt.gca().invert_xaxis()

#re-running the poly_interp() function for values 0-15 (i.e predicting 5y. in the future)

x_axis2 = range(15)

poly_fit_values = []
for i in range(len(x_axis2)):
    poly_fit_values.append(poly_interp(i))
    
plt.plot(x_axis2, poly_fit_values, "-r", label = "Fitted")

plt.legend(loc="upper right")
#plt.gca().invert_xaxis()


