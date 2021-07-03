from sqlalchemy import *

db = create_engine("mysql+mysqlconnector://sline:sline@localhost/slineDB")

db.echo = False  # Try changing this to True and see what happens

metadata = MetaData(db)

users = Table('itemProperty', metadata,
    Column('QRid', Integer, primary_key=True),
    Column('name', String(64)),
    Column('description', String(255)),

    Column('size_1', Integer),
    Column('size_2', Integer),
    Column('size_3', Integer),
    Column('color', String(64)),
    Column('function', String(64)),

    Column('image_1_filename', String(100)),
    Column('image_2_filename', String(100)),
    Column('image_3_filename', String(100)),
    Column('image_4_filename', String(100)),
)

users.create()

