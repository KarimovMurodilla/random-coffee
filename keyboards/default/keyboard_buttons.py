from aiogram import types


def check_name():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
    btn1 = types.KeyboardButton("Верно")
    btn2 = types.KeyboardButton("Исправить")
    menu.add(btn1, btn2)

    return menu


def show_jobs():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
    btn1 = types.KeyboardButton("БЛОГЕР")
    btn2 = types.KeyboardButton("В НАЙМЕ")
    btn3 = types.KeyboardButton("СВОЙ БИЗНЕС")
    btn4 = types.KeyboardButton("ФРИЛАНСЕР")
    btn5 = types.KeyboardButton("НАХЛЕБНИК")
    btn6 = types.KeyboardButton("Avon")
    menu.add(btn1, btn2, btn3, btn4, btn5, btn6)

    return menu


def main_menu():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
    btn1 = types.KeyboardButton("Профиль")
    btn2 = types.KeyboardButton("Поддержка")
    btn3 = types.KeyboardButton("Настройка")
    btn4 = types.KeyboardButton("one-click")
    menu.add(btn1, btn2, btn3, btn4)

    return menu