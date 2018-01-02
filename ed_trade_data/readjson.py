import json
import pandas as pd
from pprint import pprint
fp = open('/home/pallabeedey/Downloads/ed_trade_data.json') 

data = json.load(fp)
kys =data.keys()
a=data['ETH_NTC']
#pprint(data)
#type(data)
for i in range(0,275):
    kys[i]=pd.DataFrame(data[kys[i]])



