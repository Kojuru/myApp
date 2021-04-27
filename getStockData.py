import pandas_datareader as pdr



def get_stock_data(stock, start, end):
    '''
    Gets data from a specific stock in a determined time.
    :param stock: stock name (type: string)
    :param start: start date (type: string)
    :param end: end date (type: string)
    :return: Pandas DataFrame object
    '''

    try:
        ### get stock data from yahooo
        stock_data = pdr.get_data_yahoo(stock,
                                        start=start,
                                        end=end
                                        )

        ### Deleting whitespace in column "Adj Close"
        stock_data = stock_data.rename(columns={stock_data.columns[5]: "AdjClose"})

        return stock_data

    except ValueError as vE:
        print("An error has occurred: "+ str(vE))

        return 1

    except Exception as ex:

        print("An error has occured: " + str(ex))

        return 1









