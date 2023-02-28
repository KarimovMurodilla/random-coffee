import asyncio
import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, db
from keyboards.default import keyboard_buttons
from keyboards.inline import inline_buttons
from states.generic import Questions, NoQuestions


# If user have a questions
@dp.message_handler(state=Questions.step1)
async def process_questions(message: types.Message):
    text = message.text

    if text == "Пропущу":
        msg = await message.answer('ㅤ', reply_markup=types.ReplyKeyboardRemove())
        await msg.delete()

        await message.answer("Ну вот, мы же только начали. Когда я смогу снова написать тебе?",
            reply_markup = inline_buttons.date_btns()
        )
        await Questions.next()

    elif text == "Поехали":
        await message.answer("Уже в среду я пришлю тебе собеседника, и ты сможешь договориться с ним о встрече.")
        await NoQuestions.step2.set()


@dp.callback_query_handler(state=Questions.step2)
async def get_next_notification_date(c: types.CallbackQuery, state: FSMContext):    
    await c.message.delete()
    await c.message.answer("Хорошо, тогда до встречи!")

    deltas = {
        '1_week': datetime.timedelta(weeks=1),
        '2_weeks': datetime.timedelta(weeks=2),
        '3_weeks': datetime.timedelta(weeks=3),
        '1_month': datetime.timedelta(days=31)
    }

    now = datetime.datetime.now()
    scheduled_date = now + deltas[c.data]

    await db.reg_new_schedule_date(
        user_id = c.from_user.id,
        trigger = c.data,
        scheduled_date = scheduled_date
    )

    await state.finish()


# If user haven't any questions
@dp.message_handler(text="Поехали", state=NoQuestions.step1)
async def process_no_questions(message: types.Message, state: FSMContext):
    await message.answer("Уже в среду я пришлю тебе собеседника, и ты сможешь договориться с ним о встрече.",
        reply_markup=types.ReplyKeyboardRemove()
    )

    await asyncio.sleep(1)
    msg = await message.answer("3")
    
    for i in range(2, -1, -1):
        i = '🚀' if i == 0 else i        
        await asyncio.sleep(2)
        await msg.edit_text(str(i))

    await asyncio.sleep(1)
    await message.answer("Только не думай, что мы сейчас куда-то полетим. Я же сказал, жди среды. Пришлю ссылку на собеседника.")