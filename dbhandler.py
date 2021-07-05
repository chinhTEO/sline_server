from sqlalchemy import *

db = create_engine("mysql+mysqlconnector://sline:sline@localhost/slineDB")

db.echo = False  # Try changing this to True and see what happens

metadata = MetaData(db)

users = Table('itemProperty', metadata,
    Column('qrid', Integer, primary_key=True),
    Column('name', String(64)),
    Column('description', String(255)),

    Column('color', String(64)),
    Column('function', String(64)),

    Column('images', JSON),
    Column('created_date', Date),
    Column('last_accessed_date', Date),

    Column('status', String(64)),
    Column('enable', Boolean)
)

users.create()

