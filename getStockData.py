import pandas_datareader as pdr



def get_stock_data(stock, start, end):
    '''
    Gets data from a specific stock in a determined time period.
    :param stock: stock name (type: string)
    :param start: start date (type: string)
    :param end: end date (type: string)
    :return: Pandas DataFrame object
    '''

    ### try/except

    try:
        ### get stock data from yahooo
        stock_data = pdr.get_data_yahoo(stock,
                                        start=start,
                                        end=end
                                        )

        ### Deleting whitespace in column "Adj Close"
        stock_data = stock_data.rename(columns={stock_data.columns[5]: "AdjClose"})

        ### Add column "Name" to dataframe with stock name as values
        stock_data["Name"] = stock

        return stock_data

    except ValueError as vE:

        raise vE

    except Exception as ex:

        raise ex









