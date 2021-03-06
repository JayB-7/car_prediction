# -*- coding: utf-8 -*-
"""car.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CBi2gH49JzxZQEdtezLvskHAqpcifLgt
"""

import pandas as pd

df = pd.read_csv('car data.csv')
df.drop(columns=['Car_Name'],inplace=True)

df['no_of_year'] = 2021 - df['Year']

df.drop(columns=['Year'],inplace=True)

df = pd.get_dummies(df,drop_first=True)

X = df.iloc[:,1:]
y = df.iloc[:,0]

#Feature Importance
from sklearn.ensemble import ExtraTreesRegressor
model = ExtraTreesRegressor()
model.fit(X,y)

print(model.feature_importances_)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

X_train.shape

from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor()

rf.fit(X_train,y_train)

import pickle

file = open('car_prediction.pkl','wb')
pickle.dump(rf,file)

