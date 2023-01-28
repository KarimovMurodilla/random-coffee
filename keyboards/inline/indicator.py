"""
Indicator for inline buttons
"""
from loader import db
from .data import ru2en


def show(text, user_id, flag = None):
    if not flag:
        response = db.get_country(user_id, ru2en[text])

    elif flag == 'places':
        response = db.get_place(user_id, text)
    
    else:
        response = None


    status = '✅' if response else ''
    return f"{text} {status}"