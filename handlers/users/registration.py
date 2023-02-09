import asyncio
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db
from states.generic import Reg
from keyboards.inline import inline_buttons
from keyboards.default import keyboard_buttons


@dp.message_handler(state=Reg.check_name)
async def process_check_name(message: types.Message, state: FSMContext):
    if message.text == 'Верно':
        async with state.proxy() as data:
            data['name'] = message.from_user.first_name


        msg = await message.answer('ㅤ', reply_markup=types.ReplyKeyboardRemove())
        await msg.delete()

        user_id = message.from_user.id
        text = "Славно! А теперь выбери страну (или несколько), в которой находишься. Пока могу предложить небольшой выбор. Но это временно 😉"
        await message.answer(text, reply_markup=inline_buttons.show_countries(user_id))
        await Reg.get_country.set()


    elif message.text == 'Исправить':
        text = "Упс, введи своё верное имя"
        await message.answer(text)
        await Reg.change_name.set()


@dp.message_handler(state=Reg.change_name)
async def process_change_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    user_id = message.from_user.id
    text = "Славно! А теперь выбери страну (или несколько), в которой находишься. Пока могу предложить небольшой выбор. Но это временно 😉"
    await message.answer(text, reply_markup=inline_buttons.show_countries(user_id))
    await Reg.next()


@dp.callback_query_handler(state=Reg.get_country)
async def process_get_country(c: types.CallbackQuery, state: FSMContext):
    country = c.data
    user_id = c.from_user.id
    
    if country == 'done':
        if db.get_selected_countries(user_id):
            await c.message.answer("Я не буду открывать тебе свой возраст, а вот тебе придётся. Введи его вот в таком формате: 21.")
            await Reg.get_age.set()
        else:
            await c.answer("Вы не выбрали город!")

    else:
        country_data = db.get_country(user_id, country)

        if country_data:
            db.del_country(user_id, country)
            await c.message.edit_reply_markup(inline_buttons.show_countries(user_id))
        
        else:
            async with state.proxy() as data:
                data['country'] = country   

            await c.message.edit_text("Ещё мне нужно знать, в каком ты городе. Ты можешь выбрать несколько городов для офлайн встреч, например",
                reply_markup=inline_buttons.show_places(country, user_id)
            )
            await Reg.next()


@dp.callback_query_handler(state=Reg.get_place)
async def process_get_place(c: types.CallbackQuery, state: FSMContext):
    country = c.data
    user_id = c.from_user.id

    if country == 'back':
        text = "Славно! А теперь выбери страну (или несколько), в которой находишься. Пока могу предложить небольшой выбор. Но это временно 😉"
        await c.message.edit_text(text, reply_markup=inline_buttons.show_countries(user_id))
        await Reg.previous()
    
    elif country == 'ДРУГОЕ':
        await c.message.answer("Да ладно! Что я пропустил? Окей, введи город в строке ниже. Пример: Эйлат")
        await Reg.get_place_by_hand.set()

    else:
        async with state.proxy() as data:
            ctry = data.get('country')

        response = inline_buttons.places.get(ctry) if inline_buttons.places.get(ctry) else ''
        if c.data in response:
            if not db.get_place(user_id, c.data):
                db.reg_country(user_id=user_id, country=ctry, place=c.data)
            else:
                db.del_place(user_id, c.data)
                
            await c.message.edit_reply_markup(inline_buttons.show_places(ctry, user_id))


@dp.message_handler(state=Reg.get_place_by_hand)
async def process_get_place_by_hand(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    place = message.text

    async with state.proxy() as data:
        country = data['country']


    db.reg_country(user_id=user_id, country=country, place=place)
    
    await message.answer("Я не буду открывать тебе свой возраст, а вот тебе придётся. Введи его вот в таком формате: 21.")
    await Reg.get_age.set()


@dp.message_handler(state=Reg.get_age)
async def process_get_age(message: types.Message, state: FSMContext):
    age = message.text

    if age.isdigit():
        async with state.proxy() as data:
            data['age'] = int(age)
        await message.answer("Расскажи, чем ты занимаешься?", reply_markup=keyboard_buttons.show_jobs())
        await Reg.next()
    
    else:
        await message.answer("Введи только цифрами!")
    

@dp.message_handler(state=Reg.get_job)
async def process_get_job(message: types.Message, state: FSMContext):
    job = message.text
    user_id = message.from_user.id

    if job == 'БЛОГЕР':
        await message.answer("Ты мог выбрать НАХЛЕБНИК. Только не обижайся, сегодня ретроградный меркурий", reply_markup=types.ReplyKeyboardRemove())

    elif job == 'НАХЛЕБНИК':
        await message.answer("Ты мог выбрать БЛОГЕР. Только не обижайся, сегодня ретроградный меркурий", reply_markup=types.ReplyKeyboardRemove())

    elif job == 'Avon':
        await message.answer("Скажи честно, тебя мама заставляет? Ладно, не отвечай!", reply_markup=types.ReplyKeyboardRemove())

    msg = await message.answer('ㅤ', reply_markup=types.ReplyKeyboardRemove())
    await msg.delete()
    await message.answer("Теперь выбери сферу или несколько.", reply_markup=inline_buttons.show_spheres(user_id))
    await Reg.next()


@dp.callback_query_handler(state=Reg.get_sphere)
async def process_get_sphere(c: types.CallbackQuery, state: FSMContext):
    sphere = c.data
    user_id = c.from_user.id

    if sphere == 'ДРУГОЕ':
        await c.message.answer("Что я упустил? Напиши одним словом, например, Спорт")
        await Reg.get_sphere_by_hand.set()
    
    elif sphere == 'done':
        await c.message.answer("Осталось совсем немного, хотя, некоторые мгновения имеют привкус вечности. Выбери свои увлечения, можно несколько.", 
            reply_markup=inline_buttons.show_emojis(user_id)
        )
        await Reg.get_emoji.set()

    else:
        async with state.proxy() as data:
            data['main_sphere'] = sphere
        await c.message.edit_text("Ну-ка уточни, можешь выбрать несколько:", reply_markup=inline_buttons.show_more_spheres(user_id, sphere))
        await Reg.next()


@dp.callback_query_handler(state=Reg.get_more_spheres)
async def process_get_more_spheres(c: types.CallbackQuery, state: FSMContext):
    sphere = c.data
    user_id = c.from_user.id

    async with state.proxy() as data:
        main_sphere = data['main_sphere']

    response = inline_buttons.show_more_spheres(user_id, main_sphere, sphere)

    if sphere == 'ДРУГОЕ':
        await Reg.other_in_search.set()
        await c.message.answer(response)    

    elif sphere == 'back':
        await c.message.edit_text("Теперь выбери сферу или несколько.", reply_markup=inline_buttons.show_spheres(user_id))
        await Reg.previous()
    
    else:
        if not db.get_direction(user_id, c.data):
            db.reg_sphere(user_id=user_id, sphere_name=main_sphere, direction_name=c.data)

            if response:
                await c.message.answer(response)    
        else:
            db.del_direction(user_id, c.data)
        await c.message.edit_reply_markup(reply_markup=inline_buttons.show_more_spheres(user_id, main_sphere))
        

@dp.message_handler(state=Reg.get_sphere_by_hand)
async def process_get_sphere_by_hand(message: types.Message, state: FSMContext):
    sphere = message.text
    user_id = message.from_user.id

    async with state.proxy() as data:
        data['main_sphere'] = sphere

    db.reg_sphere(user_id=user_id, sphere_name=sphere, direction_name=sphere)

    await message.answer("Осталось совсем немного, хотя, некоторые мгновения имеют привкус вечности. Выбери свои увлечения, можно несколько.", 
        reply_markup=inline_buttons.show_emojis(user_id)
    )
    await Reg.get_emoji.set() 


@dp.message_handler(state=Reg.other_in_search)
async def process_in_search(message: types.Message, state: FSMContext):
    direction = message.text
    user_id = message.from_user.id

    async with state.proxy() as data:
        main_sphere = data['main_sphere']
    
    db.reg_sphere(user_id=user_id, sphere_name=main_sphere, direction_name=direction)

    await message.answer("Осталось совсем немного, хотя, некоторые мгновения имеют привкус вечности. Выбери свои увлечения, можно несколько.", 
        reply_markup=inline_buttons.show_emojis(user_id)
    )
    await Reg.next()


@dp.callback_query_handler(state=Reg.get_emoji)
async def process_get_emoji(c: types.CallbackQuery, state: FSMContext):
    emoji = c.data
    user = c.from_user

    description = inline_buttons.show_emojis(user.id, emoji)
    await c.answer(description, show_alert=True)

    if emoji == 'done':
        await c.message.answer(
            'Знаешь, я внезапно понял одну вещь… Я уже столько знаю о тебе. Мы как семья, '
            'я — двоюродный дядя с причудами, который живёт в хижине чудес и о котором ты '
            'узнал только сегодня 🫀   Ты, возможно, уже хочешь познакомить меня со своими '
            'друзьями. Так не робей, пришли им ссылку и расскажи, как мы сблизились за короткое время.',
                reply_markup=inline_buttons.share()
        )

        await asyncio.sleep(2)

        await c.message.answer("Мы почти закончили. Давай я покажу тебе меню")
        await c.message.answer(
            "<b>ПРОФИЛЬ</b> — ни на что не намекаю, но здесь ты сможешь поменять личную информацию о себе. Допустим, скрываясь от повестки.\n\n"
            "<b>ПОДДЕРЖКА</b> — для связи с НИМ, с его светлостью разработчиком\n\n"
            "<b>НАСТРОЙКА</b> — ты, конечно, сможешь менять заданные ИМ настройки, но нужно ли тебе это?\n\n"
            "<a href='https://one-click.site/'>one-click</a> — шикарная возможность выделиться среди всех остальных. Козырнуть навыками, так сказать. А именно заиметь собственный лендинг по цене большого латте с ореховым топингом.",
                disable_web_page_preview=True,
                reply_markup=keyboard_buttons.main_menu()
        )

        async with state.proxy() as data:
            name = data.get('name') if data.get('name') else user.first_name
            age = data.get('age')

        db.reg_user(user.id, user.username, name, age)

        await state.finish()
    
    else:
        if not db.get_emoji(user.id, emoji):
            db.reg_emoji(user.id, emoji)
        
        else:
            db.del_emoji(user.id, emoji)
        
        await c.message.edit_reply_markup(reply_markup=inline_buttons.show_emojis(user.id))
