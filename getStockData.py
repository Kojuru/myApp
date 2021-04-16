import pandas_datareader as pdr
import datetime
import mysql.connector
import datetime
from sqlalchemy import create_engine


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

engine = create_engine('mysql+mysqlconnector://root:root@127.0.0.1/stock_data')

mycursor = mydb.cursor()

stock = get_stock_data()

#mycursor.execute("DROP TABLE stocklist")
#mydb.commit()
#mycursor.execute("CREATE TABLE stocklist (date TIMESTAMP, high FLOAT, low FLOAT, open FLOAT, close FLOAT, volume DOUBLE, ajdclose FLOAT)")

#mycursor.execute("ALTER TABLE stocklist MODIFY date DATE")

#mycursor.execute("DESCRIBE stocklist")
#for x in mycursor:
#    print(x)

stock.to_sql(name="stocklist2", con=engine, if_exists="replace", index="True", index_label="ID")

mycursor.execute("SELECT * FROM stocklist2")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)






#mycursor.execute("SHOW stocklist")
#for x in mycursor:
#    print(x)

