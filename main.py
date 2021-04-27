import click
from download import download
from serve import serve

'''
Ideas:
- Create maybe a test-class for testing my API?
- return currency ($)

'''

@click.group()
def start():
    pass

start.add_command(download)
start.add_command(serve)



