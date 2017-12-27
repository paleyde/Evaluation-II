import pandas as pd
data=pd.read_csv('/home/pallabeedey/Downloads/ping-api-etherdelta-com.csv',sep=' ')
data=data[['56(84)','of']]
data=data.rename(columns={'56(84)':'icmp_seq','of':'time'})
data['time']=data['time'].str.replace('time=', '')
data['icmp_seq']=data['icmp_seq'].str.replace('icmp_seq=', '')
data=data.set_index('icmp_seq')
col1=['mean_period5','mean_period10','mean_period20']
col2=['StdDev_period5','StdDev_period10','StdDev_period20']
period = [5,10,20]
for i,j in zip(col1,period):
    data[i]=data['time'].rolling(window=j).mean()
for i,j in zip(col2,period):
    data[i]=data['time'].rolling(window=j).std()
data.to_csv('output_ping-api-etherdelta-com.csv')

