import sqlalchemy as db


engine = db.create_engine('sqlite:///test_db.db', echo=True)

# Create the Metadata Object
metadata_obj = db.MetaData()

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


converter_pages = db.Table(
    'ConverterPages',
    metadata_obj,
    db.Column('id', db.Integer, autoincrement=True, primary_key=True),
    db.Column('name', db.String, nullable=False),
    db.Column('ff', db.String, nullable=False),
    db.Column('tf', db.String, nullable=False),
    db.Column('category', db.Integer, nullable=False),
    db.Column('image', db.String),
)


# Create the profile table
metadata_obj.create_all(engine)