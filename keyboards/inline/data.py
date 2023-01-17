places = {
    'georgia': ['Тбилиси', 'Батуми', 'Рустави', 'Кутаиси', 'Сухуми', 'Гори', 'Поти', 'Зугдиди', 'ДРУГОЕ'],
    'israel': ['Иерусалим', 'Тель-Авив', 'Ашкелон', 'Тверия', 'Цфат', 'Хайфа', 'Ришон-ле-Цион', 'Петах-Тиква', 'Ашдод', 'Нетания', 'Беэр-Шева', 'ДРУГОЕ'],
    'kazakhstan': ['Алма-Ата', 'Астана', 'Шымкент', 'Актобе', 'Караганда', 'Тараз', 'Атырау', 'Павлодар', 'ДРУГОЕ'],
    'turkey': ['Стамбул', 'Анкара', 'Измир', 'Бурса', 'Алания', 'Каш', 'Конья', 'Анталья', 'ДРУГОЕ'],
    'indonesia': ['Бали', 'Джакарта', 'Сурабая', 'Бандунг', 'Бекаси', 'Медан', 'Тангеранг', 'Депок', 'Семаранг', 'ДРУГОЕ'],
    'armenia': ['Ереван', 'Гюмри', 'Иджеван', 'Дилижан', 'Алаверди', 'Джермук', 'Агарак', 'ДРУГОЕ'],
    'thai': ['Паттая', 'Самуи', 'Панган', 'Бангкок', 'Нонтхабури', 'Хатъяй', 'Сураттхани', 'Удонтхани', 'Накхонратчасима', 'Чиангмай', 'Кхонкэн', 'ДРУГОЕ']
}

spheres = {
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
    },

    "В ПОИСКЕ": {
        'Работы': 'Попробуй местные чатики. Там всегда кто-то кого-то ищет. Я нашел сына.',
        'Себя': 'Ответ во фронтальной камере твоего телефона. Не благодари.',
        'Друга': 'Ну, меня ты уже нашел! А над дальнейшим поработаем!',
        'Дивана': 'Дай мысленно пять!',
        'Другое': 'Неожиданно, введи сферу в строке ниже. Пример: Искусство'
    },
    "ДРУГОЕ": None
}


# TODO write this text into dict

emojis_and_answers = {
    'all_emojis': ['🎬' , '🎶',  '🍫', '🐕',  '🐈',  '🪴', '🚘', '🏖', '⛺️', '📸', '🎮', '🧘‍♂️', '🏄', '🏊', '🧗‍♀️',  '🚴', '⛹️', '🪂', '🏂', '🎿', '🛼', '🛹', '🥋', '🏓', '🏸', '🏒', '🪳', '🕷', '🐍', '🏃', '🖕', '👻'],
    '⛺️':  'В этой стране такая шикарная природа',
    '🐕':  'тоже люблю животных, у нас столько общего',
    '🐈':  'тоже люблю животных, у нас столько общего',
    '🪳':  'не говори об этом арендодателю. У вас есть питомцы? — Таракан? Кто сказал таракан? Это кот.',
    '🕷':  'не говори об этом арендодателю. У вас есть питомцы? — Таракан? Кто сказал таракан? Это кот.',
    '📸':  'Ооо! Представляю, какие красивые снимки ты можешь сделать в этой стране.',
    '🎬':  'Мой любимый фильм «Трансформеры», первый',
    '🪴':  'Фикус также называют «каучуковым деревом»',
    '🚘':  'Бери машину в аренду и отправляйся исследовать страну',
    '🏄':  'Ответ только для Грузии, Тайланда, ИЗРАИЛЯ, Турции, Индонезии: Тебе повезло, в этой стране есть море, и оно, считай, под рукой.',
    '🏊':  'Ответ только для Грузии, Тайланда, ИЗРАИЛЯ, Турции, Индонезии: Тебе повезло, в этой стране есть море, и оно, считай, под рукой.',
    '🖕':  'Хотел бы я знать, что это значит.',
    '👩‍❤️‍👩':  'Когда меня спрашивают, что важнее, еда или любовь, я молчу, потому что ем.',
    '👩‍❤️‍👨':  'Когда меня спрашивают, что важнее, еда или любовь, я молчу, потому что ем.',
    '👨‍❤️‍👨':  'Когда меня спрашивают, что важнее, еда или любовь, я молчу, потому что ем.',
    '🧖':  'В баньке главное не бухать с друзьями. А то мало ли где завтра проснёшься',
    '👻':  'Лучший фильм ужасов — «Дети кукурузы» '
}

print(emojis_and_answers['👨‍❤️‍👨'])