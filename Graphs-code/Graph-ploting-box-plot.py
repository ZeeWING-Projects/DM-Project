import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt

#READING DATA SET

df = pd.read_csv("Pre-processed-dataset.csv")
data1 = df.loc[df['Item_Type'] == 'Snack Foods']['Item_Weight']
data2 = df.loc[df['Item_Type'] == 'Dairy']['Item_Weight']
data3 = df.loc[df['Item_Type'] == 'Meat']['Item_Weight']
data4 = df.loc[df['Item_Type'] == 'Breads']['Item_Weight']

fig = plt.figure(figsize =(10, 7))
  
# Creating axes instance
ax = fig.add_axes([0, 0, 1, 1])

data = [data1,data2,data3,data4]
  
# Creating plot
bp = ax.boxplot(data)
  
# show plot

plt.xlabel("Our selected 4 attributes wieght")
plt.ylabel("Range")
plt.title("Box-Plot")
plt.show()











#DONE BY ZEESHAN AHMED