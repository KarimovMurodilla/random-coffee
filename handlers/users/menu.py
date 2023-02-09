import asyncio
from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, db, bot
from data.config import ADMINS
from states.generic import Support, Settings, OneClick, Questions, NoQuestions
from keyboards.default import keyboard_buttons


# ----PROFILE----
@dp.message_handler(text = 'Профиль')
async def show_profile(message: types.Message):
    user = message.from_user
    user_data = db.get_user_data(user.id)

    await message.answer(
        f"<b>Сфера:</b> {' '.join([obj.name for obj in user_data.sphere])}\n"
        f"<b>Город:</b> {' '.join([obj.name for obj in user_data.place])}\n"
        f"<b>Имя:</b> {user_data.user.name}\n"
        f"<b>Возраст:</b> {user_data.user.age}\n"
        f"<b>Страна:</b> {' '.join([obj.name for obj in user_data.country])}\n"
        f"<b>Занятия:</b> {' '.join([obj.emoji for obj in user_data.emoji])}\n"
        f"<b>Интересы:</b> {' '.join([obj.name for obj in user_data.direction])}\n"
    )


# ----SUPPORT----
@dp.message_handler(text = "Поддержка", state = '*')
async def support(message: types.Message):
    await message.answer("Напиши сюда свои горести и радости. Я передам ЕМУ", reply_markup = types.ReplyKeyboardRemove())
    await Support.get_question.set()


@dp.message_handler(state = Support.get_question)
async def process_question(message: types.Message, state: FSMContext):
    for admin in ADMINS:
        await bot.send_message(admin, message.text)
    
    await message.answer("Твое сообщение доставлено к админам ✅")
    await state.finish()


# ----SETTINGS----
@dp.message_handler(text = "Настройки")
async def settings(message: types.Message):
    await message.answer("Выбирай:", reply_markup=keyboard_buttons.settings_menu())
    await Settings.get_buttons.set()


@dp.message_handler(state = Settings.get_buttons)
async def process_settings(message: types.Message, state: FSMContext):
    text = message.text

    if text == "Остановить бота":
        await message.answer("Test", reply_markup = types.ReplyKeyboardRemove())
        await state.finish()
    
    elif text == "Настройка уведомлений":
        await message.answer("Test", reply_markup = types.ReplyKeyboardRemove())
        await state.finish()


# ----ONE CLICK----
@dp.message_handler(text = "one-click")
async def info_one_click(message: types.Message):
    await message.answer("Крутой digital-сервис, который поможет рассказать о твоей индивидуальности, чтобы не только друзей находить, но и клиентов, и партнёров, и вообще!")
    await asyncio.sleep(2)
    await message.answer(
        "Теперь я отправляюсь собирать для тебя собеседников. Если остались вопросы, нажми кнопку ниже.", 
            reply_markup = keyboard_buttons.one_click_menu()
    )

    await OneClick.any_questions.set()


@dp.message_handler(state = OneClick.any_questions)
async def process_one_click(message: types.Message, state: FSMContext):
    text = message.text

    if text == "Вопросы":
        await message.answer("Вижу, у тебя остались вопросы. Тогда тебе нужна команда ПОДДЕРЖКА Или нажми кнопку ПОЕХАЛИ, если вопрос отпал",
            reply_markup=keyboard_buttons.skip_or_support()
        )
        await Questions.step1.set()

    elif text == "Вопросов нет":
        await message.answer("А ты сообразительный собеседник!", reply_markup=keyboard_buttons.lets_go_btn())
        await NoQuestions.step1.set()