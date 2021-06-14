from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy
from serverCfg import ServerCfg
import werkzeug

cfg = ServerCfg.getInstance()
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = cfg.DBpath
db = SQLAlchemy(app)


            
# class Item(serverDB.getInstance().DB.Model):
#     __tablename__ = 'Item'
#     db = serverDB.getInstance().DB
#     QR_ID = db.Column(db.Integer, primary_key=True)


class HelloWorld(Resource):
    def get(self):
        serverCfg = ServerCfg.getInstance()
        return {'hello': serverCfg.DBpath}


class NewItem(Resource):
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
        parse.add_argument('name', required=True, type=str, location='form')
        parse.add_argument('description', required=True, type=str, location='form')
        parse.add_argument('color', required=True, type=str, location='form')
        args = parse.parse_args()
        audioFile = args['file']
        audioFile.save("your_file_name.jpg")
        return {'out':'ok',
                'name': args['name'],
                'des': args['description'],
                'color': args['color']}

api.add_resource(NewItem,'/new')
api.add_resource(HelloWorld,'/')

if __name__ == '__main__':      
    app.run(debug=True,host="192.168.1.112",port=8080)