import pandas as pd
import numpy as np

#returns dataframe storing cleaned up excel file
def cleanNYC(file_name):
    df=pd.read_csv(file_name);
    df.drop(df.columns[[0,3,5,6,7,8,9,10,11]],axis=1)
    #remove tip amount
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

cleanUber
cleanUber
cleanUber
cleanUber
cleanUber
cleanUber
cleanUber
cleanUber
cleanUber
cleanUber
cleanUber
cleanUber
