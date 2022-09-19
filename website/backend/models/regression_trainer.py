# Training the Regression for Professor Review Predictor
#
# Given training data from analyzed photos on faculty website 
# and professor reviews on the DartHub portal, computes coefficients 
# for the four criteria used to predict teaching reviews.
#
# Used in helpers.py
#
# Created by Liam Prevelige, September 2022

import pandas
from sklearn import linear_model
import numpy as np

df = pandas.read_csv("hack-a-thing-1-22f-liam/website/backend/models/regression_training_data.csv")
X = df[['Colorfulness', 'Blur Amount', 'Happy', 'Attractiveness']]
y = df['Rating']

regr = linear_model.LinearRegression()
regr.fit(X, y)

print(regr.coef_)
print(regr.intercept_)
print(regr.get_params())

yhat = regr.predict(X)
SS_Residual = sum((y-yhat)**2)       
SS_Total = sum((y-np.mean(y))**2)     
r_squared = 1 - (float(SS_Residual))/SS_Total
adjusted_r_squared = 1 - (1-r_squared)*(len(y)-1)/(len(y)-X.shape[1]-1)
print(r_squared)
print(adjusted_r_squared)
