from typing import List
from dataclasses import dataclass
from utils.db_api.models import (
    Country, Place, Sphere, 
    Direction, Emojis, Users
)


@dataclass
class UserData:
    user: Users
    country: List[Country]
    place: List[Place]
    sphere: List[Sphere]
    direction: List[Direction]
    emoji: List[Emojis]