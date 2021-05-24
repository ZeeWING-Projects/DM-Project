import numpy as np
import pandas as pd
import csv


#READING DATA SET

df = pd.read_csv("RealDataSet.csv")

# 1.1 : Replacing shortcuts.

df['Item_Fat_Content'] = df['Item_Fat_Content'].replace(['LF'],'Low Fat')
df['Item_Fat_Content'] = df['Item_Fat_Content'].replace(['reg'],'Regular')

#1.2 : Filling missing values.
#using mean to fill these numeric values....

df['Item_Weight'].fillna((df['Item_Weight'].mean()), inplace=True)

#using some builtinfutions to fill ordinal attriutes...

dist = df.Outlet_Size.value_counts(normalize=True)
nan_outlet_rows = df['Outlet_Size'].isnull()
df.loc[nan_sex_rows,'Outlet_Size'] = np.random.choice(dist.index, size=len(df[nan_outlet_rows]),p=dist.values)

#Now converting string columns to numeric values.


#Wrting back to CSV file.

df.to_csv ('Preprocessed_dataset.csv', index = False, header=True)


















#DONE BY : Zeeshan Ahmed