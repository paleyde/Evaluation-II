data4=pd.read_csv('/home/pallabeedey/Downloads/anom_order.out',sep='_',header=None,names=['ed','-','ETH','source','anom','date'])
data4['date']=data4['date'].str.replace('.csv', '')
data4=data4[['source','date']]
data4['date']=pd.to_datetime(data4['date'], unit='ns')
data4
