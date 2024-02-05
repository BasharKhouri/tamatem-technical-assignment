import os
from flask import Flask
from waitress import serve
import time
import logging, sys
port=os.environ.get('PORT', 8080)

app = Flask(__name__)
logging.getLogger().setLevel(logging.INFO)

@app.route('/')
def hello():
	return 'Hello Tamatem!'

if __name__ == '__main__':
	serve(app, port=port)