from aiogram import executor
import logging
from handlers import (commands,echo, FSMproducts)
from config import dp, Admins, bot
from db import main_db
import buttons

async def on_startup(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin, text='Здраствуйте хозяин !', reply_markup=buttons.start)
        await main_db.create_table()


async def on_shutdown(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin, text='До встречи хозяин!')


commands.register_handlers(dp)
FSMproducts.register_handlers(dp)






# ===============================================================================
echo.register_handlers(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)