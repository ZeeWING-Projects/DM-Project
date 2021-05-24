import numpy as np
import pandas as pd
import csv
import statsmodels.api as sm
import pylab as py
#READING DATA SET

df = pd.read_csv("Pre-processed-dataset.csv")
data1 = df.loc[df['Item_Type'] == 'Snack Foods']['Item_Weight']
data2 = df.loc[df['Item_Type'] == 'Dairy']['Item_Weight']
data3 = df.loc[df['Item_Type'] == 'Meat']['Item_Weight']
data4 = df.loc[df['Item_Type'] == 'Breads']['Item_Weight']

data_item_weight = 

data_points = np.random.normal(0, 1, 100)  

sm.qqplot(data_points, line ='45')  
py.show()
# show plot
