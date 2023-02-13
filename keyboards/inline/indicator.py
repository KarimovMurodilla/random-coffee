"""
Indicator for inline buttons
"""
from loader import db


async def show(text, user_id, flag = None):
    if not flag:
        response = await db.get_country(user_id, text)

    elif flag == 'places':
        response = await db.get_place(user_id, text)
    
    elif flag == 'spheres':
        response = await db.get_sphere(user_id, text)

    elif flag == 'more_spheres':
        response = await db.get_direction(user_id, text)
    
    elif flag == 'emojis':
        response = await db.get_emoji(user_id, text)
    
    else:
        response = None


    status = '✅' if response else ''
    return f"{text} {status}"