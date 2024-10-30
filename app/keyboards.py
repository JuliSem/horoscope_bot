from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup
)

register_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(
            text='Зарегистрироваться в боте'
        )],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Для продолжения нажмите на кнопку ниже'
)

zodiac = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='♈'),
         KeyboardButton(text='♊'),
         KeyboardButton(text='♉'),
         KeyboardButton(text='♋')],
        [KeyboardButton(text='♌'),
         KeyboardButton(text='♍'),
         KeyboardButton(text='♎'),
         KeyboardButton(text='♏')],
        [KeyboardButton(text='♐'),
         KeyboardButton(text='♑'),
         KeyboardButton(text='♒'),
         KeyboardButton(text='♓')],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Выберите нужный знак зодиака ниже'
)

update = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text='Обновить',
            callback_data='update'
        )],
    ]
)
