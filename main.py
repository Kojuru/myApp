import click
from sqlalchemy import create_engine
from download import download
from serve import serve

'''
Ideas:
- Create maybe a test-class for testing my API?
- return currency ($)

'''

### Connection to local DB
engine = create_engine('mysql+mysqlconnector://root:root@127.0.0.1/stock_data')

@click.group()
def start():
    pass

start.add_command(download)
start.add_command(serve)



