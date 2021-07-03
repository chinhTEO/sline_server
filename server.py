from flask_restful import Resource, reqparse
from serverCfg import ServerCfg
import werkzeug
import random
from model.itemProperty import itemPropertyDB
from baseServices import db, api, app

# class Item(serverDB.getInstance().DB.Model):
#     __tablename__ = 'Item'
#     db = serverDB.getInstance().DB
#     QR_ID = db.Column(db.Integer, primary_key=True)


class HelloWorld(Resource):
    def get(self):
        return {'status': 'OK',
                'msg': 'hello'}



class NewItem(Resource):
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('QRid', required=True, type=int, location='form')
        parse.add_argument('name', required=True, type=str, location='form')
        parse.add_argument('description', required=True, type=str, location='form')

        parse.add_argument('size_1', required=True, type=int, location='form')
        parse.add_argument('size_2', required=True, type=int, location='form')
        parse.add_argument('size_3', required=True, type=int, location='form')
        parse.add_argument('color', required=True, type=str, location='form')
        parse.add_argument('function', required=True, type=str, location='form')

        parse.add_argument('image_1', type=werkzeug.datastructures.FileStorage, location='files')
        parse.add_argument('image_2', type=werkzeug.datastructures.FileStorage, location='files')
        parse.add_argument('image_3', type=werkzeug.datastructures.FileStorage, location='files')
        parse.add_argument('image_4', type=werkzeug.datastructures.FileStorage, location='files')

        args = parse.parse_args()

        item = itemPropertyDB()
        item.setPropertyByArgs(args)

        print(item.toDic())

        item.saveToDB()

        return {'status': 'OK',
                'msg': 'upload successfully'}

class checkItem(Resource):
    def get(self,QRid):
        print(QRid)
        item = itemPropertyDB()
        return item.getItemByID(QRid)


api.add_resource(checkItem,'/utility/check/<int:QRid>')
api.add_resource(NewItem,'/new')
api.add_resource(HelloWorld,'/')

if __name__ == '__main__':      
    app.run(debug=True,host="192.168.1.112",port=8080)