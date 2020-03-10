
#This program predicts stock prices by using Machine Learning Models 

#Install the dependecies 
import quandl
import numpy as np 

from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR #support vector machine (machine learning algorithim)
from sklearn.model_selection import train_test_split #method to split and train data 

#Get the stock data 
df = quandl.get("WIKI/FB")

#Take a look at the data 
print(df.head())
