import asyncio
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db
from states.reg import Reg
from keyboards.inline import inline_buttons
from keyboards.default import keyboard_buttons



@dp.message_handler(content_types = 'document', state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer_video(message.document.file_id, width=1920, height=1020, supports_streaming=True)


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(f"Давай заполним твой профиль? Твоё имя {message.from_user.first_name}",
        reply_markup=keyboard_buttons.check_name()
    )
    await Reg.check_name.set()


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

    countries = ['georgia', 'israel']

    if country == 'done':
        await c.message.answer("Ещё мне нужно знать, в каком ты городе. Ты можешь выбрать несколько городов для офлайн встреч, например",
            reply_markup=inline_buttons.show_places(countries, user_id)
        )
        await Reg.next()

    else:
        pass


@dp.callback_query_handler(state=Reg.get_place)
async def process_get_country(c: types.CallbackQuery, state: FSMContext):
    place = c.data

    if place == 'ДРУГОЕ':
        await c.message.answer("Да ладно! Что я пропустил? Окей, введи город в строке ниже. Пример: Эйлат")
        await Reg.get_place_by_hand.set()
    
    elif place == 'done':
        await c.message.answer("Я не буду открывать тебе свой возраст, а вот тебе придётся. Введи его вот в таком формате: 21.")
        await Reg.next()


@dp.message_handler(state=Reg.get_place_by_hand)
async def process_get_place_by_hand(message: types.Message, state: FSMContext):
    await message.answer("Я не буду открывать тебе свой возраст, а вот тебе придётся. Введи его вот в таком формате: 21.")
    await Reg.get_age.set()


@dp.message_handler(state=Reg.get_age)
async def process_get_age(message: types.Message, state: FSMContext):
    age = message.text

    if age.isdigit():
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
        async with state.proxy() as data:
            data['main_sphere'] = sphere
        await c.message.answer("Ну-ка уточни, можешь выбрать несколько:", reply_markup=inline_buttons.show_more_spheres(user_id, sphere))
        await Reg.next()


@dp.callback_query_handler(state=Reg.get_more_spheres)
async def process_get_more_spheres(c: types.CallbackQuery, state: FSMContext):
    sphere = c.data
    user_id = c.from_user.id

    async with state.proxy() as data:
        main_sphere = data['main_sphere']

    response = inline_buttons.show_more_spheres(user_id, main_sphere, sphere)

    if response:
        if response == 'ДРУГОЕ':
            await Reg.other_in_search.set()

        await c.message.answer(response)

        # if response != 'ДРУГОЕ':
        #     await c.message.answer("Осталось совсем немного, хотя, некоторые мгновения имеют привкус вечности. Выбери свои увлечения, можно несколько.", 
        #         reply_markup=inline_buttons.show_emojis(user_id)
        #     )
        #     await Reg.get_emoji.set()

    elif sphere == 'done':
        await c.message.answer("Осталось совсем немного, хотя, некоторые мгновения имеют привкус вечности. Выбери свои увлечения, можно несколько.", 
            reply_markup=inline_buttons.show_emojis(user_id)
        )
        await Reg.get_emoji.set()


@dp.message_handler(state=Reg.get_sphere_by_hand)
async def process_get_sphere_by_hand(message: types.Message, state: FSMContext):
    sphere = message.text
    user_id = message.from_user.id

    async with state.proxy() as data:
        data['main_sphere'] = sphere

    await message.answer("Осталось совсем немного, хотя, некоторые мгновения имеют привкус вечности. Выбери свои увлечения, можно несколько.", 
        reply_markup=inline_buttons.show_emojis(user_id)
    )
    await Reg.get_emoji.set() 


@dp.message_handler(state=Reg.other_in_search)
async def process_in_search(message: types.Message, state: FSMContext):
    target = message.text
    user_id = message.from_user.id

    await message.answer("Осталось совсем немного, хотя, некоторые мгновения имеют привкус вечности. Выбери свои увлечения, можно несколько.", 
        reply_markup=inline_buttons.show_emojis(user_id)
    )
    await Reg.next()


@dp.callback_query_handler(state=Reg.get_emoji)
async def process_get_emoji(c: types.CallbackQuery, state: FSMContext):
    emoji = c.data
    user_id = c.from_user.id

    description = inline_buttons.show_emojis(user_id, emoji)
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