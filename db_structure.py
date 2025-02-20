import sqlalchemy as db

# Defining the Engine
from sqlalchemy import insert

engine = db.create_engine('sqlite:///test_db.db', echo=True)

# Create the Metadata Object
metadata_obj = db.MetaData()

# Define the profile table

# database name
pages = db.Table(
    'Pages',
    metadata_obj,
    db.Column('id', db.Integer, autoincrement=True, primary_key=True),
    db.Column('name', db.String, nullable=False),
    db.Column('slug', db.String, nullable=False),
    db.Column('category', db.Integer, nullable=False),
    db.Column('image', db.String),
)


# Create the profile table
metadata_obj.create_all(engine)