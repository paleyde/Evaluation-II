import pandas as pd
data4=pd.read_csv('/home/pallabeedey/Downloads/anom_order.out',sep='_',header=None,names=['ed','-','ETH','coin','anom','date'])
data4['date']=data4['date'].str.replace('.csv', '')
data4=data4[['coin','date']]
data4['date']=pd.to_datetime(data4['date'], unit='ns')
data4_unique_source=pd.DataFrame(data4.coin.value_counts())
data4_unique_source=data4_unique_source.rename(columns={'coin':'No._of_unique_coin'})
data4_unique_source.to_csv("data4_unique_coin.csv")
data4['new_date'] = [d.date() for d in data4['date']] 
data4['new_time'] = [d.time() for d in data4['date']]
data4_unique_date =pd.DataFrame(data4.new_date.value_counts())
data4_unique_date=data4_unique_date.rename(columns={'new_date':'No._of_unique_date'})
data4_unique_date.to_csv("data4_unique_date.csv")
