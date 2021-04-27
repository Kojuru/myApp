import pandas_datareader as pdr
import datetime



def get_stock_data(stock, start, end):
    '''
    IF falls Start > End ist. Dann nochmal neue Eingabe fordern vom User.
    If something doesnt work properly, return something
    When download is sucessful, return a message --> try/error
    :return:
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
        print("Es ist ein Fehler aufgetreten: "+ str(vE))

        return 1

    except Exception as ex:

        print("Es ist ein Fehler aufgetreten: " + str(ex))

        return 1









