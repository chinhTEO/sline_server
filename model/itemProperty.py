from datetime import datetime
from flask_restful import reqparse
from serverCfg import ServerCfg
from baseServices import db
from flask import jsonify
import uuid

class itemPropertyDB(db.Model):
            __tablename__ = 'itemProperty'
            __table_args__ = {'extend_existing': True}
            QRid = db.Column('QRid', db.Integer, primary_key = True)
            name = db.Column(db.String)
            description = db.Column(db.String)
            color = db.Column(db.String)
            function = db.Column(db.String)
            images = db.Column(db.JSON)
            created_date = db.Column(db.Date)
            last_accessed_date = db.Column(db.Date)
            status = db.Column(db.String)
            enable = db.Column(db.Boolean)

            def __init__(self):
                self.serverCfg = ServerCfg.getInstance()

            def setPropertyByArgs(self,args):
                self.QRid = args['QRid']
                self.name = args['name']
                self.description = args['description']
                self.color = args['color']
                self.function = args['function']
                self.images = args['images[]']
                self.status = ""
                self.enable = True
                self.last_accessed_date = datetime.now()
                self.created_date = datetime.now()

            def getItemByID(self, QRid):
                item = {}
                results = self.query.get(QRid)
                item['QRid'] = results.QRid
                item['name'] = results.name
                item['description'] = results.description
                item['color'] = results.color
                item['function'] = results.function
                item['images'] = results.images
                return jsonify(item)

            def toDic(self):
                return {
                    "QRid": self.QRid,
                    "name": self.name,
                    "description": self.description,
                    "color": self.color,
                    "function":  self.function,
                }

            def saveToDB(self):
                imagesName = {}
                imagesName['name'] = []
                for image in self.images:
                    filename = "{}.jpg".format(uuid.uuid4().hex)
                    image.save(self.serverCfg.ImgPath + "/" + filename)
                    imagesName['name'].append(filename)

                self.images = imagesName
                    
                db.session.add(self)
                db.session.commit()