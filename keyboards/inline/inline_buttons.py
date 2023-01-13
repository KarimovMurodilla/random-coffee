from aiogram import types
from .indicator import show
from .data import places, spheres

def show_countries(user_id):
    menu = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text=show("ТАЙЛАНД🇹🇭", user_id), callback_data="thai")
    btn2 = types.InlineKeyboardButton(text=show("ГРУЗИЯ🇬🇪", user_id), callback_data="georgia")
    btn3 = types.InlineKeyboardButton(text=show("ИЗРАИЛЬ🇮🇱", user_id), callback_data="israel")
    btn4 = types.InlineKeyboardButton(text=show("ОАЭ🇦🇪", user_id), callback_data="uae")
    btn5 = types.InlineKeyboardButton(text=show("КАЗАХСТАН🇰🇿", user_id), callback_data="kazakhstan")
    btn6 = types.InlineKeyboardButton(text=show("ТУРЦИЯ🇹🇷", user_id), callback_data="turkey")
    btn7 = types.InlineKeyboardButton(text=show("ИНДОНЕЗИЯ🇮🇩", user_id), callback_data="indonesia")
    btn8 = types.InlineKeyboardButton(text=show("АРМЕНИЯ🇦🇲", user_id), callback_data="armenia")
    menu.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)

    return menu


def show_places(country, user_id):
    menu = types.InlineKeyboardMarkup(row_width=2)

    for place in places.get(country):
        btn = types.InlineKeyboardButton(text=show(place, user_id), callback_data=place)
        menu.insert(btn)
    
    return menu


def show_spheres(user_id):
    menu = types.InlineKeyboardMarkup(row_width=2)

    for sphere in spheres.keys():
        btn = types.InlineKeyboardButton(text=show(sphere, user_id), callback_data=sphere)
        menu.insert(btn)
    
    return menu


def show_more_spheres(user_id, sphere):
    menu = types.InlineKeyboardMarkup(row_width=2)

    for sphere in spheres.get(sphere).keys():
        btn = types.InlineKeyboardButton(text=show(sphere, user_id), callback_data=sphere)
        menu.insert(btn)
    
    return menu