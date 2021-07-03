from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from serverCfg import ServerCfg

cfg = ServerCfg.getInstance()
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = cfg.DBpath
db = SQLAlchemy(app)