import pandas as pd
bitcoin = pd.read_csv('/home/pallabeedey/Downloads/bitcoin-cross.csv',sep='|')
bitcoin=bitcoin.rename(columns={'Volume (24h)':'Volume (24h)(in $)','Price':'Price(in $)','Volume (%)':'Volume (in %)'})
bitcoin['Volume (24h)(in $)']=bitcoin['Volume (24h)(in $)'].str.replace(',', '').map(lambda x: x.lstrip('*'))
bitcoin['Volume (24h)(in $)'] = bitcoin['Volume (24h)(in $)'].str.replace('$', '')
bitcoin['Price(in $)']=bitcoin['Price(in $)'].map(lambda x: x.lstrip('*'))
bitcoin['Price(in $)'] = bitcoin['Price(in $)'].str.replace('$', '')
bitcoin['Volume (in %)'] = bitcoin['Volume (in %)'].str.replace('%', '')
bitcoin['Volume (24h)(in $)']=pd.to_numeric(bitcoin['Volume (24h)(in $)'])
bitcoin['Price(in $)']=pd.to_numeric(bitcoin['Price(in $)']) 
bitcoin['Volume (in %)']=pd.to_numeric(bitcoin['Volume (in %)'])
a=bitcoin.groupby('Source').agg({'Pair':"nunique",'Volume (24h)(in $)':"sum"})
a1=a.sort_values(by='Pair', ascending=0)
a1=a.rename(columns={'Pairs':'No.Of Pairs'})
a2=a.sort_values(by='Volume (24h)(in $)', ascending=0)
Ans1=a1.iloc[0:20,:]
Ans12=a2.iloc[0:20,:]
Ans1.to_html('top_20_largest_exchange_by_no_of_traded_pairs.html')
Ans12.to_html('top_20_largest_exchange_by_turnover.html')
b=bitcoin.groupby('Pair').agg({'Source':"nunique",'Volume (24h)(in $)':"sum"})
b1=b.sort_values(by='Source', ascending=0)
b1=b.rename(columns={'Source':'No.Of Sources'})
b12=b.sort_values(by='Volume (24h)(in $)', ascending=0)
Ans2=b1.iloc[0:20,:]
Ans21=b12.iloc[0:20,:]
Ans2.to_html('top_25_most_traded_pairs_no_of_traded_pairs.html')
Ans21.to_html('top_25_most_traded_pairs_by_turnover.html')
c=bitcoin.groupby('Pair').agg({'Price(in $)':"mean"})
c1=c.sort_values(by='Price(in $)', ascending=1)
Ans3=c1.iloc[0:10,:]
Ans3.to_html('top_10_cheapest_pairs.html')
