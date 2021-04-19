# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
#Imports:
#import sys
import requests
import json
import shutil
#import gzip
#import zipfile
import pandas as pd
#import numpy as np
#import io
import os
from datetime import datetime

#Set these parameters before running the code:
filePath = os.path.dirname(os.path.abspath(__file__))
print("Python file is in: " + filePath)
#filePath = "/Users/HX/Desktop/RefinitivData/"  #Location to save downloaded files
myUsername = "9019880"
myPassword = "ilovema5!"
useAws = True
days = 3
#Set the last parameter above to:
# - False to download from TRTH servers
# - True to download from Amazon Web Services cloud (recommended, it is faster)


bin_dict = {
    1: '00:00 to 00:10',
    2: '00:10 to 00:20',
    3: '00:20 to 00:30',
    4: '00:30 to 00:40',
    5: '00:40 to 00:50',
    6: '00:50 to 01:00',
    7: '01:00 to 01:10',
    8: '01:10 to 01:20',
    9: '01:20 to 01:30',
    10: '01:30 to 01:40',
    11: '01:40 to 01:50',
    12: '01:50 to 02:00',
    13: '02:00 to 02:10',
    14: '02:10 to 02:20',
    15: '02:20 to 02:30',
    16: '02:30 to 02:40',
    17: '02:40 to 02:50',
    18: '02:50 to 03:00',
    19: '03:00 to 03:10',
    20: '03:10 to 03:20',
    21: '03:20 to 03:30',
    22: '03:30 to 03:40',
    23: '03:40 to 03:50',
    24: '03:50 to 04:00',
    25: '04:00 to 04:10',
    26: '04:10 to 04:20',
    27: '04:20 to 04:30',
    28: '04:30 to 04:40',
    29: '04:40 to 04:50',
    30: '04:50 to 05:00',
    31: '05:00 to 05:10',
    32: '05:10 to 05:20',
    33: '05:20 to 05:30',
    34: '05:30 to 05:40',
    35: '05:40 to 05:50',
    36: '05:50 to 06:00',
    37: '06:00 to 06:10',
    38: '06:10 to 06:20',
    39: '06:20 to 06:30',
    40: '06:30 to 06:40',
    41: '06:40 to 06:50',
    42: '06:50 to 07:00',
    43: '07:00 to 07:10',
    44: '07:10 to 07:20',
    45: '07:20 to 07:30',
    46: '07:30 to 07:40',
    47: '07:40 to 07:50',
    48: '07:50 to 08:00',
    49: '08:00 to 08:10',
    50: '08:10 to 08:20',
    51: '08:20 to 08:30',
    52: '08:30 to 08:40',
    53: '08:40 to 08:50',
    54: '08:50 to 09:00',
    55: '09:00 to 09:10',
    56: '09:10 to 09:20',
    57: '09:20 to 09:30',
    58: '09:30 to 09:40',
    59: '09:40 to 09:50',
    60: '09:50 to 10:00',
    61: '10:00 to 10:10',
    62: '10:10 to 10:20',
    63: '10:20 to 10:30',
    64: '10:30 to 10:40',
    65: '10:40 to 10:50',
    66: '10:50 to 11:00',
    67: '11:00 to 11:10',
    68: '11:10 to 11:20',
    69: '11:20 to 11:30',
    70: '11:30 to 11:40',
    71: '11:40 to 11:50',
    72: '11:50 to 12:00',
    73: '12:00 to 12:10',
    74: '12:10 to 12:20',
    75: '12:20 to 12:30',
    76: '12:30 to 12:40',
    77: '12:40 to 12:50',
    78: '12:50 to 13:00',
    79: '13:00 to 13:10',
    80: '13:10 to 13:20',
    81: '13:20 to 13:30',
    82: '13:30 to 13:40',
    83: '13:40 to 13:50',
    84: '13:50 to 14:00',
    85: '14:00 to 14:10',
    86: '14:10 to 14:20',
    87: '14:20 to 14:30',
    88: '14:30 to 14:40',
    89: '14:40 to 14:50',
    90: '14:50 to 15:00',
    91: '15:00 to 15:10',
    92: '15:10 to 15:20',
    93: '15:20 to 15:30',
    94: '15:30 to 15:40',
    95: '15:40 to 15:50',
    96: '15:50 to 16:00',
    97: '16:00 to 16:10',
    98: '16:10 to 16:20',
    99: '16:20 to 16:30',
    100: '16:30 to 16:40',
    101: '16:40 to 16:50',
    102: '16:50 to 17:00',
    103: '17:00 to 17:10',
    104: '17:10 to 17:20',
    105: '17:20 to 17:30',
    106: '17:30 to 17:40',
    107: '17:40 to 17:50',
    108: '17:50 to 18:00',
    109: '18:00 to 18:10',
    110: '18:10 to 18:20',
    111: '18:20 to 18:30',
    112: '18:30 to 18:40',
    113: '18:40 to 18:50',
    114: '18:50 to 19:00',
    115: '19:00 to 19:10',
    116: '19:10 to 19:20',
    117: '19:20 to 19:30',
    118: '19:30 to 19:40',
    119: '19:40 to 19:50',
    120: '19:50 to 20:00',
    121: '20:00 to 20:10',
    122: '20:10 to 20:20',
    123: '20:20 to 20:30',
    124: '20:30 to 20:40',
    125: '20:40 to 20:50',
    126: '20:50 to 21:00',
    127: '21:00 to 21:10',
    128: '21:10 to 21:20',
    129: '21:20 to 21:30',
    130: '21:30 to 21:40',
    131: '21:40 to 21:50',
    132: '21:50 to 22:00',
    133: '22:00 to 22:10',
    134: '22:10 to 22:20',
    135: '22:20 to 22:30',
    136: '22:30 to 22:40',
    137: '22:40 to 22:50',
    138: '22:50 to 23:00',
    139: '23:00 to 23:10',
    140: '23:10 to 23:20',
    141: '23:20 to 23:30',
    142: '23:30 to 23:40',
    143: '23:40 to 23:50',
    144: '23:50 to 00:00'
}

get_bin_dict = lambda x: bin_dict.get(x)

################## Step 1: token request ##############################

requestUrl = "https://hosted.datascopeapi.reuters.com/RestApi/v1/Authentication/RequestToken"

requestHeaders={
    "Prefer":"respond-async",
    "Content-Type":"application/json"
    }

requestBody={
    "Credentials": {
    "Username": myUsername,
    "Password": myPassword
  }
}

r1 = requests.post(requestUrl, json=requestBody,headers=requestHeaders)

if r1.status_code == 200 :
    jsonResponse = json.loads(r1.text.encode('ascii', 'ignore'))
    token = jsonResponse["value"]
    print ('Authentication token (valid 24 hours):')
    print (token)
else:
    print ('Invalid credentials')

header2 = {'Content-Type': 'application/json', 'Authorization': 'Token ' + token }
header3 = {'Content-Type': 'application/json', 'Authorization': 'Token ' + token, 'Prefer': 'respond-async'}

########### Step 2: send an on demand extraction request of file names using the received token ########## 

EndPointURL='https://hosted.datascopeapi.reuters.com/RestApi/v1/StandardExtractions/PackageDeliveries'

tokenRequestBody = json.dumps({'Credentials':{'Password':myPassword,'Username':myUsername}})

header = header2
response = requests.post(EndPointURL, tokenRequestBody, headers=header)
response = requests.get(EndPointURL, headers=header)
df = pd.DataFrame(response.json()['value'])
# df.to_csv(filePath + 'subscriptions.csv')

#################### Step 3: Filtering for order book data file "NORMALIZEDLL2" #################### 

ob_name_df = df[df.Name.str.contains('FXD5') & df.Name.str.contains('NORMALIZEDLL2-Data')] \
             .sort_values(by=['Name'], ascending=False) \
             .reset_index(drop=True)
#alldaysspreads_df = pd.DataFrame()

#################### Step 4: Filtering for transaction data file "NORMALIZEDMP" ####################
             
trans_name_df = df[df.Name.str.contains('FXD5-2') & df.Name.str.contains('NORMALIZEDMP-Data')] \
                .sort_values(by=['Name'], ascending=False) \
                .reset_index(drop=True)

#dates = volumes_df['Name'].tolist()[-1][5:15] + " to " + vol#umes_df['Name'].tolist()[0][5:15]
#alldaysvolumes_df = pd.DataFrame()

################### Step 5: Compile new order book data ###########################

print(filePath + "\\orderbook.csv.gz")
try:
    #temp_df = pd.read_csv("/Users/HX/Desktop/RefinitivData/orderbook.csv.gz")
    temp_df =  pd.read_csv(filePath + "\\orderbook.csv.gz")
    temp_df = pd.to_datetime(temp_df['Date-Time'])
    date_df = pd.DataFrame(temp_df.dt.date.astype(str).unique())
    ob_exist = True
except:
    print("No existing file detected for order book data!")
    date_df = pd.DataFrame()
    ob_exist = False
    
ob_df = pd.DataFrame()
col_name_ob = ['#RIC', 'Domain', 'Date-Time', 'GMT Offset', 'Type',
               'L1-BidPrice', 'L1-BidSize', 'L1-BuyNo', 'L1-AskPrice', 'L1-AskSize', 'L1-SellNo', 
               'L2-BidPrice', 'L2-BidSize', 'L2-BuyNo', 'L2-AskPrice', 'L2-AskSize', 'L2-SellNo', 
               'L3-BidPrice', 'L3-BidSize', 'L3-BuyNo', 'L3-AskPrice', 'L3-AskSize', 'L3-SellNo', 
               'L4-BidPrice', 'L4-BidSize', 'L4-BuyNo', 'L4-AskPrice', 'L4-AskSize', 'L4-SellNo', 
               'L5-BidPrice', 'L5-BidSize', 'L5-BuyNo', 'L5-AskPrice', 'L5-AskSize', 'L5-SellNo']
                
for _, row in ob_name_df.iterrows():
    date = datetime.strptime(row.Name[5:15], '%Y-%m-%d').strftime('%Y-%m-%d')
    if not date_df.empty:
        if date in date_df.values:
            continue
    print('Extracting order book data on ' + date)
    
    file_url = EndPointURL + "('" + row.PackageDeliveryId + "')" + '/$value'
    #AWS requires an additional header: X-Direct-Download
    if useAws:
        requestHeaders={
            "Prefer":"respond-async",
            "Content-Type":"text/plain",
            "Accept-Encoding":"gzip",
            "X-Direct-Download":"true",
            "Authorization": "token " + token
        }
    else:
        requestHeaders={
            "Prefer":"respond-async",
            "Content-Type":"text/plain",
            "Accept-Encoding":"gzip",
            "Authorization": "token " + token
        }
    
    r5 = requests.get(file_url, headers = requestHeaders, stream = True)
    #Ensure we do not automatically decompress the data on the fly:
    r5.raw.decode_content = False
    
    #if useAws:
    #    print ('Content response headers (AWS server): type: ' + r5.headers["Content-Type"] + '\n')
    #    #AWS does not set header Content-Encoding="gzip".
    #else:
    #    print ('Content response headers (TRTH server): type: ' + r5.headers["Content-Type"] + ' - encoding: ' + r5.headers["Content-Encoding"] + '\n')   
    
    fileName = filePath + "\\newfile.csv.gz"
    rr = r5.raw
    # open(fileName,"w")
    with open(fileName, 'wb') as fd:
        shutil.copyfileobj(rr, fd, 1024)
    fd.close
   
    daily_df = pd.read_csv(fileName, header = 0)
    daily_df = daily_df[daily_df['#RIC'] == 'SGD=D3D'][col_name_ob]
    ob_df = ob_df.append(daily_df, ignore_index=True)

################### Step 6: Compile new transaction data ###########################

try:
    #temp_df = pd.read_csv("/Users/HX/Desktop/RefinitivData/transaction.csv.gz")
    temp_df =  pd.read_csv(filePath + "\\transaction.csv.gz")
    temp_df = pd.to_datetime(temp_df['Date-Time'])
    date_df = pd.DataFrame(temp_df.dt.date.astype(str).unique())
    trans_exist = True
except:
    print("No existing file detected for transaction data!")
    date_df = pd.DataFrame()
    trans_exist = False
    
trans_df = pd.DataFrame()
col_name_trans = ['#RIC', 'Domain', 'Date-Time', 'GMT Offset', 'Type', 'Bid Price',
                  'Price', 'Volume', 'Bid Size', 'Ask Price', 'Ask Size',
                  'Qualifiers', 'Exch Time']

for _, row in trans_name_df.iterrows():
    date = datetime.strptime(row.Name[5:15], '%Y-%m-%d').strftime('%Y-%m-%d')
    if not date_df.empty:
        if date in date_df.values:
            continue
    print('Extracting transaction data on ' + date)
    
    file_url = EndPointURL + "('" + row.PackageDeliveryId + "')" + '/$value'
    #AWS requires an additional header: X-Direct-Download
    if useAws:
        requestHeaders={
            "Prefer":"respond-async",
            "Content-Type":"text/plain",
            "Accept-Encoding":"gzip",
            "X-Direct-Download":"true",
            "Authorization": "token " + token
        }
    else:
        requestHeaders={
            "Prefer":"respond-async",
            "Content-Type":"text/plain",
            "Accept-Encoding":"gzip",
            "Authorization": "token " + token
        }
    
    r5 = requests.get(file_url,headers=requestHeaders,stream=True)
    #Ensure we do not automatically decompress the data on the fly:
    r5.raw.decode_content = False
    
    #if useAws:
    #    print ('Content response headers (AWS server): type: ' + r5.headers["Content-Type"] + '\n')
        #AWS does not set header Content-Encoding="gzip".
    #else:
    #    print ('Content response headers (TRTH server): type: ' + r5.headers["Content-Type"] + ' - encoding: ' + r5.headers["Content-Encoding"] + '\n')   
    
    fileName = filePath + "\\newfile.csv.gz"
    rr = r5.raw
    #open(fileName,"w")
    with open(fileName, 'wb') as fd:
        shutil.copyfileobj(rr, fd, 1024)
    fd.close
    
    daily_df = pd.read_csv(fileName, header = 0)
    daily_df = daily_df[daily_df['#RIC'] == 'SGD=D5'][col_name_trans]
    trans_df = trans_df.append(daily_df, ignore_index=True)

    os.remove(fileName)     

############## Step X: Append new data to existing files ##############################
if not ob_df.empty:
    ob_df['Date-Time'] = pd.to_datetime(ob_df['Date-Time'])
    ob_df = ob_df.sort_values(by = ['Date-Time'])
    ob_consol_name = filePath + "\\orderbook.csv.gz"
    if ob_exist:
        ob_df.to_csv(ob_consol_name, compression = 'gzip', mode = 'a', header = False, index = False)
    else:
        ob_df.to_csv(ob_consol_name, compression = 'gzip', header = True, index = False)
        
if not ob_df.empty:
    trans_df['Date-Time'] = pd.to_datetime(trans_df['Date-Time'])
    trans_df = trans_df.sort_values(by = ['Date-Time'])
    trans_consol_name = filePath + "\\transaction.csv.gz"
    if trans_exist:
        trans_df.to_csv(trans_consol_name, compression = 'gzip', mode = 'a', header = False, index = False)
    else:
        trans_df.to_csv(trans_consol_name, compression = 'gzip', header = True, index = False)