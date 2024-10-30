import sqlite3

from datetime import datetime


class Database():
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_db()

    def create_db(self):
        '''Создание таблицы users.'''
        try:
            query = (
                'CREATE TABLE IF NOT EXISTS users('
                'id INTEGER PRIMARY KEY,'
                'user_name TEXT,'
                'user_phone TEXT,'
                'user_zodiac TEXT,'
                'telegram_id INTEGER,'
                'last_horoscope_date DATE,'
                'zodiac_message_id INTEGER);'

            )
            self.cursor.execute(query)
            self.connection.commit()
        except sqlite3.Error as Error:
            print('Ошибка при создании таблицы: ', Error)

    def add_user(self, user_name, user_phone, user_zodiac, telegram_id):
        '''Добавление нового пользователя.'''
        query = (
            'INSERT INTO users(user_name, user_phone, user_zodiac, telegram_id) '
            'VALUES (?, ?, ?, ?);'
        )
        self.cursor.execute(
            query,
            (user_name, user_phone, user_zodiac, telegram_id)
        )
        self.connection.commit()
    
    def update_last_horoscope_date(self, telegram_id):
        '''Обновление данных о дате последнего сообщения с гороскопом.'''
        query = (
            'UPDATE users SET last_horoscope_date = ? WHERE telegram_id = ?'
        )
        last_horoscope_date = datetime.now().strftime('%d.%m.%Y')
        self.cursor.execute(query, (last_horoscope_date, telegram_id))
        self.connection.commit()
    
    def update_zodiac_message_id(self, zodiac_message_id, telegram_id):
        '''Обновление данных об id сообщения с выбранным знаком зодиака.'''
        query = (
            'UPDATE users SET zodiac_message_id = ? WHERE telegram_id = ?'
        )
        self.cursor.execute(query, (zodiac_message_id, telegram_id))
        self.connection.commit()

    def get_zodiac_message_id(self, telegram_id):
        '''Получение данных об id сообщения с выбранным знаком зодиака.'''
        query = ('SELECT zodiac_message_id FROM users WHERE telegram_id = ?')
        user = self.cursor.execute(query, (telegram_id, ))
        return user.fetchone()[0]

    def select_user(self, telegram_id):
        '''Извлекает данные пользователя по его telegram_id.'''
        query = ('SELECT * FROM users WHERE telegram_id = ?')
        user = self.cursor.execute(query, (telegram_id, ))
        return user.fetchone()
    
    def select_all_telegram_id(self):
        '''Получение всех telegram_id пользователей '''
        '''для отправки гороскопов в определенное время.'''
        query = ('SELECT telegram_id FROM users WHERE last_horoscope_date <> ?')
        date = datetime.now().strftime('%d.%m.%Y')
        all_telegram_id = self.cursor.execute(query, (date, ))
        return all_telegram_id.fetchone()
    
    def get_zodiac(self, telegram_id):
        '''Получение данных о знаке зодиака по telegram_id пользователя.'''
        query = ('SELECT user_zodiac FROM users WHERE telegram_id = ?')
        zodiac = self.cursor.execute(query, (telegram_id, ))
        return zodiac.fetchone()[0]
    
    def change_zodiac(self, user_zodiac, telegram_id):
        '''Обновление данных о знаке зодиака.'''
        query = ('UPDATE users SET user_zodiac = ? WHERE telegram_id = ?')
        self.cursor.execute(query, (user_zodiac, telegram_id))
        self.connection.commit()

    def __del__(self):
        '''Закрытие соединения.'''
        self.cursor.close()
        self.connection.close()
