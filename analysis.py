#create model to predict when uber cheaper than taxi
import numpy as np
import pandas as pd
import sklearn
import sklearn.linear_model as lm
import sklearn.model_selection as ms
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

nyc1=pd.read_csv('nyc1.csv')
nyc2=pd.read_csv('nyc2.csv')
nyc3=pd.read_csv('nyc3.csv')
nyc4=pd.read_csv('nyc4.csv')

#joining dataframes together
frames=[nyc1,nyc2,nyc3,nyc4]
nyc=pd.concat(frames)
del nyc1,nyc2,nyc3,nyc4

#use different models for weekday & weekend
data_weekday_nyc=nyc[['weekday']]

data_weekend_nyc=nyc[['weekend']]


