import pandas as pd
import numpy as np
import h5py

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
    return df

def cleanUber(file_name):
    df=pd.read_csv(file_name);

#df1=cleanNYC('yellow_tripdata_2014-10.csv')
#df1.to_hdf('nyc1.h5','data',mode='w',format='table')
#del df1

df2=cleanNYC('yellow_tripdata_2014-11.csv')
df2.to_hdf('nyc2.h5','data',mode='w',format='table')
del df2

df3=cleanNYC('yellow_tripdata_2014-12.csv')
df3.to_hdf('nyc3.h5','data',mode='w',format='table')
del df3

df4=cleanNYC('yellow_tripdata_2015-01.csv')
df4.to_hdf('nyc4.h5','data',mode='w',format='table')
del df4



