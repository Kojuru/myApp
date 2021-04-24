import getStockData as gsd
import click
from sqlalchemy import create_engine
from flask import Flask, jsonify

'''
Ideas:
- Create maybe a test-class for testing my API?
- return currency ($)

'''

### Connection to local DB
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
    click.echo("Download ist gestartet.")

    ### creat stock element as pandas DataFrame object
    stock = gsd.get_stock_data(stock, start, end)

    #click.echo(type(stock))

    ### insert stocklist into DB
    ### To DO: change db name
    stock.to_sql(name="stocklist2", con=engine, if_exists="replace", index="True")


if __name__=="__main__":
    download

###starts webserver (local) from command line (command: serve). Ggf. hier noch Click Argument?
def serve():
    '''This script starts the webserver'''
    app = Flask(__name__)

    ### Returns mean of high, low, open, close, volume, adj close
    @app.route('/mean', methods=['GET'])
    def get_mean():
        ### Idee: Alle Means werden in eine Liste appended. String formation ggf. in Select Abfrage reinpacken um ggf. curl Arguments abzufangen.
        ### "Spezifische Means müssen über einen POST Request gehandlet werden

        ### Select means from the DB and creates an [object] --> Specify what object
        result = engine.execute("SELECT AVG(High), AVG(LOW), AVG(Open), AVG(Close), AVG(Volume), AVG('Adj Close') FROM stocklist2")

        ###Append result tuples to mean
        mean_list = (x for x in result)

        ###TO DO: not necessary
        mean = list(mean_list)

        ### TO DO: Ggf. mean object umwandeln?
        return jsonify(
            {
                'High Mean': round(float(mean[0][0]),2),
                'Low Mean': round(float(mean[0][1]),2),
                'Open Mean': round(float(mean[0][2]),2),
                'Close Mean': round(float(mean[0][3]),2),
                'Volume Mean': round(float(mean[0][4]),2),
                'Adj Close Mean': str(mean[0][5])
            }
        )



    ###Get the number of datapoints
    @app.route('/datapoints', methods=['GET'])
    def get_datapoints():

        result = engine.execute("SELECT COUNT(High) FROM stocklist2")

        for x in result:
            return jsonify(
                {'Number of data points': str(x[0])}
            )

    ###Get the peak to peak amplitude
    @app.route('/peaktopeak', methods=['GET'])
    def get_peaktopeak():

        result = engine.execute("SELECT MAX(High), MIN(Low) FROM stocklist2")

        amplitude = []

        for x in result:
            amplitude.append(x)

        return jsonify(
            {
                'Peak to Peak Amplitude': round((float(amplitude[0][0])-float(amplitude[0][1])),2)
             }
        )


    #Run Server
    app.run(debug=True)



if __name__=="__main__":
    serve