# Horoscope Bot
### Описание проекта:

**Horoscope Bot** - это телеграм бот для получения ежедневного гороскопа.

### Функционал телеграм бота:

<br>1. При регистрации бот предлагает пользователю выбрать свой знак зодиака. 
Используется ReplyKeyboardMarkup 3 ряда по 4 кнопки с эмоджи знака зодиака. 
После выбора знака бот присылает сообщение с информацией о выбранном знаке.

<br>2. После регистрации бот присылает гороскоп на сегодня. Сообщение 
включает себя текст, картинку и InlineKeyboardMarkup с одной кнопкой 
“Обновить”. Текст включает в себя дату гороскопа, выделенную жирным шрифтом. 
При нажатии на кнопку сообщение должно обновиться, и прогноз должен 
измениться на другой.

<br>3. Каждый день в 10 утра пользователь получает гороскоп на новый день 
(только в случае, если его еще нет).

<br>4. В меню бота есть команда “/update”, которая обновляет прогноз на 
сегодня (аналогично кнопке “Обновить” в сообщении) либо отправляет новое 
сообщение с гороскопом, если сообщения за сегодня по какой-то причине нет.

<br>5. Когда пользователь отправляет что-угодно в чат, бот пишет 
“Извините, я не понял”.

<br>6. Команда “/change_zodiac” в меню бота  - при нажатии появляется 
клавиатура, как при регистрации, и знак зодиака пользователя меняется на 
выбранный. Приходит новый гороскоп на сегодня.

<br>7. Команда “/clear_history” в меню бота - очищает историю сообщений, 
оставляя только сообщение с последним выбранным знаком зодиака.

### Стек технологий:

- Python
- aiogram

### Как запустить проект:

<br>1. Клонировать репозиторий и перейти в него в командной строке:

```
git clone "адрес клонируемого репозитория"
```

<br>2. В файле **config.py** впишите токен вашего телеграм бота.

<br>3. Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    venv\Scripts\activate
    ```

<br>4. Установить и обновить пакетный менеджер:

```
python -m pip install --upgrade pip
```

<br>5. Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

<br>6. Запустите телеграм бота:

```
python manage.py runserver
```

### Project's preview:
  
![](media/preview.gif)

### Автор проекта:

Семёнова Юлия (GitHub: JuliSem)