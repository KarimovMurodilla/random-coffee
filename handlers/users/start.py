from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db
from states.reg import Reg
from keyboards.inline import inline_buttons
from keyboards.default import keyboard_buttons


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

    await c.message.answer("Ещё мне нужно знать, в каком ты городе. Ты можешь выбрать несколько городов для офлайн встреч, например",
        reply_markup=inline_buttons.show_places(country, user_id)
    )
    await Reg.next()


@dp.callback_query_handler(state=Reg.get_place)
async def process_get_country(c: types.CallbackQuery, state: FSMContext):
    place = c.data
    user_id = c.from_user.id

    if place == 'ДРУГОЕ':
        await c.message.answer("Да ладно! Что я пропустил? Окей, введи город в строке ниже. Пример: Эйлат")
        await Reg.get_place_by_hand.set()
    
    else:
        await c.message.answer("Я не буду открывать тебе свой возраст, а вот тебе придётся. Введи его вот в таком формате: 21.")
        await Reg.get_age.set()



@dp.message_handler(state=Reg.get_place_by_hand)
async def process_get_place_by_hand(message: types.Message, state: FSMContext):
    place = message.text

    await message.answer("Да ладно! Что я пропустил? Окей, введи город в строке ниже. Пример: Эйлат")
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
        await message.answer("Ты мог выбрать НАХЛЕБНИК. Только не обижайся, сегодня ретроградный меркурий")

    elif job == 'НАХЛЕБНИК':
        await message.answer("Ты мог выбрать БЛОГЕР. Только не обижайся, сегодня ретроградный меркурий")

    elif job == 'Avon':
        await message.answer("Скажи честно, тебя мама заставляет? Ладно, не отвечай!")


    await message.answer("Теперь выбери сферу или несколько.", reply_markup=inline_buttons.show_spheres(user_id))
    await Reg.next()


@dp.callback_query_handler(state=Reg.get_sphere)
async def process_get_country(c: types.CallbackQuery, state: FSMContext):
    sphere = c.data
    user_id = c.from_user.id

    await c.message.answer("Ну-ка уточни, можешь выбрать несколько:", reply_markup=inline_buttons.show_more_spheres(user_id, sphere))