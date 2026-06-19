from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:vishal%402709@localhost:5432/KitKat"
engine = create_engine(db_url)
session = sessionmaker(autoflush = False, autocommit = False, bind = engine) 