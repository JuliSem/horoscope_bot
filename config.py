TOKEN='вставьте здесь токен вашего телеграм бота'
DATABASE_NAME = 'horoscope_bot.db'

ZODIACS = {
    '♈': 'oven',
    '♊': 'bliznec',
    '♉': 'telec',
    '♋': 'rak',
    '♌': 'lev',
    '♍': 'deva',
    '♎': 'vesy',
    '♏': 'skorpion',
    '♐': 'strelec',
    '♑': 'kozerog',
    '♒': 'vodoley',
    '♓': 'ryby',
}

HOROSCOPES = [
    'Вы будете энергичны и решительны, что поможет добиться впечатляющих '
      'результатов.',
    'У вас отлично получается располагать к себе людей. Ваше добродушие '
      'не останется незамеченным окружающими и поможет решить многие '
      'проблемы в вашу пользу.',
    'Вас ожидает удачный день. Вы справитесь со множеством трудных задач '
      'без особых усилий. Появится возможность проявить себя с лучшей '
      'стороны, укрепить свой авторитет в глазах коллег и руководства.',
    'Сегодня подходящий день для того, чтобы решиться на смелый поступок! '
      'Возможно пришло время расширить свои горизонты и начать новое '
      'увлекательное хобби или планировать путешествие.',
    'Сегодня можно отключить будильник и поспать подольше – нужно дать себе '
      'передышку. А вот браться за сложное лучше после полудня – тогда у вас '
      'будет достаточно сил. Все вокруг будет искушать отвлечься от '
      'действительно важных дел, не поддавайтесь.',
    'Сегодня вы удачливы как никогда. Успех будет поджидать за каждым углом, '
      'так что есть смысл браться за сложные и важные дела – добьетесь своего '
      'быстро. Рекламируйте себя везде и всюду – вы обязательно наткнетесь на '
      'комплименты и лакомые предложения.',
    'Сегодня будет непросто двигаться вперед – на вашем пути могут то и дело '
      'вырастать тупики. Разбивайте их в пух и прах настойчивостью и точно '
      'добьетесь своего. Перепроверяйте работу и документы – где-то может '
      'скрываться фатальная ошибка.',
    'День обещает быть насыщенным, вы на всё будете смотреть с интересом. '
      'Это, кстати, вдохновит на новые дела и победы. Главное – '
      'не стесняться. Сегодня вечером можно сходить на свидание или устроить '
      'его – вам будет приятно пообщаться с симпатичным человеком, да и время '
      'вы проведете классно.',
    'Cегодня вы можете почувствовать прилив гармонии и стремление к балансу '
      'во всех аспектах вашей жизни. Используйте этот день для того, чтобы '
      'аккуратно выстроить мосты между вашими желаниями и потребностями '
      'окружающих, особенно на работе и в личных связях.',
    'Не бойтесь следовать за вызовами, которые будоражат ваше сердце – они '
      'могут привести к неожиданным и радостным открытиям.'
]
