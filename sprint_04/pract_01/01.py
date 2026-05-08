def list_superset(list_set_1, list_set_2):
    # Не меняйте названия функции и параметров. Напишите решение здесь.
    big, small = None, None
    flag = False
    if len(list_set_1) >= len(list_set_2):
        big = list_set_1
        small = list_set_2
    elif len(list_set_1) < len(list_set_2):
        big = list_set_2
        small = list_set_1
    for elt in small:
        if elt in big:
            continue
        flag = True
        break
    else:
        if len(big) == len(small):
            return 'Наборы равны.'
        else:
            return f'Набор {big} - супермножество.'
    # if not flag:
    return 'Супермножество не обнаружено.'
        




# Примеры для проверки функции.
list_set_1 = [1, 3, 5, 7]
list_set_2 = [3, 5]
list_set_3 = [5, 3, 7, 1]
list_set_4 = [5, 6]

print(list_superset(list_set_1, list_set_2))
print(list_superset(list_set_2, list_set_3))
print(list_superset(list_set_1, list_set_3))
print(list_superset(list_set_2, list_set_4))