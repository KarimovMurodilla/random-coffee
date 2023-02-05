from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db
from states.reg import Reg
from keyboards.default import keyboard_buttons


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    user = message.from_user

    if not db.get_user(user.id):
        await message.answer(f"Давай заполним твой профиль? Твоё имя {message.from_user.first_name}",
            reply_markup=keyboard_buttons.check_name()
        )
        await Reg.check_name.set()
    
    else:
        user = db.get_user(user.id)
        await message.answer(f"Привет {user.name}!", reply_markup=keyboard_buttons.main_menu())