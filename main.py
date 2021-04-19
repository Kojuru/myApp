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
    stock.to_sql(name="stocklist2", con=engine, if_exists="replace", index="True", index_label="ID")

    result = engine.execute("SELECT AVG(High) FROM stocklist2")

    for x in result:
         click.echo(x[0])

if __name__=="__main__":
    download


def serve():

    app = Flask(__name__)

    @app.route('/mean', methods=['GET'])
    def get_mean():
        result = engine.execute("SELECT AVG(High) FROM stocklist2")

        for x in result:
            return jsonify(
                {'mean': str(x[0])}
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