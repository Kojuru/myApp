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
    '''
)