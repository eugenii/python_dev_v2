import datetime

FORMAT = '%d.%m.%Y'


def validate_record(name: str, birthdate: str) -> bool:
    # Напишите код, верните булево значение.
    try:
        date = datetime.datetime.strptime(birthdate, FORMAT)
    except ValueError:
        return False
    return True


def process_people(entries: list[tuple]) -> dict:
    # Объявите счётчики.
    good_count = 0
    bad_count = 0
    # Распакуйте кортежи из полученного списка entries.
    # Каждую пару значений передайте в validate_record(),
    # чтобы проверить корректность формата даты рождения.
    # В зависимости от результата проверки увеличьте один из счётчиков.
    for name, birthdate in entries:
        if validate_record(name, birthdate):
            good_count += 1
        else:
            bad_count += 1
            print('Некорректный формат даты в записи: {}, {}'.format(name, birthdate))
    # Верните словарь.
    return dict([('good', good_count), ('bad', bad_count)])


data = [
    ('Акакій Башмачкинъ',    '23 марта 1791 года'),
    ('Яков Степанов', 'Двадцать шестое июля 1971'),
    ('Потап Алексеев', '16.09.1990'),
    ('Евгений Женин', '5 декабря 1984'),
    ('Кондрат Александров', '18.01.1994')
] 
statistics = process_people(data)
print(f'Корректных записей: {statistics["good"]}')
print(f'Некорректных записей: {statistics["bad"]}')