#create model to predict when uber cheaper than taxi
import numpy as np
import pandas as pd
import sklearn
import sklearn.linear_model as lm
import sklearn.model_selection as ms
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
import matplotlib.pyplot as plt

nyc1=pd.read_csv('nyc1.csv')
nyc2=pd.read_csv('nyc2.csv')
nyc3=pd.read_csv('nyc3.csv')
#joining dataframes together
index=pd.Series(['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24'])
nyc=pd.DataFrame(index=index)
nyc[:]=0.0
weekday=[]
weekend=[]
#merging dataframes together into one
for x in xrange(len(nyc)):
    time1=nyc1.iloc[x]['weekday']
    time2=nyc2.iloc[x]['weekday']
    time3=nyc3.iloc[x]['weekday']
    time4=nyc1.iloc[x]['weekend']
    time5=nyc2.iloc[x]['weekend']
    time6=nyc3.iloc[x]['weekend']
    weekday.append((time1+time2+time3)/3)
    weekend.append((time4+time5+time6)/3)
nyc['weekday']=pd.Series(weekday,index=nyc.index)
nyc['weekend']=pd.Series(weekend,index=nyc.index)
nyc['time']=pd.Series([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],index=nyc.index)

nyc.to_csv('nyc.csv')
del nyc1,nyc2,nyc3

#plotting a graph of NYC weekday vs weekday price graph
plt.plot(nyc[['time']],nyc[['weekday']],label='weekday price')
plt.plot(nyc[['time']],nyc[['weekend']],label='weekend price')
plt.title('Price per mile/time')
plt.ylabel('Price')
plt.xlabel('Time (24 hours)')
plt.legend()
plt.savefig('nyc_price-graph.png')
plt.gcf().clear()

uber1=pd.read_csv('uber1.csv')
uber2=pd.read_csv('uber2.csv')
uber3=pd.read_csv('uber3.csv')
index=pd.Series(['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24'])
uber=pd.DataFrame(index=index)
uber[:]=0.0
weekday=[]
weekend=[]
#merging dataframes together into one
for x in xrange(len(uber)):
    time1=uber1.iloc[x]['weekday']
    time2=uber2.iloc[x]['weekday']
    time3=uber3.iloc[x]['weekday']
    time4=uber1.iloc[x]['weekend']
    time5=uber2.iloc[x]['weekend']
    time6=uber3.iloc[x]['weekend']
    weekday.append((time1+time2+time3)/3)
    weekend.append((time4+time5+time6)/3)
uber['weekday']=pd.Series(weekday,index=uber.index)
uber['weekend']=pd.Series(weekend,index=uber.index)
uber['time']=pd.Series([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],index=uber.index)

uber.to_csv('uber.csv')
del uber1,uber2,uber3

plt.plot(uber[['time']],uber[['weekday']],label='weekday price')
plt.plot(uber[['time']],uber[['weekend']],label='weekend price')
plt.title('Price per mile/time')
plt.ylabel('Price')
plt.xlabel('Time (24 hours)')
plt.legend()
plt.savefig('uber_price-graph.png')
plt.gcf().clear()


#creating linear regression model to compare uber and yellow taxi

#weekday prediction for NYC
x=nyc.time
y=nyc.weekday
svr_rbf=SVR(kernel='rbf',C=1e3,gamma=0.1)
y_rbf=svr_rbf.fit(x.reshape(len(x),1),y).predict(x.reshape(len(x),1))
plt.plot(x.reshape(len(x),1),y_rbf,label='weekday NYC prediction')
#weekend prediction for NYC
y=nyc.weekend
y_rbf=svr_rbf.fit(x.reshape(len(x),1),y).predict(x.reshape(len(x),1))
plt.plot(x.reshape(len(x),1),y_rbf,label='weekend NYC prediction')
#weekday prediction for UberX
x=uber.time
y=uber.weekday
y_rbf=svr_rbf.fit(x.reshape(len(x),1),y).predict(x.reshape(len(x),1))
plt.plot(x.reshape(len(x),1),y_rbf,label='weekday uber prediction')
#weekend prediction for UberX
x=uber.time
y=uber.weekend
y_rbf=svr_rbf.fit(x.reshape(len(x),1),y).predict(x.reshape(len(x),1))
plt.plot(x.reshape(len(x),1),y_rbf,label='weekend uber prediction')
plt.legend()
plt.ylabel('Price')
plt.xlabel('Time (24 hours)')
plt.title('Predicted price/time')
plt.savefig('predicted-price.png')

#seeing how accurate prediction is:

