from aiogram import types


def pay_and_question():
    menu = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="Общая информация о канале и обо мне", callback_data="info")
    btn2 = types.InlineKeyboardButton(text="Вопрос", callback_data="question")
    menu.add(btn1, btn2)

    return menu


def test():
    data = [1, 2, 3, 4]
    menu = types.InlineKeyboardMarkup(row_width = 2)
    back = types.InlineKeyboardButton("Back", callback_data='back')
    
    menu.add(back)
    menu.add(*[types.InlineKeyboardButton(str(i), callback_data=str(i)) for i in data])
    
    return menu