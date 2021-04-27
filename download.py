import click
import getStockData as gsd
from sqlalchemy import create_engine

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
    click.echo("Download is started.")

    '''print(type(end))
    print(end)

    end = datetime.datetime.strptime(end, "%Y-%m-%d")
    start = datetime.datetime.strptime(start, "%Y-%m-%d")

    print(type(end))

    if end > start:
        print("Bin hier")
        start, end = end, start

    print(end)'''

    ### creat stock element as pandas DataFrame object
    stock = gsd.get_stock_data(stock, start, end)

    ### if error occurs, stop download function --> doesnt work atm
    if stock==1:
        return

    click.echo("Download was successful")

    ### insert stocklist into DB
    stock.to_sql(name="stocklist", con=engine, if_exists="replace", index="Date")



if __name__=="__main__":
    download