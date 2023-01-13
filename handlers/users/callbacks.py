from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, db
from keyboards.inline import inline_buttons


@dp.callback_query_handler(text_contains = 'info', state="*")
async def cancel_handler(c: types.CallbackQuery, state: FSMContext):
    await state.finish()