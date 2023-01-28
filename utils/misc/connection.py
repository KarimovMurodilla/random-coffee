from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy import update, delete
from sqlalchemy.orm import sessionmaker

from utils.db_api.base import Base
from utils.db_api.models import Country, Place

db_string = r"sqlite:///database.db"
db = create_engine(db_string)  

Session = sessionmaker(db)  
session = Session()

Base.metadata.create_all(db)


class Database:
    # ---Countries---
    def reg_country(self, user_id, country, place):
        """Some docs"""

        country_data = self.get_country(user_id, country)

        if not country_data:
            session.merge(
                Country(
                    user_id=user_id,
                    name=country,
                    places=[
                        Place(
                            user_id=user_id,
                            name=place
                        )
                    ]
                )
            )
        
        else:
            session.merge(
                Place(
                    user_id=user_id,
                    name=place,
                    country_id=country_data.id
                )
            )

        session.commit()
    

    def get_country(self, user_id: int, country: str) -> Country:
        """Some docs"""
        country_data = session.query(Country).filter_by(user_id=user_id, name=country).first()
        return country_data

    
    def del_country(self, user_id, country):
        """Some docs"""

        country_data = self.get_country(user_id, country)
        session.delete(country_data)
        session.commit()


    # ---Places---
    def get_place(self, user_id, place) -> Place:
        """Some docs"""
        response = session.query(Place).\
            filter_by(user_id=user_id, name=place).first()

        return response


    def del_place(self, user_id, place):
        """Some docs"""

        place_data = self.get_place(user_id, place)

        country_data = session.query(Country).\
            filter_by(id = place_data.country_id).first()

        count = session.query(Place).\
            filter_by(country_id = place_data.country_id).count()
        
        if count == 1:
            self.del_country(user_id, country_data.name)

        else:
            session.delete(place_data)
            session.commit()







    # # ---Users---
    # def reg_user(self, user_id: str, username: str, name: str, insta: str, contact: str):
    #     """Some docs"""
    #     session.merge(Users(user_id = user_id, 
    #                         username = username,
    #                         name = name,
    #                         insta = insta,
    #                         contact = contact
    #                         )
    #                     )
    #     session.commit()
    

    # def get_user(self, user_id) -> Users:
    #     """Some docs"""
    #     response = session.query(Users).filter(Users.user_id == user_id).first()
    #     return response

    
    # def update_status(self, user_id):
    #     """Some docs"""
    #     session.execute(
    #             update(Users).filter(Users.user_id == user_id).
    #             values(status = 'payed')
    #     )
    #     session.commit()
    

    # def get_row_count(self):
    #     response = session.query(Users).count()
    #     return response