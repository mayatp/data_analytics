#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 20:06:55 2017

@author: mayapetranova
"""

import pandas as pd
import matplotlib.pyplot as plt
#simple data visualisation

data = pd.read_excel('obesity_over_regions.xlsx')
data.set_index('year', inplace=True)
data.plot()
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()
plt.ylabel('Rate')
plt.title('Admission rates in different regions')
plt.savefig('obesity_over_regions.png') #saving the image as png
