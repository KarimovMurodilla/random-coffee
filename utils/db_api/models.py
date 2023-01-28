from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, Integer, String, ForeignKey

from utils.db_api.base import Base


class Users(Base):
    __tablename__ = "users"

    user_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)
    username = Column(String(20))
    name = Column(String(50))
    age = Column(Integer)

# TODO
class Country(Base):
    __tablename__ = "country"

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger)
    name = Column(String(50), nullable=False)
    places = relationship("Place", cascade="all, delete")

# TODO
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


# class User(Base):
#     __tablename__ = 'user'

#     id = Column(Integer, primary_key=True)
#     name = Column(String(50), nullable=False)
#     addresses = relationship("Address", backref="user")

# class Address(Base):
#     __tablename__ = 'address'

#     id = Column(Integer, primary_key=True)
#     email_address = Column(String(50), nullable=False)
#     user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    