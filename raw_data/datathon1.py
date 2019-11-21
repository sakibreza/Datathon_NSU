# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 12:06:23 2019

@author: Tanbin Islam Rohan
"""
import pandas as pd

data1= pd.read_csv('train1.csv')

train_data1= pd.DataFrame(data1)
print(train_data1.info())

##
data2= pd.read_csv('train_df2.csv',header=None)

train_data2= pd.DataFrame(data2)
print(train_data2.info())

data3= pd.read_csv('train_df333.csv',header=None)

train_data3= pd.DataFrame(data3)
print(train_data3.info())

data4= pd.read_csv('train_df44.csv',header=None)

train_data4= pd.DataFrame(data4)
print(train_data4.info())
final = pd.concat([train_data1, train_data2 , train_data3 , train_data4])
print(final.info())

x1=train_data1
