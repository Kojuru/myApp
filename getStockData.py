import pandas_datareader as pdr
import datetime
import mysql.connector
from sqlalchemy.sql import select
from sqlalchemy import create_engine, MetaData, Table


def get_stock_data(stock, start, end):
    '''
    IF falls Start > End ist. Dann nochmal neue Eingabe fordern vom User.
    If something doesnt work properly, return something
    When download is sucessful, return a message --> try/error
    :return:
    '''

    stock_data = pdr.get_data_yahoo(stock,
                                    start=start,
                                    end=end
                                    )

    return stock_data



