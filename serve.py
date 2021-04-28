import click
from sqlalchemy import create_engine
from flask import Flask, jsonify, request

'''
Ideas:
Stockname in route --> e.g. localhost../aapl/mean?="Volume"?
'''

### TODO: Try/Except

@click.command()
###starts webserver (local) from command line (command: serve).
def serve():
    '''
    This script starts the webserver
    API Request: curl -X GET -d "stockname" http://127.0.0.1:5000/ROUTE
    '''
    app = Flask(__name__)

    ### Connection to local DB
    engine = create_engine('mysql+mysqlconnector://root:root@127.0.0.1/stock_data')

    ### Returns mean of high, low, open, close, volume, adj close
    ### TODO: Verbesserung: zwei verschiedene GET-Request 1. done, 2. specified mean value e.g. High, Volume, etc.
    @app.route('/mean', methods=["GET"])
    def get_mean():

        '''### TODO: POST-Request --> specific Mean
        if request.method == "POST":
            target_column = request.get_data().decode("UTF-8")

            result = engine.execute(f"SELECT AVG({target_column}) FROM stocklist")
            mean_list = [x for x in result]

            ###TODO: not necessary
            mean = list(mean_list)

            return jsonify(
                {
                    f'{target_column} Mean': "$ " + str(round(float(mean[0][0]), 2)),
                }
            )'''

        target_column = str(request.get_data().decode("UTF-8"))

        ### Select means from the DB and creates an [object] --> Specify what object
        result = engine.execute(f"SELECT AVG(High), AVG(LOW), AVG(Open), AVG(Close), AVG(Volume), AVG(AdjClose) FROM stocklist WHERE Name='{target_column}'")

        ###Append result tuples to mean
        mean_list = [x for x in result]

        ### TODO: Ggf. mean object umwandeln? mean_list in dict umwandeln.
        return jsonify(
            {
                'High Mean': "$ " + str(round(float(mean_list[0][0]), 2)),
                'Low Mean': "$ " + str(round(float(mean_list[0][1]), 2)),
                'Open Mean': "$ " + str(round(float(mean_list[0][2]), 2)),
                'Close Mean': "$ " + str(round(float(mean_list[0][3]), 2)),
                'Volume Mean': "$ " + str(round(float(mean_list[0][4]), 2)),
                'Adj Close Mean': "$ " + str(round(float(mean_list[0][5]), 2))
            }
        )


    ###Get the number of datapoints
    @app.route('/datapoints', methods=['GET'])
    def get_datapoints():
        target_column = str(request.get_data().decode("UTF-8"))

        result = engine.execute(f"SELECT COUNT(High) FROM stocklist WHERE Name='{target_column}'")

        for x in result:
            return jsonify(
                {'Number of data points': str(x[0])}
            )

    ###Get the peak to peak amplitude
    ### TODO: Return highest/lowest Peak to Peak Amplitude for comparison
    ### TODO: Specify timeperiod
    @app.route('/peaktopeak', methods=['GET'])
    def get_peaktopeak():

        target_column = str(request.get_data().decode("UTF-8"))

        result = engine.execute(f"SELECT MAX(High), MIN(Low) FROM stocklist WHERE Name='{target_column}'")

        amplitude = [x for x in result]

        return jsonify(
            {
                'Peak to Peak Amplitude': "$ " + str(round((float(amplitude[0][0]) - float(amplitude[0][1])), 2))
            }
        )

    # Run Server
    app.run(debug=True)


if __name__ == "__main__":
    serve
