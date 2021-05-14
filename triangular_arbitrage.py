# -*- coding: utf-8 -*-
"""
Created on Thu May  6 23:06:31 2021

@author: ali_k
"""

import time
import datetime as dt
from requests_futures.sessions import FuturesSession

session = FuturesSession()

threshold = 1.02

exchange1AssetName = 'TRX_USDT'
exchange2AssetName = 'TRX_BTC'
exchange3AssetName = 'BTC_USDT'

exchange4AssetName = 'XRP_USDT'
exchange5AssetName = 'XRP_BTC'

exchange6AssetName = 'ADA_USDT'
exchange7AssetName = 'ADA_BTC'

exchange8AssetName = 'UNI_USDT'
exchange9AssetName = 'UNI_BTC'


uri1 = "https://api.btcturk.com/api/v2/ticker?pairSymbol=" + exchange1AssetName
uri2 = "https://api.btcturk.com/api/v2/ticker?pairSymbol=" + exchange2AssetName
uri3 = "https://api.btcturk.com/api/v2/ticker?pairSymbol=" + exchange3AssetName

uri4 = "https://api.btcturk.com/api/v2/ticker?pairSymbol=" + exchange4AssetName
uri5 = "https://api.btcturk.com/api/v2/ticker?pairSymbol=" + exchange5AssetName
uri6 = "https://api.btcturk.com/api/v2/ticker?pairSymbol=" + exchange6AssetName
uri7 = "https://api.btcturk.com/api/v2/ticker?pairSymbol=" + exchange7AssetName

uri8 = "https://api.btcturk.com/api/v2/ticker?pairSymbol=" + exchange8AssetName
uri9 = "https://api.btcturk.com/api/v2/ticker?pairSymbol=" + exchange9AssetName


while True:
    req1 = session.get(url=uri1)
    req2 = session.get(url=uri2)
    req3 = session.get(url=uri3)
    
    req4 = session.get(url=uri4)
    req5 = session.get(url=uri5)
    req6 = session.get(url=uri6)
    req7 = session.get(url=uri7)
    
    req8 = session.get(url=uri8)
    req9 = session.get(url=uri9)
    
    result1 = req1.result().json()["data"][0]
    result1bid = result1["bid"]
    result1ask = result1["ask"]
    
    result2 = req2.result().json()["data"][0]
    result2bid = 1 / result2["bid"]
    result2ask = 1 / result2["ask"]
    
    result3 = req3.result().json()["data"][0]
    result3bid = 1 / result3["bid"]
    result3ask = 1 / result3["ask"]
    
    result4 = req4.result().json()["data"][0]
    result4bid = result4["bid"]
    result4ask = result4["ask"]
    
    result5 = req5.result().json()["data"][0]
    result5bid = 1 / result5["bid"]
    result5ask = 1 / result5["ask"]
    
    result6 = req6.result().json()["data"][0]
    result6bid = result6["bid"]
    result6ask = result6["ask"]
    
    result7 = req7.result().json()["data"][0]
    result7bid = 1 / result7["bid"]
    result7ask = 1 / result7["ask"]
    
    result8 = req8.result().json()["data"][0]
    result8bid = result8["bid"]
    result8ask = result8["ask"]
    
    result9 = req9.result().json()["data"][0]
    result9bid = 1 / result9["bid"]
    result9ask = 1 / result9["ask"]
    
    printed = False
    
    if result1ask*result2bid*result3bid > threshold:
        print('TRX Diff: ' + str(result1ask*result2bid*result3bid))
        printed = True
        
    if result4ask*result5bid*result3bid > threshold:
        print('XRP Diff: ' + str(result4ask*result5bid*result3bid))
        printed = True
        
    if result6ask*result7bid*result3bid > threshold:
        print('ADA Diff: ' + str(result6ask*result7bid*result3bid))
        printed = True
        
    if result8ask*result9bid*result3bid > threshold:
        print('UNI Diff: ' + str(result8ask*result9bid*result3bid))
        printed = True
    
    
    if printed:
        currentTime = dt.datetime.now().strftime('%H:%M:%S.%f')
        print(currentTime)
    
    
    time.sleep(2)




