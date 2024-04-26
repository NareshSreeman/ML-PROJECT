# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session






#Importing necessary libraries
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')




# Imoirting the data
data = pd.read_csv('/kaggle/input/road-accident-severity-in-india/Road.csv')



# Imoirting the data
data = pd.read_csv('/kaggle/input/road-accident-severity-in-india/Road.csv')



data.columns # Columns in the table


data.info()

data.isnull().sum() # Null values in a dataset 



data.dropna(inplace=True) # Dropping values

data.isnull().sum() # The data is clean now



plt.figure(figsize = (20, 6))
sns.countplot(x='Day_of_week',data=data,palette='Set2')
plt.show()
# Accidents do not seems to have any relation with days of week



plt.figure(figsize = (20, 6))
sns.countplot(x='Sex_of_driver',data=data, palette='Set2')
plt.show() 
#We can see accidents of males occured more as compared to females



plt.figure(figsize = (20, 6))
sns.countplot(x='Age_band_of_driver',data=data,palette='Set2')
plt.show() # Drivers in the range of 18-30 had encountered more number of accidents.



plt.figure(figsize = (20, 6))
sns.countplot(x='Driving_experience',data=data,palette='Set2')
plt.show() 


plt.figure(figsize = (20, 6))
sns.countplot(x='Type_of_vehicle',data=data,palette='Set2')
plt.xticks(rotation=90)
plt.show() # Automobile vehicles tends to had more number of acciedents following by Lorry.


plt.figure(figsize = (20, 6))
sns.countplot(x='Cause_of_accident',data=data,palette='Set2')
plt.xticks(rotation=90)
plt.show() # Major cause of most number of accidents are due to "No distancing"



plt.figure(figsize = (20, 6))
sns.countplot(x='Weather_conditions',data=data,palette='Set2')
plt.xticks(rotation=90)
plt.show() # Weather conditions do not tend to have any major affect as most acciedents occured in Normal weather condition only.


plt.figure(figsize = (20, 6))
sns.countplot(x='Area_accident_occured',data=data,palette='Set2')
plt.xticks(rotation=90)
plt.show() # Most acciends occured near office areas, so according measures should be taken to prevent this.

