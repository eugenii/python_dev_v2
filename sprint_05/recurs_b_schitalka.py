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
    


if __name__ == '__main__':
    pretenders = list(range(1, int(input()) + 1))
    print(schitalka_recursive(pretenders, int(input())))