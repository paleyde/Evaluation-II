import pandas as pd
bitcoin = pd.read_csv('/home/pallabeedey/Downloads/bitcoin-cross.csv',sep='|')
bitcoin=bitcoin.rename(columns={'Volume (24h)':'Volume (24h)(in $)','Price':'Price(in $)','Volume (%)':'Volume (in %)'})
bitcoin['Volume (24h)(in $)']=bitcoin['Volume (24h)(in $)'].str.replace(',', '').map(lambda x: x.lstrip('*'))
bitcoin['Volume (24h)(in $)'] = bitcoin['Volume (24h)(in $)'].str.replace('$', '')
bitcoin['Price(in $)']=bitcoin['Price(in $)'].str.replace('.', '').map(lambda x: x.lstrip('*'))
bitcoin['Price(in $)'] = bitcoin['Price(in $)'].str.replace('$', '')
bitcoin['Volume (in %)'] = bitcoin['Volume (in %)'].str.replace('%', '')
bitcoin['Volume (24h)(in $)']=pd.to_numeric(bitcoin['Volume (24h)(in $)'])
bitcoin['Price(in $)']=pd.to_numeric(bitcoin['Price(in $)']) 
bitcoin['Volume (in %)']=pd.to_numeric(bitcoin['Volume (in %)'])
bitcoin['traded_quantity']=bitcoin['Volume (24h)(in $)']/bitcoin['Price(in $)']
a=bitcoin.groupby('Source').agg({'Volume (in %)':"sum"})
a1=a.sort_values(by='Volume (in %)', ascending=0)
Ans1=a1.iloc[1:20,:]
Ans1.to_csv('top_20_largest_exchange.csv')
b=bitcoin.groupby('Pair').agg({'traded_quantity':"mean"})
b1=b.sort_values(by='traded_quantity', ascending=0)
Ans2=b1.iloc[1:25,:]
Ans2.to_csv('top_25_most_traded_pairs.csv')
c=bitcoin.groupby('Pair').agg({'Price(in $)':"mean"})
c1=c.sort_values(by='Price(in $)', ascending=1)
Ans3=c1.iloc[1:10,:]
Ans3.to_csv('top_10_cheapest_pairs.csv')

