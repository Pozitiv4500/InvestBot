import requests

import apimoex


def price_now(a):
    with requests.Session() as session:
        data = apimoex.get_market_candles(session,a.upper())
        max_date = '2013-12-19 00:00:00'
        max_data_slovar = 0
        for i in range(0, len(data)):
            if data[i]['begin'] > max_date:
                max_date = data[i]['begin']
                max_data_slovar = i
        
        if data == []:
            return 'Неверно введён тикер акции'
        else:
          c = str(data[max_data_slovar]['close'])
          return c



def STOCK_delta_price1(c):
    c = c.split()
    a = c[0]
    b = c[1]

    with requests.Session() as session:
            data = apimoex.get_market_candles(session, a.upper())
            max_date = '2013-12-19 00:00:00'
            max_data_slovar = 0
            for i in range(0, len(data)):
                if data[i]['begin'] > max_date:
                    max_date = data[i]['begin']
                    max_data_slovar = i
            if str(data[max_data_slovar]['close']) >= str(b):
                return True
def STOCK_delta_price2(c):
    c = c.split()
    a = c[0]
    b = c[1]

    with requests.Session() as session:
            data = apimoex.get_market_candles(session, a.upper())
            max_date = '2013-12-19 00:00:00'
            max_data_slovar = 0
            for i in range(0, len(data)):
                if data[i]['begin'] > max_date:
                    max_date = data[i]['begin']
                    max_data_slovar = i
            if str(data[max_data_slovar]['close']) <= str(b):
                return True
def DOXODNOST(c):
    c = c.split()
    a = c[0].upper()
    b = c[1]

    with requests.Session() as session:
            data = apimoex.get_market_candles(session, a)
            max_date = '2013-12-19 00:00:00'
            max_data_slovar = 0
            for i in range(0, len(data)):
                if data[i]['begin'] > max_date:
                    max_date = data[i]['begin']
                    max_data_slovar = i
            if str(data[max_data_slovar]['close']) <= str(b):
                return True
