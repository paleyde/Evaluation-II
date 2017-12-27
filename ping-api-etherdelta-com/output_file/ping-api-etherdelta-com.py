import pandas as pd
data=pd.read_csv('/home/pallabeedey/Downloads/ping-api-etherdelta-com.csv',sep=' ')
data=data[['56(84)','of']]
data=data.rename(columns={'56(84)':'icmp_seq','of':'time'})
data['time']=data['time'].str.replace('time=', '')
data['icmp_seq']=data['icmp_seq'].str.replace('icmp_seq=', '')
data=data.set_index('icmp_seq')
data['mean_period5']=data['time'].rolling(window=5).mean()
data['mean_period10']=data['time'].rolling(window=10).mean()
data['mean_period20']=data['time'].rolling(window=20).mean()
data['StdDev_period5']=data['time'].rolling(window=5).std()
data['StdDev_period10']=data['time'].rolling(window=10).std()
data['StdDev_period20']=data['time'].rolling(window=20).std()

