from aiogram import types


def send_contact():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Поделиться контактом", request_contact=True)
    menu.add(btn1)

    return menu