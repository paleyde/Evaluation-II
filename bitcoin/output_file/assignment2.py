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
a111=a.sort_values(by='Pair', ascending=0)
a112=a.sort_values(by='Pair', ascending=1)
a121=a.sort_values(by='Volume (24h)(in $)', ascending=0)
a122=a.sort_values(by='Volume (24h)(in $)', ascending=1)
Ans111=a111.iloc[0:20,:]
Ans112=a112.iloc[0:20,:]
Ans121=a121.iloc[0:20,:]
Ans122=a122.iloc[0:20,:]
Ans111.to_html('top_20_largest_exchange_by_no_of_traded_pairs.html')
Ans121.to_html('top_20_largest_exchange_by_turnover.html')
Ans112.to_html('top_20_smallest_exchange_by_no_of_traded_pairs.html')
Ans122.to_html('top_20_smallest_exchange_by_turnover.html')
b=bitcoin.groupby('Pair').agg({'Source':"nunique",'Volume (24h)(in $)':"sum"})
b111=b.sort_values(by='Source', ascending=0)
b112=b.sort_values(by='Source', ascending=1)
b121=b.sort_values(by='Volume (24h)(in $)', ascending=0)
b122=b.sort_values(by='Volume (24h)(in $)', ascending=1)
Ans211=b111.iloc[0:20,:]
Ans212=b112.iloc[0:20,:]
Ans221=b121.iloc[0:20,:]
Ans222=b122.iloc[0:20,:]
Ans211.to_html('top_25_most_traded_pairs_by_no_of_exchanges.html')
Ans212.to_html('top_25_least_traded_pairs_by_no_of_exchanges.html')
Ans221.to_html('top_25_most_traded_pairs_by_turnover.html')
Ans222.to_html('top_25_least_traded_pairs_by_turnover.html')
c=bitcoin.groupby('Pair').agg({'Price(in $)':"mean"})
c1=c.sort_values(by='Price(in $)', ascending=1)
c2=c.sort_values(by='Price(in $)', ascending=0)
Ans31=c1.iloc[0:10,:]
Ans32=c2.iloc[0:10,:]
Ans31.to_html('top_10_cheapest_pairs.html')
Ans32.to_html('top_10_expensive_pairs.html')
