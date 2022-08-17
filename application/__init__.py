from flask import Flask
from application.data_connection import DataBase
from config import Config

database = DataBase('media_library.db')
app = Flask(__name__)
app.secret_key = Config.SECRET_KEY

from application import routes