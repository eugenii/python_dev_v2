# Неправильные горы 
from array import array
import sys



def valid_mountain_array(data: array) -> bool:
    valid = False
    if not data:
        return valid
    if len(data) < 3:
        return valid
    if data[0] > data[1]:
        return False
    pos = 1

    while pos < len(data) - 1:
        if data[pos] < data[pos + 1]:
            pos += 1
            continue
        elif data[pos] == data[pos + 1]:
            return valid
        else:
            valid = True
            pos +=1 
            break
    else:
        return valid
    while pos < len(data) - 1:
        if data[pos] <= data[pos + 1]:
            return False
        pos += 1
        continue

    return valid

     
data = array( 'i', map(int, sys.stdin.read().split()))

print(valid_mountain_array(data))

"""Решение от Google ИИ
Более эффективное - просто шагать сначала вверх, потом вниз.
в конце каждого цикла проверять где мы находимся (конец не конец).
"""
# import sys
# from array import array

# def valid_mountain_array(data: array) -> bool:
#     n = len(data)
#     if n < 3:
#         return False
    
#     pos = 0
    
#     # Шагаем строго вверх
#     while pos + 1 < n and data[pos] < data[pos + 1]:
#         pos += 1
        
#     # Проверяем, что вершина — не первый и не последний элемент
#     if pos == 0 or pos == n - 1:
#         return False
        
#     # Шагаем строго вниз
#     while pos + 1 < n and data[pos] > data[pos + 1]:
#         pos += 1
        
#     # Если дошли до конца массива, значит гора правильная
#     return pos == n - 1

# # Используем тип 'i' для защиты от больших чисел
# data = array('i', map(int, sys.stdin.read().split()))
# print(valid_mountain_array(data))
