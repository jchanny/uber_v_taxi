import pandas as pd
import numpy as np

#returns dataframe storing cleaned up excel file
def cleanNYC(file_name):
    #col names available in file:
    #vendor_id,pickup_datetime,dropoff_datetime,passenger_count,trip_distance,
    #pickup_longitude,pickup_latitude,rate_code,store_and_fwd_flag,
    #dropoff_longitude,dropoff_latitude,payment_type,fare_amount,surcharge,
    #mta_tax,tip_amount,tolls_amount,total_amount
    df2=pd.read_pickle(file_name)
    df=df2[:100000]
    df.drop(df.columns[[0,3,5,6,7,8,9,10,11]],axis=1)
    #col names left:
    #pickup_datetime,dropoff_datetime,trip_distance,
    #fare_amount,surcharge,
    #mta_tax,tip_amount,tolls_amount,total_amount
    for x in xrange(len(df)):
        tipamt=df.at[x,'tip_amount']
        totaltemp=df.at[x,'total_amount']
        df.at[x,'total_amount']=totaltemp-tipamt
        totaltemp=df.at[x,'total_amount']
        tollamt=df.at[x,'tolls_amount']
        df.at[x,'total_amount']=totaltemp-tollamt
    del df['tip_amount']
    del df['tolls_amount']
    del df['mta_tax']
    del df['fare_amount']
    del df['surcharge']
    return df;

def cleanUber(file_name):
    df=pd.read_pickle(file_name)

nyc1=cleanNYC('nyc1.pkl')
nyc2=cleanNYC('nyc2.pkl')
nyc3=cleanNYC('nyc3.pkl')
nyc4=cleanNYC('nyc4.pkl')
uber1=cleanUber('uber1.pkl')
uber2=cleanUber('uber2.pkl')
uber3=cleanUber('uber3.pkl')
uber4=cleanUber('uber4.pkl')


