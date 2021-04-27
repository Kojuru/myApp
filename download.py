import click
import getStockData as gsd
from sqlalchemy import create_engine
from sqlalchemy import inspect


engine = create_engine('mysql+mysqlconnector://root:root@127.0.0.1/stock_data')

@click.command(context_settings={"ignore_unknown_options": True})
#@click.argument('start', nargs=1)
#@click.argument('end', nargs=1)
#@click.argument('stock', nargs=1)
@click.option('--stock', prompt="Stock listing name", help="Stock you want to download")
@click.option("--start", prompt="Start date YYYY-mm-dd", help="Start date you want download stock data")
@click.option("--end", prompt="End date YYYY-mm-dd", help="End date you want download stock data")


### Start Download from command line of a given stock in a given time period. Date must be in Format "YYYY-mm-dd". Helper function need to be implemented.
def download(start, end, stock):
    '''This script starts download '''

    try:
        click.echo("Download is started!")

        ### creat stock element as pandas DataFrame object
        stock = gsd.get_stock_data(stock, start, end)


        click.echo("Download was successful!")

        ### If table does not exist, create a new one
        insp = inspect(engine)

        if not "stocklist" in insp.get_table_names():
            stock.to_sql(name="stocklist", con=engine, index="Date")
            click.echo("New table 'stocklist' was created")

        else:
            ### insert stocklist into DB and check for duplicates
            stock.to_sql(name="temptable", con=engine, if_exists="replace", index="Date")

            ### If duplicates exist, append only new values
            with engine.begin() as cn:
                sql = """INSERT INTO stocklist (Date, High, Low, Open, Close, Volume, AdjClose, Name)
                                SELECT t.Date, t.High, t.Low, t.Open, t.Close, t.Volume, t.AdjClose, t.Name
                                FROM temptable t
                                WHERE NOT EXISTS 
                                    (SELECT 1 FROM stocklist s
                                     WHERE t.Date = s.Date
                                     AND t.Name = s.Name)"""

                cn.execute(sql)

        ### TODO: if no new data was inserted than echo something else
        click.echo("Data was stored in the table")



    except Exception as ex:
        print("An error has occured: " + str(ex))

        #traceback.print_exc()





if __name__=="__main__":
    download