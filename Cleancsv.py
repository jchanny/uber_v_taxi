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

cleanNYC('yellow_tripdata_2014-04.csv').to_pickle('nyc4.pkl')
cleanNYC('yellow_tripdata_2014-05.csv').to_pickle('nyc5.pkl')
cleanNYC('yellow_tripdata_2014-06.csv').to_pickle('nyc6.pkl')
cleanNYC('yellow_tripdata_2014-07.csv').to_pickle('nyc7.pkl')
cleanNYC('yellow_tripdata_2014-08.csv').to_pickle('nyc8.pkl')
cleanNYC('yellow_tripdata_2014-09.csv').to_pickle('nyc9.pkl')
cleanNYC('yellow_tripdata_2015-01.csv').to_pickle('nyc10.pkl')
cleanNYC('yellow_tripdata_2015-02.csv').to_pickle('nyc11.pkl')
cleanNYC('yellow_tripdata_2015-03.csv').to_pickle('nyc12.pkl')
cleanNYC('yellow_tripdata_2015-04.csv').to_pickle('nyc13.pkl')
cleanNYC('yellow_tripdata_2015-05.csv').to_pickle('nyc14.pkl')
cleanNYC('yellow_tripdata_2015-06.csv').to_pickle('nyc15.pkl')


