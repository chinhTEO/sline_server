from sqlalchemy import *

db = create_engine('sqlite:///db/server.db')

db.echo = False  # Try changing this to True and see what happens

metadata = MetaData(db)

users = Table('itemProperty', metadata,
    Column('QRid', Integer, primary_key=True),
    Column('name', String),
    Column('description', String),

    Column('size_1', Integer),
    Column('size_2', Integer),
    Column('size_3', Integer),
    Column('color', String),
    Column('function', String),

    Column('image_1_filename', String),
    Column('image_2_filename', String),
    Column('image_3_filename', String),
    Column('image_4_filename', String),
)

users.create()

