from aiogram import types, Dispatcher
from config import bot


async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Добро пожаловать,{message.from_user.first_name}\n'
                                f'Мы рады что выбрали нас!')



async def info_handler(message: types.Message):
    await message.answer(
        'Наш магазин представляет большой ассортимент одежды и обуви\n'
        'Бот создан для удобства наших клиентов❤️')



def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands='start')
    dp.register_message_handler(info_handler, commands='info')