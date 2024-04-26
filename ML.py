import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


data = pd.read_csv('/kaggle/input/road-accident-severity-in-india/Road.csv')


data = pd.read_csv('/kaggle/input/road-accident-severity-in-india/Road.csv')


data.columns # Columns in the table


data.info()

data.isnull().sum() # Null values in a dataset 



data.dropna(inplace=True) # Dropping values

data.isnull().sum() # The data is clean now



plt.figure(figsize = (20, 6))
sns.countplot(x='Day_of_week',data=data,palette='Set2')
plt.show()




plt.figure(figsize = (20, 6))
sns.countplot(x='Sex_of_driver',data=data, palette='Set2')
plt.show() 




plt.figure(figsize = (20, 6))
sns.countplot(x='Age_band_of_driver',data=data,palette='Set2')
plt.show()



plt.figure(figsize = (20, 6))
sns.countplot(x='Driving_experience',data=data,palette='Set2')
plt.show() 


plt.figure(figsize = (20, 6))
sns.countplot(x='Type_of_vehicle',data=data,palette='Set2')
plt.xticks(rotation=90)
plt.show()


plt.figure(figsize = (20, 6))
sns.countplot(x='Cause_of_accident',data=data,palette='Set2')
plt.xticks(rotation=90)
plt.show() 


plt.figure(figsize = (20, 6))
sns.countplot(x='Weather_conditions',data=data,palette='Set2')
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize = (20, 6))
sns.countplot(x='Area_accident_occured',data=data,palette='Set2')
plt.xticks(rotation=90)
plt.show() 
