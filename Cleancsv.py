import pandas as pd
import numpy as np

#creating is weekend column
    #col names left:
    #pickup_datetime,dropoff_datetime,trip_distance,
    #fare_amount,surcharge,
    #mta_tax,tip_amount,tolls_amount,total_amount
#weekend is an array storing the dates of weekends in that month
#newfile=filename for the filtered df
def CleanNYC(file_name,weekend,newfile):
    index=pd.Series(['1am','2am','3am','4am','5am','6am','7am','8am','9am','10am','11am','12pm','1pm','2pm','3pm','4pm','5pm','6pm','7pm','8pm','9pm','10pm','11pm','12am'])
    columns=['Weekday price','Weekday distance','Weekday','Weekend price','Weekend distance','Weekend']
    filteredDf=pd.DataFrame(index=index,columns=columns)
        
        #code for filtered df
        #figure out time stuff
        

    del df
    filteredDf.to_hdf(newfile,'data',mode=w,format='table')
    del filteredDf
    


-to do: get date format
iterate through the df, determine if that current date is a weekend
get pickup and dropoff time (lets use pickup time for time)
