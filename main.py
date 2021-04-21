import getStockData as gsd
import insertDB as db
import pandas_datareader as pdr
import datetime
import mysql.connector
import datetime
from sqlalchemy.sql import select
import click
from sqlalchemy import create_engine, MetaData, Table
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import datetime
from sys import argv
from flask import Flask, jsonify
import flaskRest

### Connection to local DB
engine = create_engine('mysql+mysqlconnector://root:root@127.0.0.1/stock_data')

@click.command(context_settings={"ignore_unknown_options": True})
@click.argument('start', nargs=1)
@click.argument('end', nargs=1)
@click.argument('stock', nargs=1)

def download(start, end, stock):

    click.echo("Hello")

    ### great stock element
    stock = gsd.get_stock_data(stock, start, end)

    ### insert stocklist into DB
    stock.to_sql(name="stocklist2", con=engine, if_exists="append", index="True")


if __name__=="__main__":
    download


def serve():

    app = Flask(__name__)

    @app.route('/mean', methods=['GET'])
    def get_mean():
        ### Idee: Alle Means werden in eine Liste appended. String formation ggf. in Select Abfrage reinpacken um ggf. curl Arguments abzufangen.
        ### "Spezifische Means müssen über einen POST Request gehandlet werden

        ### Select means from the DB
        result = engine.execute("SELECT AVG(High), AVG(LOW), AVG(Open), AVG(Close), AVG(Volume) FROM stocklist2")

        mean = []

        for x in result:
            mean.append(x)

        return jsonify(
            {
                'High Mean': round(float(mean[0][0]),2),
                'Low Mean': round(float(mean[0][1]),2),
                'Open Mean': round(float(mean[0][2]),2),
                'Close Mean': round(float(mean[0][3]),2),
                'Volume Mean': round(float(mean[0][4]),2)
   #             'Adj Close Mean': str(mean[0][5])
            }
        )




    @app.route('/datapoints', methods=['GET'])
    def get_datapoints():

        result = engine.execute("SELECT COUNT(High) FROM stocklist2")

        for x in result:
            return jsonify(
                {'Number of data points': str(x[0])}
            )


    #Run Server
    app.run(debug=True)



if __name__=="__main__":
    serve