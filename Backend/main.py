# main.py
from flask import Flask

app = Flask(__name__)

from rotas import *

if __name__ == '__main__':
    print("Rotas registradas:", app.url_map)
    app.run(debug=True)
