from sqlalchemy import create_engine
from lib.models import Base

# Create an engine that will connect to an SQLite database file
engine = create_engine('sqlite:///theater.db')

# Create all tables in the database (from models.py)
Base.metadata.create_all(engine)
