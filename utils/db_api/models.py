from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, Integer, String, ForeignKey

from utils.db_api.base import Base


class Users(Base):
    __tablename__ = "users"

    user_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)
    username = Column(String(20))
    name = Column(String(50))
    age = Column(Integer)


class Country(Base):
    __tablename__ = "country"

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger)
    name = Column(String(50), nullable=False)
    places = relationship("Place", cascade="all, delete")


class Place(Base):
    __tablename__ = "place"

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger)
    name = Column(String(50), nullable=False)
    country_id = Column(Integer, ForeignKey("country.id"), nullable=False)


class Sphere(Base):
    __tablename__ = "sphere"

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger)
    name = Column(String(50))
    directions = relationship("Direction", cascade="all, delete")


class Direction(Base):
    __tablename__ = "direction"

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger)
    name = Column(String(50))
    sphere_id = Column(Integer, ForeignKey('sphere.id'), nullable=False)


class Emojis(Base):
    __tablename__ = "emojis"

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger)
    emoji = Column(String(5))