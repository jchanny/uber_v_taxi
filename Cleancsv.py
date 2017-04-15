import pandas as pd
import numpy as np

#returns dataframe storing cleaned up excel file
def cleanNYC(file_name):
    #col names available in file:
    #vendor_id,pickup_datetime,dropoff_datetime,passenger_count,trip_distance,
    #pickup_longitude,pickup_latitude,rate_code,store_and_fwd_flag,
    #dropoff_longitude,dropoff_latitude,payment_type,fare_amount,surcharge,
    #mta_tax,tip_amount,tolls_amount,total_amount
    df=pd.read_csv(file_name);
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
    return df

def cleanUber(file_name):
    df=pd.read_csv(file_name);

cleanNYC('yellow_tripdata_2014-10.csv').to_pickle('nyc1.pkl')
cleanNYC('yellow_tripdata_2014-11.csv').to_pickle('nyc2.pkl')
cleanNYC('yellow_tripdata_2014-12.csv').to_pickle('nyc3.pkl')
cleanNYC('yellow_tripdata_2015-01.csv').to_pickle('nyc4.pkl')

cleanUber('uber-10-2014.csv').to_pickle('uber1.pkl')
cleanUber('uber-11-2014.csv').to_pickle('uber2.pkl')
cleanUber('uber-12-2014.csv').to_pickle('uber3.pkl')
cleanUber('uber-1-2015.csv').to_pickle('uber4.pkl')


