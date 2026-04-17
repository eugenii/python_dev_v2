# Финальное задание "Холодильник"
from decimal import Decimal
import datetime

DATE_FORMAT = '%Y-%m-%d'


def add(items, title, amount, expiration_date=None):
    if expiration_date:
        expiration_date = datetime.datetime.strptime(expiration_date, DATE_FORMAT).date()
    if title in items:
        items[title].append({'amount': Decimal(amount), 'expiration_date': expiration_date})
    else:
        items[title] = [{'amount': Decimal(amount), 'expiration_date': expiration_date}]


def add_by_note(items, note):
    note = note.split()
    try:
        datetime.datetime.strptime(note[-1], DATE_FORMAT)
        expiration_date = note[-1]
        amount = Decimal(note[-2])
        title = ' '.join(note[:-2])
    except ValueError:
        expiration_date = None
        amount = Decimal(note[-1])
        title = ' '.join(note[:-1])
    add(items, title, amount, expiration_date)


def find(items, needle):
    result = []
    for title in items:
        if needle in title.lower():
            result.append(title)
    # result = [item for item in items.keys() if needle in item.lower()]
    return result


def get_amount(items, needle):
    result = Decimal('0')
    for item in items:
        if needle.lower() in item.lower():
            for part in items[item]:
                result += part['amount']
    return result


def get_expired(items, in_advance_days=0):
    result = {}
    exp_datetime = datetime.datetime.now() + datetime.timedelta(days=in_advance_days)
    exp_date = exp_datetime.date()
    for item in items:
        for part in items[item]:
            if part['expiration_date']:
                if part['expiration_date'] <= exp_date:
                    if item in result:
                        result[item] += part['amount']
                    else:
                        result[item] = part['amount']
    return list(result.items())


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


add(goods, "Cabbage", '1.1', expiration_date='2006-08-12')
add_by_note(goods, 'Яйца гусиные 4 2023-07-15')
add_by_note(goods, 'Макароны 1.5')
print(*goods)
print(goods['Cabbage'])
print(find(goods, 'пель'))
print(get_amount(goods, 'пель'))
add_by_note(goods, 'просто пельмени 0.5 2023-07-15')
print(find(goods, 'пель'))
print("==================")
print(get_expired(goods, 10))