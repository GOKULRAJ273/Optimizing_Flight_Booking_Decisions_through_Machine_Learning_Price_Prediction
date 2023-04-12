# -*- coding: utf-8 -*-
"""Copy of output columns.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H2xQjePgMG6cCnP73q26WoZejr4ocBLL
"""

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns
from sklearn.model_selection import train_test_split

xlsx_file = pd.read_excel('/content/Data_Train.xlsx')

csv_file = '/content/Data_Train.csv'

xlsx_file.to_csv(csv_file, index=None, header=True)

data=pd.read_csv('/content/Data_Train.csv')

data.head()

data.Destination.unique



data.Date_of_Journey = data.Date_of_Journey.str.split('/')

data.Date_of_Journey

data['Date']=data.Date_of_Journey.str[0]
data['Month']=data.Date_of_Journey.str[1]
data['Year']=data.Date_of_Journey.str[2]

data.Total_Stops.unique()

#since the maximum number of is 4, there should be maximum 6 cities in any particular route.we split the data in route column
data.Route=data.Route.str.split('->')
data.Route

data['city1']=data.Route.str[0]
data['city2']=data.Route.str[1]
data['city3']=data.Route.str[2]
data['city4']=data.Route.str[3]
data['city5']=data.Route.str[4]
data['city6']=data.Route.str[5]



#In the similar manner,we split the Dep_time column,and create separate columns of departure hours and minutes-
data.Dep_Time=data.Dep_Time.str.split(':')

data['Dep_Time_Hour']=data.Dep_Time.str[0]
data['Dep_Time_Mins']=data.Dep_Time.str[1]

data.Arrival_Time=data.Arrival_Time.str.split('')

data['Arrival_date']=data.Arrival_Time.str[1]
data['Time_of_Arrival']=data.Arrival_Time.str[0]

data['Time_of_Arrival']=data.Time_of_Arrival.str.split(':')

data['Arrival_Time_Hour']=data.Time_of_Arrival.str[0]
data['Arrival_Time_Mins']=data.Time_of_Arrival.str[1]

#Next, we divide the 'Duration' column to 'Travel_mins'

data.Duration=data.Duration.str.split(' ')

data['Travel_Hours']=data.Duration.str[0]
data['Travel_Hours']=data['Travel_Hours'].str.split('h')
data['Travel_Hours']=data['Travel_Hours'].str[0]
data.Travel_Hours=data.Travel_Hours
data['Travel_Mins']=data.Duration.str[1]

data.Travel_Mins=data.Travel_Mins.str.split('m')
data.Travel_Mins=data.Travel_Mins.str[0]

#We also treat the 'Total_stops' column, and replace non-stop flights with 0 value and extract the integer part of the'Total_stops'
data.Total_Stops.replace('non-stop',0,inplace=True)
data.Total_Stops=data.Total_Stops.str.split(' ')
data.Total_Stops=data.Total_Stops.str[0]

data.Additional_Info.unique()

data.Additional_Info.replace('No Info','No Info',inplace=True)

data.isnull().sum()

#we also drop some columns like 'city6' and 'city5',since majority of the data in these columns was NaN(null)
data.drop(['city4','city5','city6'],axis=1,inplace=True)

data.drop(['Arrival_Time_Mins',],axis=1, inplace=True)
data.drop(['Travel_Mins'],axis=1,inplace=True)

#check Null values
data.isnull().sum()

"""# Replacing Missing Value"""

#filling  total_stop as none, missing valuees are less
data['Total_Stops'].fillna('None',inplace=True)

#filling  city1 as none, missing valuees are less
data['city1'].fillna('None',inplace=True)

#filling  city2 as none, missing valuees are less
data['city2'].fillna('None',inplace=True)

#filling  city3 as none, missing valuees are less
data['city3'].fillna('None',inplace=True)

#filling  Travel_Mins as Zero
data['Route'].fillna(0,inplace=True)

data.info()

#changing the numerical colums from object to int
data.Date=data.Date.astype('int64')
data.Month=data.Month.astype('int64')
data.Year=data.Year.astype('int64')
data.Dep_Time_Hour=data.Dep_Time_Hour.astype('int64')
#data.Dep_Time_Mins=data.Dep_Time_Mins.astype('int64')
data.Arrival_date=data.Arrival_date.astype('int64')
#data.Travel_Hours=data.Travel_Hours.astype('int64')
#data.Travel_Mins=data.Travel_Mins.astype('int64')

data[data['Travel_Hours']=='5']



data.head()

data.isnull().any()

categorical=['Airline','source','Destination','Additional_info','City1']
numerical=['Total_Stop','Date','Month','Year','Dep_Time_Hour','Dep_time_Mins','Arrival_date','Arrival_Time_Hour',
           'Arrival_time_mins','Travel_Hours','Travel_Mins']

data.info()

#remove missing value
data.dropna(inplace=True)

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

data.Airline=le.fit_transform(data.Airline)
data.Source=le.fit_transform(data.Source)
data.city1=le.fit_transform(data.city1)
data.city2=le.fit_transform(data.city2)
data.city3=le.fit_transform(data.city3)
data.Additional_Info=le.fit_transform(data.Additional_Info)

#outlput columns
data.head()

data = data[['Airline','Destination','Date','Month','Year','Dep_Time_Hour','Arrival_date','Price']]

data.head()

"""EDA"""

data.describe()

c=1
plt.figure(figsize=(20,45))

sns.distplot(data['Price'])

sns.boxplot(data['Price'])

y=data['Price']
x=data.drop(columns=['Price'],axis=1)

from sklearn.preprocessing import StandardScaler 
ss=StandardScaler()

data['Destination'] = data['Destination'].apply(float)

plt.figure(figsize=(12,5))
plt.subplot(131)
sns.countplot(df['Duration'],hue=df['Price'])
plt.subplot(132)
sns.countplot(df['Route'],hue=df['Price']

for i in categorical:
  plt.subplot(6,3,c)
  sns.countplot(data[i])
  plt.xticks(rotation=90)
  plt.tight_layout(pad=3.0)
  c=c+1
  plt.show( )

x_scaled = pd.DataFrame(x_scaled,columns=x.colums)

data.head()

x_scaled = ss.fit_transform(x)


