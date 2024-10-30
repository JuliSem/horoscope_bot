import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime

from app.apsched import send_horoscope_cron
from app.commands import set_commands
from app.handlers import (
    change_zodiac,
    choose_zodiac,
    clear_history,
    start,
    start_register,
    register_name,
    register_phone,
    dayly_horoscope,
    update_dayly_horoscope,
    unknown_command
)
from app.state import RegisterState
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.message.register(start, Command(commands='start'))
dp.message.register(start_register, F.text=='Зарегистрироваться в боте')
dp.message.register(register_name, RegisterState.regName)
dp.message.register(register_phone, RegisterState.regPhone)
dp.message.register(choose_zodiac, RegisterState.regZodiac)
dp.message.register(change_zodiac, Command(commands='change_zodiac'))
dp.message.register(dayly_horoscope, Command(commands='update'))
dp.callback_query.register(update_dayly_horoscope, F.data=='update')
dp.message.register(clear_history, Command(commands='clear_history'))
dp.message.register(unknown_command)

scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
scheduler.add_job(
    send_horoscope_cron,
    trigger='cron',
    start_date=datetime.now(),
    hour=10,
    kwargs={'bot': bot}
)

async def main():
    scheduler.start()
    await set_commands(bot)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
