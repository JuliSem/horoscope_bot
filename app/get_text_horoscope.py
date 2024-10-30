import random

from datetime import datetime

from config import HOROSCOPES

def get_text_horoscope():
    date = datetime.now().strftime('%d.%m.%Y')
    horoscope = random.choice(HOROSCOPES)
    text = f'<b>Гороскоп на {date}</b>\n{horoscope}'
    return text
