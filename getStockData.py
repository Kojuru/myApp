import pandas_datareader as pdr



def get_stock_data(stock, start, end):
    '''
    IF falls Start > End ist. Dann nochmal neue Eingabe fordern vom User.
    If something doesnt work properly, return something
    When download is sucessful, return a message --> try/error
    :return:
    '''

    ### get stock data from yahooo
    stock_data = pdr.get_data_yahoo(stock,
                                    start=start,
                                    end=end
                                    )

    return stock_data



