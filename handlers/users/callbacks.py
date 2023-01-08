from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, mail, db
from states.ask import Ask
from keyboards.inline import inline_buttons


@dp.callback_query_handler(text_contains = 'info', state="*")
async def cancel_handler(c: types.CallbackQuery, state: FSMContext):
    await state.finish()

    await c.answer()
    await c.message.answer("Ознакомьтесь здесь: https://telegra.ph/Glavnaya-01-08", disable_web_page_preview=True)


@dp.callback_query_handler(text_contains = 'question', state="*")
async def cancel_handler(c: types.CallbackQuery, state: FSMContext):
    await state.finish()

    await c.answer()
    await c.message.answer("Напишите вопрос, а я передам его :)")
    await Ask.step1.set()


@dp.message_handler(state=Ask.step1)
async def cancel_handler(message: types.Message, state: FSMContext):
    user_info = db.get_user(message.from_user.id)

    mail.send_mail(
        subject = "New question", 
        text_part = f"[{user_info.contact}]: {message.text}"
    )
    
    await message.answer("Отправлен ✅")
    await state.finish()