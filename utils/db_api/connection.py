from typing import List
from dataclasses import dataclass
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession

from utils.db_api.base import Base
from utils.db_api.models import (
    Country, Place, Sphere, 
    Direction, Emojis, Users,
    ScheduledNotifications
)

from .mixins import UserData


class Database:
    async def load(self) -> AsyncSession:
        engine = create_async_engine(
            "sqlite+aiosqlite:///database.db",
            future=True
        )

        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        # expire_on_commit=False will prevent attributes from being expired
        # after commit.
        async_sessionmaker = sessionmaker(
            engine, expire_on_commit=False, class_=AsyncSession
        )

        self.async_session = async_sessionmaker


    # ---Countries-Place relationship---
    async def reg_country(self, user_id, country, place):
        """Some docs"""

        country_data = await self.get_country(user_id, country)

        async with self.async_session() as session:
            session: AsyncSession

            if not country_data:
                await session.merge(
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
                await session.merge(
                    Place(
                        user_id=user_id,
                        name=place,
                        country_id=country_data.id
                    )
                )

            await session.commit()
        

    async def get_country(self, user_id: int, country: str) -> Country:
        """Some docs"""
        async with self.async_session() as session:
            session: AsyncSession

            country_data = await session.execute(select(Country).filter_by(user_id=user_id, name=country))
            return country_data.scalar()

    
    async def get_selected_countries(self, user_id):
        async with self.async_session() as session:
            session: AsyncSession
            response = await session.execute(select(Country).filter_by(user_id = user_id))
            return response.all()

    
    async def del_country(self, user_id, country):
        """Some docs"""
        async with self.async_session() as session:
            session: AsyncSession

            country_data = await self.get_country(user_id, country)
            await session.delete(country_data)
            await session.commit()


    # ---Places---
    async def get_place(self, user_id, place) -> Place:
        """Some docs"""
        async with self.async_session() as session:
            session: AsyncSession

            response = await session.execute(select(Place).filter_by(user_id=user_id, name=place))

            return response.scalar()


    async def del_place(self, user_id, place):
        """Some docs"""

        place_data = await self.get_place(user_id, place)

        async with self.async_session() as session:
            session: AsyncSession

            country_data = await session.get(Country, place_data.country_id)
            count = await session.execute(select(Place).filter_by(country_id = place_data.country_id))
            
            if len(count.scalars().all()) == 1:
                await self.del_country(user_id, country_data.name)

            else:
                await session.delete(place_data)
                await session.commit()
        

    # ---Sphere-Direction relationship---
    async def reg_sphere(self, user_id, sphere_name, direction_name):
        """Some docs"""

        sphere_data = await self.get_sphere(user_id, sphere_name)
        direction = await self.get_direction(user_id, direction_name)

        async with self.async_session() as session:
            session: AsyncSession

            if not sphere_data:
                await session.merge(
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
            
            elif not direction:
                await session.merge(
                    Direction(
                        user_id=user_id,
                        name=direction_name,
                        sphere_id=sphere_data.id
                    )
                )

            await session.commit()


    async def get_sphere(self, user_id: int, sphere_name: str) -> Sphere:
        """Some docs"""
        async with self.async_session() as session:
            session: AsyncSession

            sphere_data = await session.execute(select(Sphere).filter_by(user_id=user_id, name=sphere_name))
            return sphere_data.scalar()


    async def del_sphere(self, user_id, sphere_name):
        """Some docs"""

        sphere_data = await self.get_sphere(user_id, sphere_name)

        async with self.async_session() as session:
            session: AsyncSession
            await session.delete(sphere_data)
            await session.commit()


    # ---Directions---
    async def get_direction(self, user_id, direction_name) -> Direction:
        """Some docs"""
        async with self.async_session() as session:
            session: AsyncSession
            response = await session.execute(select(Direction).filter_by(user_id=user_id, name=direction_name))

            return response.scalar()


    async def del_direction(self, user_id, direction_name):
        """Some docs"""

        direction_data = await self.get_direction(user_id, direction_name)

        async with self.async_session() as session:
            session: AsyncSession

            sphere_data = await session.get(Sphere, direction_data.sphere_id)            
            count = await session.execute(select(Direction).where(Direction.sphere_id == direction_data.sphere_id))

            if len(count.scalars().all()) == 1:
                await self.del_sphere(user_id, sphere_data.name)

            else:
                await session.delete(direction_data)
                await session.commit()


    # ---Emojis---
    async def reg_emoji(self, user_id, emoji):
        """Some docs"""
        async with self.async_session() as session:
            await session.merge(
                Emojis(
                    user_id=user_id,
                    emoji=emoji
                )
            )
            await session.commit()

    
    async def get_emoji(self, user_id, emoji) -> Emojis:
        async with self.async_session() as session:
            session: AsyncSession
    
            response = await session.execute(select(Emojis).filter_by(user_id = user_id, emoji = emoji))
            return response.scalar()


    async def del_emoji(self, user_id, emoji):
        emoji = await self.get_emoji(user_id, emoji)
        async with self.async_session() as session:
            session: AsyncSession

            await session.delete(emoji)
            await session.commit()


    # ---Users---
    async def reg_user(self, user_id: str, username: str, name: str, age: int):
        """Some docs"""
        async with self.async_session() as session:
            await session.merge(
                Users(
                    user_id = user_id, 
                    username = username,
                    name = name,
                    age = age
                )
            )
            await session.commit()
    

    async def get_user(self, user_id) -> Users:
        """Some docs"""
        async with self.async_session() as session:
            session: AsyncSession

            response = await session.get(Users, user_id)
            return response
    

    async def get_user_data(self, user_id) -> UserData:
        """Some docs"""
        async with self.async_session() as session:
            session: AsyncSession
            
            user = await session.get(Users, user_id)
            country = await session.execute(select(Country).where(Country.user_id == user_id))
            place = await session.execute(select(Place).where(Place.user_id == user_id))
            sphere = await session.execute(select(Sphere).where(Sphere.user_id == user_id))
            direction = await session.execute(select(Direction).where(Direction.user_id == user_id))
            emoji = await session.execute(select(Emojis).where(Emojis.user_id == user_id))

        user_data = UserData(user, country.scalars(), place.scalars(), sphere.scalars(), direction.scalars(), emoji.scalars())

        return user_data
    

    # ---ScheduledNotifications---
    async def reg_new_schedule_date(self, user_id: int, trigger: str, scheduled_date: datetime):
        """Some docs"""
        async with self.async_session() as session:
            session: AsyncSession
            await session.merge(
                ScheduledNotifications(
                    user_id = user_id,
                    trigger = trigger,
                    scheduled_date = scheduled_date
                )
            )
            await session.commit()
    
    # async def get_


    
    # async def update_status(self, user_id):
    #     """Some docs"""
    #     await session.execute(
    #             update(Users).filter(Users.user_id == user_id).
    #             values(status = 'payed')
    #     )
    #     await session.commit()
    

    # async def get_row_count(self):
    #     response = session.query(Users).count()
    #     return response