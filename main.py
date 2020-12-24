# Неиспользуемые импорты, нужно привести в порядок
import datetime as dt
import json


# Общее замечание: нужно привести код в соответствие с PEP8
# Правильно расставь переносы, пустые строки между классами и методами и пробелы.
# Этой придирке я научился у тех кто меня учил, но скоро ты поймешь
# что написанный по РЕР8 код гораздо легче читать. 
# Не отчаивайся, все будет хорошо =)
class Record:
    def __init__(self, amount, comment, date=''):
        self.amount=amount
        self.date = dt.datetime.now().date() if not date else dt.datetime.strptime(date, '%d.%m.%Y').date()
        self.comment=comment
class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records=[]
    def add_record(self, record):
        self.records.append(record)
    def get_today_stats(self):
        today_stats=0
        # Переменные не так именуются.
        for Record in self.records:
            if Record.date == dt.datetime.now().date():
                # Лучше было бы сделать это конкатенацией
                today_stats = today_stats+Record.amount
        return today_stats
    def get_week_stats(self):
        week_stats=0
        today = dt.datetime.now().date()
        for record in self.records:
            # Лучше вынести условия в отдельные переменные для лучшей читаемости.
            # У класса Record, кажется, можно достать дату из записи.
            # Так же стоит посмотреть как работает datetime.timedelta()
            if (today -  record.date).days <7 and (today -  record.date).days >=0:
                week_stats +=record.amount
        return week_stats
class CaloriesCalculator(Calculator):
    def get_calories_remained(self): # Получает остаток калорий на сегодня
        x=self.limit-self.get_today_stats()
        if x > 0:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {x} кКал'
        else:
            return 'Хватит есть!'
class CashCalculator(Calculator):
    # Комментарии должны начинать с # и пробела
    # Это целые числа, зачем их превращать во float?
    USD_RATE = float(60)  # Курс доллар США.
    EURO_RATE = float(70)  # Курс Евро.
    # Курсы валют лучше брать через self, не стоит их передавать
    # как переменную в функцию
    def get_today_cash_remained(self, currency, USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):
        currency_type = currency
        cash_remained = self.limit - self.get_today_stats()
        # Можно улучшить. Подумай как можно избавиться от первых трех if-ов и 
        # тем самым убрать дублирование.
        # Так же ветвления следует завершать условием else, как это 
        # сделано у тебя выше.
        if currency == 'usd':
            cash_remained /= USD_RATE
            currency_type = 'USD'
        elif currency_type == 'eur':
            cash_remained /= EURO_RATE
            currency_type = 'Euro'
        elif currency_type == 'rub':
            # Подумай что вернет эта строка и как она используется
            cash_remained == 1.00
            currency_type = 'руб'
        if cash_remained > 0:
            return f'На сегодня осталось {round(cash_remained, 2)} {currency_type}'
        elif cash_remained == 0:
            return 'Денег нет, держись'
        elif cash_remained < 0:
            return 'Денег нет, держись: твой долг - {0:.2f} {1}'.format(-cash_remained, currency_type)

    # Зачем это тут? У тебя родительский класс уже имеет этот метод.
    def get_week_stats(self):
        super().get_week_stats()
