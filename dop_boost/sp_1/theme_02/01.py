# 01

# Объявите функцию buy_sweeties в параметре money
# Посчитайте результат и напечатайте на экране фразу в соответствии с заданием


def buy_sweeties(money):
    chups = money // 5
    gums = (money - chups * 5) // 2
    print('На {money} руб. Вася может купить:'.format(money))
    print('Чупа Чупсов: {} шт.'.format(chups))
    print('Жевательных резинок: {} шт.'.format(gums))


buy_sweeties(13)
# На 13 руб. Вася может купить:
# Чупа Чупсов: 2 шт.
# Жевательных резинок: 1 шт.
buy_sweeties(1)
buy_sweeties(25)