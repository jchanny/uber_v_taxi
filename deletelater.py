import pandas as pd
import h5py

df=pd.read_csv('test.csv')
df2=df
print df2.iloc[1]['tip_amount']
print df2
