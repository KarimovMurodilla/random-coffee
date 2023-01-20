from distutils.sysconfig import get_makefile_filename
from sqlalchemy import Column, BigInteger, Integer, String

from utils.db_api.base import Base


class Users(Base):
    __tablename__ = "users"

    user_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)
    username = Column(String(20))
    name = Column(String(50))
    age = Column(Integer)


class Spheres(Base):
    __tablename__ = "spheres"

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger)




    