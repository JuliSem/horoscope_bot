import re

from aiogram import Bot, F
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramBadRequest
from aiogram import Router
from aiogram.fsm.context import FSMContext 
from aiogram.types import Message, FSInputFile, CallbackQuery

from app.database import Database
from app.get_text_horoscope import get_text_horoscope
import app.keyboards as kb
from app.state import RegisterState
from config import DATABASE_NAME, ZODIACS

router = Router()

async def start(message: Message, bot: Bot):
    '''Команда старт.'''
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Привет!😀👋🏻 Это Гороскоп-бот!\n'
             'Здесь Вы можете узнать свой ежедневный гороскоп🔮\n'
             'Нажмите кнопку "Зарегистрироваться в боте", '
             'если в первый раз тут либо интересующую опцию в меню.',
        reply_markup=kb.register_keyboard
    )

async def start_register(message: Message, state: FSMContext, bot: Bot):
    db = Database(DATABASE_NAME)
    user = db.select_user(message.from_user.id)
    if user:
        await bot.send_message(
            chat_id=message.from_user.id,
            text=f'{user[1]}, Вы уже зарегистрированы!'
        )
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text=f'Давайте начнём регистрацию!\n'
                  'Для начала скажите, как Вас зовут?'
        )
        await state.set_state(state=RegisterState.regName)

async def register_name(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f'Приятно познакомиться {message.text}!\n'
              'Теперь укажите Ваш номер телефона'
              'Формат ввода: +7XXXXXXXXXX'
    )
    await state.update_data(regname=message.text)
    # установим состояние ожидания ввода телефона пользователя
    await state.set_state(state=RegisterState.regPhone)

async def register_phone(message: Message, state: FSMContext, bot: Bot):
    if (re.findall('^\+?[7][-\(]?\d{3}\)?-?\d{3}-?\d{2}-?\d{2}$', message.text)):
        await bot.send_message(
            chat_id=message.from_user.id,
            text='Номер телефона успешно добавлен!\n'
                 'Теперь выберите свой знак зодиака😌',
            reply_markup=kb.zodiac
        )
        await state.update_data(regphone=message.text)
        await state.set_state(state=RegisterState.regZodiac)
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text='Номер указан в неверном формате!\n'
                 'Попробуйте снова.'
        )

async def choose_zodiac(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(regzodiac=message.text)
    db = Database(DATABASE_NAME)
    user = db.select_user(message.from_user.id)
    if user:
        db.change_zodiac(message.text, message.from_user.id)
        msg = await bot.send_message(
            chat_id=message.from_user.id,
            text=f'{user[1]}, Ваш знак зодиака успешно обновлён на '
                 f'{message.text}!😌'
        )
        db.update_zodiac_message_id(msg.message_id, message.from_user.id)
    else:
        reg_data = await state.get_data()
        reg_name = reg_data.get('regname')
        reg_phone = reg_data.get('regphone')
        reg_zodiac = reg_data.get('regzodiac')
        msg = await bot.send_message(
            chat_id=message.from_user.id,
            text=f'Спасибо за регистрацию, {reg_name}!🤗\n'
                 f'Ваш знак зодиака: {reg_zodiac}'
            )
        db.add_user(reg_name, reg_phone, reg_zodiac, message.from_user.id)
        db.update_zodiac_message_id(msg.message_id, message.from_user.id)
    await state.clear()
    await dayly_horoscope(message=message, bot=bot)

async def change_zodiac(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Выберите нужный знак зодиака😌',
        reply_markup=kb.zodiac
    )
    await state.set_state(state=RegisterState.regZodiac)

async def dayly_horoscope(message: Message, bot: Bot):
    db = Database(DATABASE_NAME)
    zodiac = db.get_zodiac(message.from_user.id)
    zodiac = ZODIACS[zodiac]
    text = get_text_horoscope()
    gif_file = FSInputFile(path=f'./media/{zodiac}.gif')
    db.update_last_horoscope_date(message.from_user.id)
    await bot.send_animation(
        chat_id=message.from_user.id,
        animation=gif_file,
        caption=text,
        parse_mode=ParseMode.HTML,
        reply_markup=kb.update
    )

async def update_dayly_horoscope(callback_query: CallbackQuery):
    updated_text = get_text_horoscope()
    await callback_query.message.edit_caption(
        caption=updated_text,
        reply_markup=kb.update,
        parse_mode=ParseMode.HTML,
    )

async def clear_history(message: Message, bot: Bot):
    db = Database(DATABASE_NAME)
    user = db.select_user(message.from_user.id)
    if user:
        last_message_id = db.get_zodiac_message_id(message.from_user.id)
        try:
            for i in range(message.message_id, 0, -1):
                if i != last_message_id:
                    await bot.delete_message(
                        chat_id=message.from_user.id, message_id=i
                    )
                else:
                    await message.answer(
                        text='История сообщений очищена, оставлено последнее '
                             'сообщение с вашим знаком зодиака.'
                    )
        except TelegramBadRequest as ex:
            if ex.message == 'Bad Request: message to delete not found':
                print('Некоторые сообщения уже удалены или не найдены.')
            else:
                print(f'Ошибка при удалении сообщения: {ex}')
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text='Не удалось найти вашу информацию.'
        )

async def unknown_command(message: Message, bot: Bot):
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Извините, я не понял.'
    )
