import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Place(Base):
	__tablename__ = 'place'
	id = Column(Integer, primary_key=True)
	name = Column(String(80), nullable=False)
	description = Column(String(500), nullable=False)
	type = Column(String(80), nullable=False)
	rate_times = Column(Integer)
	total_point = Column(Integer)
	img_path = Column(String(), nullable=False)
	rating = Column(Float)

engine = create_engine('sqlite:///places.db')
Base.metadata.create_all(engine)
