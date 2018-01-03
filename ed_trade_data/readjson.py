import json
import pandas as pd
from pprint import pprint
import numpy as np
fp = open('/home/pallabeedey/Downloads/ed_trade_data.json') 

data = json.load(fp)
kys =data.keys()

for i in range(0,275):
    key=np.repeat([kys[i]],len(data[kys[i]]))
    k=pd.DataFrame(data[kys[i]],index=key)
    k['amount']=pd.to_numeric(k['amount'])
    kys[i]=k[np.abs(k.amount-k.amount.mean())>(3*k.amount.std())]



