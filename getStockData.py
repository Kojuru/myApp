import pandas_datareader as pdr
import datetime
import mysql.connector
import datetime


def get_stock_data():
    '''

    :return:
    '''

    stock_data = pdr.get_data_yahoo('AAPL',
                                    start=datetime.datetime(2020, 1, 1),
                                    end=datetime.datetime(2020, 2, 1))

    return stock_data

mydb = mysql.connector.connect(
    host="127.0.0.1	",
    port="3306",
    user="root",
    passwd="root",
    auth_plugin='mysql_native_password',
    database="stock_data"
)

mycursor = mydb.cursor()

stock = get_stock_data()

#mycursor.execute("DROP TABLE stocklist")
#mydb.commit()
#mycursor.execute("CREATE TABLE stocklist (date TIMESTAMP, high FLOAT, low FLOAT, open FLOAT, close FLOAT, volume DOUBLE, ajdclose FLOAT)")

mycursor.execute("ALTER TABLE stocklist MODIFY date DATE")

mycursor.execute("DESCRIBE stocklist")
for x in mycursor:
    print(x)

#stock.to_sql("stocklist", con=)

for row in stock.itertuples():
    print(row)
    mycursor.execute(
        "INSERT INTO stocklist (date, high, low, open, close, volume,ajdclose) VALUES (%s,%s,%s,%s,%s,%s,%s)",
        row
    )

mydb.commit()

mycursor.execute("SHOW stocklist")
for x in mycursor:
    print(x)

