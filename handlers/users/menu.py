from aiogram import types

from loader import dp, db


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
