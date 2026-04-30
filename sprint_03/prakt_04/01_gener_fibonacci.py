# Генератор чисел Фибоначчи

def fibonacci(n):
    # Допишите функцию.
    a, b = 0, 1  # начальные значения последовательности
    for _ in range(n):  # генерируем n чисел
        yield a  # возвращаем текущее число
        a, b = b, a + b


sequence = fibonacci(10)
for number in sequence:
    print(number)