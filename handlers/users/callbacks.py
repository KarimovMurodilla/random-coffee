from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, db
from keyboards.inline import inline_buttons


@dp.callback_query_handler(text_contains = 'info', state="*")
async def cancel_handler(c: types.CallbackQuery, state: FSMContext):
    await state.finish()


# @dp.inline_handler()
# async def my_orders(query: types.InlineQuery):	
# 	try:
# 		r = [types.InlineQueryResultPhoto( 
# 				id = '1', 
# 				photo_url = 'https://t.me/digestuz/17651',
# 				thumb_url = 'https://t.me/digestuz/17651'             
#                 )]
			
# 		await query.answer(r, cache_time = 60)
		
# 	except Exception as e:
# 		print(e)
