from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy import select

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():

    engine = create_engine('mysql+mysqlconnector://root:root@127.0.0.1/stock_data')

    result = engine.execute("SELECT AVG(High) FROM stocklist2")

    for x in result:
        mean = x[0]

    return render_template('mean.html', mean=mean)