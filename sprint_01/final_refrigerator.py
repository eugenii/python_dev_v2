# Финальное задание "Холодильник"
from decimal import Decimal
import datetime

DATE_FORMAT = '%d.%m.%Y'


def add(items, title, amount, expiration_date=None):
    if expiration_date:
        expiration_date = datetime.datetime.strptime(expiration_date, DATE_FORMAT).date()
    if title in items:
        items[title].append({'amount': Decimal(amount), 'expiration_date': expiration_date})
    else:
        items[title] = [{'amount': Decimal(amount), 'expiration_date': expiration_date}]


def add_by_note(items, note):
    ...


def find(items, needle):
    ...


def get_amount(items, needle):
    ...


def get_expired(items, in_advance_days=0):
    ...


goods = {
    'Пельмени Универсальные': [
        # Первая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('0.5'), 'expiration_date': datetime.date(2023, 7, 15)},
        # Вторая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 1)},
    ],
    'Вода': [
        {'amount': Decimal('1.5'), 'expiration_date': None}
    ],
}


add(goods, "Cabbage", '1.1', expiration_date='12.08.1975')

print(*goods)
print(goods['Cabbage'])