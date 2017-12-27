"""
NAME : Quandl exercise.
====================================
Description : To calculate rolling AVERAGE & STANDARD DEVIATION of the various columns
(e.g : close,wap,volume,etc) for all the stocks which is given.
================================================================================================
Input : A csv file of stock list,containing  quandl code with company name 
=======================================================================================
Output : A csv file containing stock code, company name & calculating values
========================================================================================
"""
import quandl
import pandas as pd
def assignment():
  
    data = pd.read_csv('/home/pallabeedey/Downloads/stock_list.csv')
    api_key = "gLV6zRzBa9NxirTyEoQc"
    Calculated_col= []
    for i,j in zip(data['Quandl_Code'], data['Company_Name']):    
        data1 = quandl.get(i, authtoken = api_key, start_date = '2017-11-10')
        data1[['close_Rolling_avg' ,'WAP_Rolling_avg', 'Vol_Rolling_avg']] = data1[['Close', 'WAP', 'No. of Shares']].rolling(window = 22).mean() 
        data1[['close_Rolling_StdDev','WAP_Rolling_StdDev' ,'Vol_Rolling_StdDev']] = data1[['Close', 'WAP', 'No. of Shares']].rolling(window = 22).std()
        m = i, j, (data1['close_Rolling_avg'][-1]), (data1['WAP_Rolling_avg'][-1]), (data1['Vol_Rolling_avg'][-1]), (data1['close_Rolling_StdDev'][-1]), (data1['WAP_Rolling_StdDev'][-1]), (data1['Vol_Rolling_StdDev'][-1])
        Calculated_col.append(m)
        Keys = ['Quandl_Code', 'Company_Name', 'close_Rolling_avg' ,'WAP_Rolling_avg', 'Vol_Rolling_avg', 'close_Rolling_StdDev','WAP_Rolling_StdDev' ,'Vol_Rolling_StdDev']
        df = pd.DataFrame.from_records(Calculated_col, columns = Keys)
        df.to_csv('Output_test1.csv')
    return df
assignment()
