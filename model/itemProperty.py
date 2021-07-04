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
            size_1 = db.Column(db.Integer) 
            size_2 = db.Column(db.Integer) 
            size_3 = db.Column(db.Integer) 
            color = db.Column(db.String)
            function = db.Column(db.String)
            image_1_filename = db.Column(db.String)
            image_2_filename = db.Column(db.String)
            image_3_filename = db.Column(db.String)
            image_4_filename = db.Column(db.String)

            isInDB = False

            def __init__(self):
                self.serverCfg = ServerCfg.getInstance()

            def setPropertyByArgs(self,args):
                self.QRid = args['QRid']
                self.name = args['name']
                self.description = args['description']
                self.size_1 = args['size_1']
                self.size_2 = args['size_2']
                self.size_3 = args['size_3']
                self.color = args['color']
                self.function = args['function']
                self.image_1 = args['image_1']
                self.image_2 = args['image_2']
                self.image_3 = args['image_3']
                self.image_4 = args['image_4']

            def setProperty(self,
                            QRid,
                            name,
                            description,
                            size_1,
                            size_2,
                            size_3,
                            color,
                            function,
                            image_1,
                            image_2,
                            image_3,
                            image_4):
                self.QRid = QRid
                self.name = name
                self.description = description
                self.size_1 = size_1
                self.size_2 = size_2
                self.size_3 = size_3 
                self.color = color
                self.function = function
                self.image_1 = image_1
                self.image_2 = image_2
                self.image_3 = image_3
                self.image_4 = image_4

            def getItemByID(self, QRid):
                item = {}
                results = self.query.get(QRid)
                item['QRid'] = results.QRid
                item['name'] = results.name
                item['description'] = results.description
                item['size_1'] = results.size_1
                item['size_2'] = results.size_2
                item['size_3'] = results.size_3
                item['color'] = results.color
                item['function'] = results.function
                if results.image_1_filename:
                    item['image_1_filename'] = results.image_1_filename
                else:
                    item['image_1_filename'] = ""
                if results.image_2_filename:
                    item['image_2_filename'] = results.image_2_filename
                else:
                    item['image_2_filename'] = ""
                if results.image_3_filename:
                    item['image_3_filename'] = results.image_3_filename
                else:
                    item['image_3_filename'] = ""
                if results.image_4_filename:
                    item['image_4_filename'] = results.image_4_filename
                else:
                    item['image_4_filename'] = ""
                return jsonify(item)

            def toDic(self):
                return {
                    "QRid": self.QRid,
                    "name": self.name,
                    "description": self.description,

                    "size_1": self.size_1,
                    "size_2": self.size_2,
                    "size_3": self.size_3,
                    "color": self.color,
                    "function":  self.function,
                }

            def saveToDB(self):
                if self.image_1:
                    self.image_1_filename = "{}.jpg".format(uuid.uuid4().hex)
                
                if self.image_2:
                    self.image_2_filename = "{}.jpg".format(uuid.uuid4().hex)

                if self.image_3:
                    self.image_3_filename = "{}.jpg".format(uuid.uuid4().hex)

                if self.image_4:
                    self.image_4_filename = "{}.jpg".format(uuid.uuid4().hex)

                if self.image_1_filename:
                    self.image_1.save(self.serverCfg.ImgPath + "/" + self.image_1_filename)
                if self.image_2_filename:
                    self.image_2.save(self.serverCfg.ImgPath + "/" + self.image_2_filename)
                if self.image_3_filename:
                    self.image_3.save(self.serverCfg.ImgPath + "/" + self.image_3_filename)
                if self.image_4_filename:
                    self.image_4.save(self.serverCfg.ImgPath + "/" + self.image_4_filename)
                    
                db.session.add(self)
                db.session.commit()