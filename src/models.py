import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), index=True, nullable=False)
    firstname = Column(String(30), nullable=False)
    lastname = Column(String(30), nullable=False)
    #email = Column(String(100), unique=True, nullable=False)
    password = Column(String(20), unique=True, nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    birth_year = Column(String(40), nullable=False)
    gender = Column(String(40), nullable=False)
    height = Column(Integer)
    skin_color = Column(String(40), nullable=False)
    hair_color = Column(String(40), nullable=False)
    eye_color = Column(String(40), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    terrain = Column(String(40), nullable=False)
    climate = Column(String(40), nullable=False)
    population = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    diameter = Column(Integer)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')