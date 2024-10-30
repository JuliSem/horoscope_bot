from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.types import FSInputFile

from app.database import Database
from app.get_text_horoscope import get_text_horoscope
import app.keyboards as kb
from config import DATABASE_NAME, ZODIACS

async def send_horoscope_cron(bot: Bot):
    '''Функция для отправки гороскопа по расписанию каждый день.'''
    db = Database(DATABASE_NAME)
    all_telegram_id = db.select_all_telegram_id()
    if all_telegram_id:
        for id in all_telegram_id:
            zodiac = db.get_zodiac(id)
            zodiac = ZODIACS[zodiac]
            text = get_text_horoscope()
            gif_file = FSInputFile(path=f'./media/{zodiac}.gif')
            db.update_last_horoscope_date(id)
            await bot.send_animation(
                chat_id=id,
                animation=gif_file,
                caption=text,
                parse_mode=ParseMode.HTML,
                reply_markup=kb.update
            )
