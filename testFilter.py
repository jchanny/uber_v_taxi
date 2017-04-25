import pandas as pd
import h5py

def filterTest(filename,weekend):
    df=pd.read_csv(filename)
    index=pd.Series(['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','00'])
    #weekday and weekend are the actual price per mile
    columns=['weekday_price','weekday_distance','weekday','weekend_price','weekend_dist','weekend']
    filteredDf=pd.DataFrame(index=index,columns=columns)
    filteredDf[:]=0.0
    currentDate=01
    weekendIndex=0
    isWeekend=False
    #filling in values for the filtered dataframe
    for x in xrange(len(df)):
        tipamt=df.iloc[x]['tip_amount']
        totaltemp=df.iloc[x]['total_amount']
        df.loc[x,'total_amount']=totaltemp-tipamt
        pickup_time=df.iloc[x]['pickup_datetime']
        pickup_time=pickup_time[11:13]
        pickup_date=df.iloc[x]['pickup_datetime']
        pickup_date=pickup_date[8:10]
        
        if pickup_date!=currentDate:
            currentDate=pickup_date

        for y in xrange(len(weekend)):
            if currentDate==weekend[y]:
                isWeekend=True
            
        distance=df.iloc[x]['trip_distance']
        
        if isWeekend==False:
            filteredDf.loc[pickup_time]['weekday_price']+=totaltemp-tipamt
            filteredDf.loc[pickup_time]['weekday_distance']+=distance
            
        if isWeekend==True:
            filteredDf.loc[pickup_time]['weekend_price']+=totaltemp-tipamt
            filteredDf.loc[pickup_time]['weekend_dist']+=distance
            
        if filteredDf.loc[pickup_time]['weekday_price']!=0 and filteredDf.loc[pickup_time]['weekday_distance']!=0:
            filteredDf.loc[pickup_time]['weekday']=filteredDf.loc[pickup_time]['weekday_price']/filteredDf.loc[pickup_time]['weekday_distance']
        if filteredDf.loc[pickup_time]['weekend_price']!=0 and filteredDf.loc[pickup_time]['weekend_price']!=0:
            filteredDf.loc[pickup_time]['weekend']=filteredDf.loc[pickup_time]['weekend_price']/filteredDf.loc[pickup_time]['weekend_dist']

        isWeekend=False
    return filteredDf

weekendList=['04','05','11','12','18','19','25','26']
df2=filterTest('test.csv',weekendList)
print df2
df2.to_csv('filtered.csv')
