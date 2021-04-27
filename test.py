from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root:root@127.0.0.1/stock_data')

a = "High"

result = engine.execute(f"SELECT MIN({a}) FROM stocklist")

for x in result:
    print(x[0][0])



from setuptools import setup

setup(
    name="stockTimeseries",
    version="1.0",
    py_modules="main",
    install_requieres=[
        "Click",
    ],
    entry_points='''
        [console_scripts]
        download=main:download
        serve=main:serve
        start=main:start
    '''
)