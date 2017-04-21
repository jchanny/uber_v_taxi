import pandas as pd

df=pd.read_hdf('nyc1.h5')
df2=df.iloc[:20]

df2.to_pickle('test.pkl')
print df2
#df=pd.read_pickly(file_name)
