from flask_bootstrap import Bootstrap4
from flask import Flask

app = Flask(__name__)

bootstrap = Bootstrap4(app)

from app import routes