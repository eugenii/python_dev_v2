# Разворот строки рекурсивно

def reverse_string(s: str) -> str:

    # Защита: если передали не строку, выбрасываем TypeError
    if not isinstance(s, str):
        raise TypeError("Входные данные должны быть строкой!")
    if s == '':
        return s
    return reverse_string(s[1:]) + s[0]


print(reverse_string('hello'))



#  Не лучший вариант для решения задачи - склейка на каждом уровне рекурсии - плохо.
# def reverse_string2(s: str) -> str:
#     if len(s) == 0:
#         return s
#     return s[-1] + reverse_string2(s[:-1])
