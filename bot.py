import logging
import time
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

TOKEN = "7232339212:AAFy2TGTBDsEGw7lcY3eNbCUGSp1xBJub"
MSG = "Чи випив ти сьогодні вітамінки, {}"

# Створюємо екземпляри класів
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
scheduler = AsyncIOScheduler()


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=}{time.asctime()}')
    await message.reply(f'Привіт, {user_full_name}. Кожного ранку о 7 - я буду тобі нагадувати про прийом вітамінок.')

    # Додаємо завдання в планувальник
    scheduler.add_job(send_daily_reminder, CronTrigger(
        hour=7, minute=0), args=[user_id, user_name])


async def send_daily_reminder(user_id, user_name):
    await bot.send_message(user_id, MSG.format(user_name))

if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, skip_updates=True)
