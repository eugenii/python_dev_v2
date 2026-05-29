# Проект С.Ч.И.Т.А.Л.К.А.


def scitalka(pretenders, takt):
    pos = 0
    while len(pretenders) > 1:
        pos = (pos + takt % len(pretenders) - 1) % len(pretenders)
        pretenders.pop(pos)

    return pretenders[0]


def schitalka_recursive(pretenders, takt, pos=0):
    if len(pretenders) == 1:
        return pretenders[0]
    pos = (pos + takt % len(pretenders) - 1) % len(pretenders)
    pretenders.pop(pos)
    return schitalka_recursive(pretenders, takt, pos=pos)
    
# Решение через формулу Иосифа Флавия (от Google AI)

def josephus(n: int, k: int) -> int:
    # Базовый случай: если остался 1 человек, он гарантированно побеждает (номер 1)
    if n == 1:
        return 1
    
    # Рекурсивный шаг по формуле Флавия
    return (josephus(n - 1, k) + k - 1) % n + 1


if __name__ == '__main__':
    # pretenders = list(range(1, int(input()) + 1))
    # print(schitalka_recursive(pretenders, int(input())))
    