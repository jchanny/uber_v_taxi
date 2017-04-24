def filterTest(filename,weekend):
    for x in xrange(len(df)):
        tipamt=df.at[x,'tip_amount']
        totaltemp=df.at[x,'total_amount']
        df.at[x,'total_amount']=totaltemp-tipamt
        totaltemp=df.at[x,'total_amount']
        tollamt=df.at[x,'tolls_amount']
        df.at[x,'total_amount']=totaltemp-tollamt


weekendList=[4,5,11,12,18,19,25,26]
df2=filterTest('test.pkl',weekendList)
