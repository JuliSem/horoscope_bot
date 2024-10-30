from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Запустить бота'
        ),
        BotCommand(
            command='update',
            description='Обновить гороскоп'
        ),
        BotCommand(
            command='change_zodiac',
            description='Поменять знак зодиака'
        ),
        BotCommand(
            command='clear_history',
            description='Очистить историю сообщений'
        )
    ]
    await bot.set_my_commands(
        commands=commands,
        scope=BotCommandScopeDefault()
    )
