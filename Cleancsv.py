import pandas as pd
import numpy as np
import random

def filterNYC(filename,weekend):
    df=pd.read_csv(filename)
    df.drop(df.columns[[0,3,5,6,7,8,9,10,11]],axis=1)
    index=pd.Series(['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24'])
    #weekday and weekend are the actual price per mile
    columns=['weekday_price','weekday_distance','weekday','weekend_price','weekend_dist','weekend']
    filteredDf=pd.DataFrame(index=index,columns=columns)
    filteredDf[:]=0.0
    currentDate=01
    weekendIndex=0
    isWeekend=False

    #randomly select 8000 data points
    r=random.sample(xrange(1,8000000),8000)
    #filling in values for the filtered dataframe
    for x in xrange(len(r)):
        
        totaltemp=df.iloc[r[x]][' fare_amount']
        df.loc[r[x],' total_amount']=totaltemp
        pickup_time=df.iloc[r[x]][' pickup_datetime']
        pickup_time=pickup_time[11:13]
        pickup_date=df.iloc[r[x]][' pickup_datetime']
        pickup_date=pickup_date[8:10]
        if pickup_time=='00':
            pickup_time='24'
            
        if pickup_date!=currentDate:
            currentDate=pickup_date

        #determining if current data point is a weekend
        for y in xrange(len(weekend)):
            if currentDate==weekend[y]:
                isWeekend=True
            
        distance=df.iloc[r[x]][' trip_distance']
        
        if isWeekend==False:
            filteredDf.loc[pickup_time]['weekday_price']+=totaltemp
            filteredDf.loc[pickup_time]['weekday_distance']+=distance
            if filteredDf.loc[pickup_time]['weekday_price']!=0 and filteredDf.loc[pickup_time]['weekday_distance']!=0:
                filteredDf.loc[pickup_time]['weekday']=filteredDf.loc[pickup_time]['weekday_price']/filteredDf.loc[pickup_time]['weekday_distance']
            
        if isWeekend==True:
            filteredDf.loc[pickup_time]['weekend_price']+=totaltemp
            filteredDf.loc[pickup_time]['weekend_dist']+=distance
            if filteredDf.loc[pickup_time]['weekend_price']!=0 and filteredDf.loc[pickup_time]['weekend_price']!=0:
                filteredDf.loc[pickup_time]['weekend']=filteredDf.loc[pickup_time]['weekend_price']/filteredDf.loc[pickup_time]['weekend_dist']
            
        isWeekend=False
    return filteredDf

OctoberWeekendList=['04','05','11','12','18','19','25','26']
nyc1=filterNYC('yellow_tripdata_2014-10.csv',OctoberWeekendList)
nyc1.to_csv('nyc1.csv')
del nyc1

NovemeberWeekendList=['1','2','8','9','15','16','22','23','29','30']
nyc2=filterNYC('yellow_tripdata_2014-11.csv',NovemeberWeekendList)
nyc2.to_csv('nyc2.csv')
del nyc2

DecemberWeekendList=['6','7','13','14','20','21','27','28']
nyc3=filterNYC('yellow_tripdata_2014-12.csv',DecemberWeekendList)
nyc3.to_csv('nyc3.csv')
del nyc3

def filterUber(filename):
    df=pd.read_csv(filename)
    weekday=[]
    weekend=[]
    for x in xrange(len(df)):
        #adding in base fare charge of $6, and assuming stuck in traffic for 10 mins @rate of .75/min & shortest route of 5.5mi is taken
        adjustedPrice_weekday=(df.iloc[x]['Weekday']+6)
        adjustedPrice_weekday=adjustedPrice_weekday+(15*.75)
        adjustedPrice_weekday=adjustedPrice_weekday/5.5
        weekday.append(adjustedPrice_weekday)
        adjustedPrice_weekend=(df.iloc[x]['Weekend']+6)
        adjustedPrice_weekend=adjustedPrice_weekend+(15*.75)
        adjustedPrice_weekend=adjustedPrice_weekend/5.5
        weekend.append(adjustedPrice_weekend)
    df['weekday']=pd.Series(weekday,index=df.index)
    df['weekend']=pd.Series(weekend,index=df.index)
    del df['Weekday']
    del df['Weekend']
    return df
        

uber1=filterUber('uber-2014-10.csv')
uber1.to_csv('uber1.csv')
del uber1

uber2=filterUber('uber-2014-11.csv')
uber2.to_csv('uber2.csv')
del uber2

uber3=filterUber('uber-2014-12.csv')
uber3.to_csv('uber3.csv')
del uber3

