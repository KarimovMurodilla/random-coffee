from aiogram import types
from .indicator import show
from .data import places, spheres, emojis_and_answers

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
    done = types.InlineKeyboardButton(text='ГОТОВО ☑', callback_data="done")
    menu.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, done)

    return menu


def show_places(countries, user_id):
    menu = types.InlineKeyboardMarkup(row_width=2)

    all_places = [place for place in [places.get(country) for country in countries]]

    for country in countries:
        for place in places.get(country):
            btn = types.InlineKeyboardButton(text=show(place, user_id), callback_data=place)
            menu.insert(btn)

    other = types.InlineKeyboardButton(text='ДРУГОЕ', callback_data="ДРУГОЕ")
    done = types.InlineKeyboardButton(text='ГОТОВО ☑', callback_data="done")
    menu.add(other)
    menu.add(done)
    
    return menu


def show_spheres(user_id):
    menu = types.InlineKeyboardMarkup(row_width=2)

    for sphere in spheres.keys():
        btn = types.InlineKeyboardButton(text=show(sphere, user_id), callback_data=sphere)
        menu.insert(btn)

    done = types.InlineKeyboardButton(text='ГОТОВО ☑', callback_data="done")
    menu.add(done)

    return menu


def show_more_spheres(user_id, sphere, check = None):
    menu = types.InlineKeyboardMarkup(row_width=2)

    if not check:
        for sphere in spheres.get(sphere).keys():
            btn = types.InlineKeyboardButton(text=show(sphere, user_id), callback_data=sphere)
            menu.insert(btn)

        done = types.InlineKeyboardButton(text='ГОТОВО ☑', callback_data="done")
        menu.add(done)     

        return menu

    else:
        return spheres.get(sphere).get(check)


def show_in_search_buttons():
    menu = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(text="Работы", callback_data="work")
    btn2 = types.InlineKeyboardButton(text="Себя", callback_data="me")
    btn3 = types.InlineKeyboardButton(text="Друга", callback_data="friend")
    btn4 = types.InlineKeyboardButton(text="Дивана", callback_data="sofa")
    btn5 = types.InlineKeyboardButton(text="Другое", callback_data="other")
    done = types.InlineKeyboardButton(text='ГОТОВО ☑', callback_data="done")
    menu.add(btn1, btn2, btn3, btn4, btn5)
    menu.add(done)

    return menu


def show_emojis(user_id, emoji=None):
    menu = types.InlineKeyboardMarkup(row_width=2)
    
    if not emoji:
        for emoji in emojis_and_answers.get('all_emojis'):
            btn = types.InlineKeyboardButton(text=show(emoji, user_id), callback_data=emoji)
            menu.insert(btn)        
        done = types.InlineKeyboardButton(text='ГОТОВО ☑', callback_data="done")
        menu.add(done)
        
        return menu

    else:
        return emojis_and_answers.get(emoji)

    


def share():
    text = '@RandomCoffeeBot: Бот для нахождения новых друзей'
    menu = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Пригласить", url=f"tg://share?text={text}")
    menu.add(btn1)

    return menu    