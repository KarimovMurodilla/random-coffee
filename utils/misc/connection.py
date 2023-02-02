from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy import update, delete
from sqlalchemy.orm import sessionmaker

from utils.db_api.base import Base
from utils.db_api.models import Country, Place, Sphere, Direction, Emojis

db_string = r"sqlite:///database.db"
db = create_engine(db_string)  

Session = sessionmaker(db)  
session = Session()

Base.metadata.create_all(db)


class Database:
    # ---Countries-Place relationship---
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

    
    def get_selected_countries(self, user_id):
        response = session.query(Country).filter_by(user_id = user_id).first()
        return response

    
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
        

    # ---Sphere-Direction relationship---
    def reg_sphere(self, user_id, sphere_name, direction_name):
        """Some docs"""

        sphere_data = self.get_sphere(user_id, sphere_name)

        if not sphere_data:
            session.merge(
                Sphere(
                    user_id=user_id,
                    name=sphere_name,
                    directions=[
                        Direction(
                            user_id=user_id,
                            name=direction_name
                        )
                    ]
                )
            )
        
        else:
            session.merge(
                Direction(
                    user_id=user_id,
                    name=direction_name,
                    sphere_id=sphere_data.id
                )
            )

        session.commit()


    def get_sphere(self, user_id: int, sphere_name: str) -> Sphere:
        """Some docs"""
        sphere_data = session.query(Sphere).filter_by(user_id=user_id, name=sphere_name).first()
        return sphere_data


    def del_sphere(self, user_id, sphere_name):
        """Some docs"""

        sphere_data = self.get_sphere(user_id, sphere_name)
        session.delete(sphere_data)
        session.commit()


    # ---Directions---
    def get_direction(self, user_id, direction_name) -> Direction:
        """Some docs"""
        response = session.query(Direction).\
            filter_by(user_id=user_id, name=direction_name).first()

        return response

    def del_direction(self, user_id, direction_name):
        """Some docs"""

        direction_data = self.get_direction(user_id, direction_name)

        sphere_data = session.query(Sphere).\
            filter_by(id = direction_data.sphere_id).first()

        count = session.query(Direction).\
            filter_by(sphere_id = direction_data.sphere_id).count()
        
        if count == 1:
            self.del_sphere(user_id, sphere_data.name)

        else:
            session.delete(direction_data)
            session.commit()


    # ---Emojis---
    def reg_emoji(self, user_id, emoji):
        """Some docs"""
        session.merge(
            Emojis(
                user_id=user_id,
                emoji=emoji
            )
        )
        session.commit()
    
    def get_emoji(self, user_id, emoji):
        response = session.query(Emojis).filter_by(user_id=user_id, emoji=emoji).first()
        return response

    def del_emoji(self, user_id, emoji):
        emoji = self.get_emoji(user_id, emoji)
        session.delete(emoji)
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