import pandas_datareader as pdr
import datetime

def get_stock_data():

    stock_data = pdr.get_data_yahoo('AAPL',
                                    start=datetime.datetime(2020, 1, 1),
                                    end=datetime.datetime(2020, 2, 1))

    return stock_data


appl = get_stock_data()

print(appl)

