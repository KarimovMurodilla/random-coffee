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


def show_sphere():
    d = {
        'СММ': {
            'ФОТО': None, 
            'ВИДЕО': None, 
            'СТОРИМЕЙКЕР': None, 
            'ТАРГЕТИНГ': None, 
            'КОПИРАЙТИНГ': None, 
            'ВСЕ ВМЕСТЕ': None
        },

        'ПРОДАЖИ': {
            'ОДЕЖДА': None, 
            'ПРОДУКТЫ': None, 
            'ТЕХНИКА': None, 
            'ИНФОРМАЦИЯ': None, 
            'УСЛУГИ': None, 
            'ДРУГОЕ': 'Не поверю, пока не расскажешь! Только пиши в одно слово, например, Органы.'
        },

        'ХЕНД-МЕЙД': {
            'ИГРУШКИ': None, 
            'УКРАШЕНИЯ': None, 
            'РИСОВАНИЕ': None, 
            'КВИЛЛИНГ': 'А ты знаешь толк в развлечениях', 
            'ЛЕПКА': None, 
            'ДРУГОЕ': 'Не поверю, пока не расскажешь! Только пиши в одно слово, например, Шитьё'
        },

        'КРАСОТА': {
            'БРОВИСТ': None, 
            'ЛЕШМЕЙКЕР': None, 
            'КОСМЕТОЛОГ': None, 
            'МАНИКЮР': None, 
            'ДЕПИЛЯЦИЯ': None, 
            'КОСМЕТОЛОГ': None, 
            'ВИЗАЖИСТ': None
        },

        'ЗДОРОВЬЕ': {
            'МАССАЖ': None, 
            'КОСМЕТОЛОГ': None, 
            'СТОМАТОЛОГ': None, 
            'ХИРУРГ': None, 
            'МЕДСЕСТРА': None, 
            'МЕДБРАТ': None, 
            'ДРУГОЕ': 'Напиши одним словом, например, Уролог'
        },

        'ИНВЕСТИЦИИ': {
            'АКЦИИ': None, 
            'МЕТАЛЛЫ': None, 
            'ФОНДОВЫЙ РЫНОК': None, 
            'КРИПТА': None, 
            'NFT': None, 
            'ВЕНЧУР': None, 
            'НЕДВИЖИМОСТЬ': None, 
            'В СЕБЯ': None, 
            'ДРУГОЕ': 'Напиши одним словом, например, Стартапы В СЕБЯ: Я тоже инвестирую в себя.'
        },

        'IT': {
            'ВЕБ': None, 
            'ИГРЫ': None, 
            'ПРИЛОЖЕНИЯ': None, 
            'НЕЙРОСЕТЬИ': None, 
            'ДАТАСАЕНТИСТ': None, 
            'ПРОГГЕР': None, 
            'QA': None, 
            'ДРУГОЕ': 'Напиши одним словом, например, Юзабилити КРИПТА:  ИНВЕСТИРУЮ, АКТИВНО ТОРГУЮ, NFT, GAMEFI ПУТЕШЕСТВИЯ'
        },

        'ДИЗАЙН': {
            'ИНТЕРЬЕРОВ': None, 
            'UX': None, 
            'UI': None, 
            'ИГРОВОЙ': None, 
            'ГРАФИЧЕСКИЙ': None, 
            'IxD': None, 
            'ДРУГОЕ': 'Напиши одним словом, например, Продуктовый МУЗЫКА: ИГРАЮ НА ИНСТРУМЕНТЕ-DJ-РЕПЧИК ЧИТАЮ-ПОЮ-БИТМЕЙКЕР'
        },

        'ПРОИЗВОДСТВО': {
            'МЕБЕЛИ': None, 
            'ОДЕЖДЫ': None, 
            'ТЕХНИКИ': None, 
            'ПРОДУКТОВ': None, 
            'ДРУГОЕ': 'Напиши одним словом, например, Бумаги В ПОИСКЕ'
        }
    }