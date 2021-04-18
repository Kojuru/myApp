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

@click.command(context_settings={"ignore_unknown_options": True})
@click.argument('start', nargs=1)
@click.argument('end', nargs=1)
@click.argument('stock', nargs=1)

def download(start, end, stock):
    ### Connection to local DB
    engine = create_engine('mysql+mysqlconnector://root:root@127.0.0.1/stock_data')

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

    hostName = "localhost"
    serverPort = 8080

    class MyServer(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
            self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))

    if __name__ == "__main__":
        webServer = HTTPServer((hostName, serverPort), MyServer)
        print("Server started http://%s:%s" % (hostName, serverPort))

        try:
            webServer.serve_forever()
        except KeyboardInterrupt:
            pass

        webServer.server_close()
        print("Server stopped.")

if __name__=="__main__":
    serve