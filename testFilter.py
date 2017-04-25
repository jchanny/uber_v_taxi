import pandas as pd
import h5py

def filterTest(filename,weekend):
    df=pd.read_csv(filename)
    index=pd.Series(['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','00'])
    #weekday and weekend are the actual price per mile
    columns=['weekday_price','weekday_distance','weekday','weekend_price','weekend_dist','weekend']
    filteredDf=pd.DataFrame(index=index,columns=columns)
    weekendlistIndex=0
    for x in xrange(len(df)):
        tipamt=df.iloc[x]['tip_amount']
        totaltemp=df.iloc[x]['total_amount']
        df.loc[x,'total_amount']=totaltemp-tipamt
        pickup_datetime=df.iloc[x]['pickup_datetime']
        pickup_datetime=pickup_datetime[11:13]
        pickup_date=df.iloc[x]['pickup_datetime']
        pickup_date=pickup_date[8:10]
        #figure out how to do determine if weekend
        filteredDf.loc[pickup_datetime]['weekday_price']+=totaltemp-tipamt
    return filteredDf
    

weekendList=[4,5,11,12,18,19,25,26]
df2=filterTest('test.csv',weekendList)
print df2
