import sys


def decode_instructions(compressed_str: str) -> str:
    """Расшифровывает сжатую строку инструкций марсохода."""
    stack: list[tuple[str, int]] = []
    current_str: str = ""
    current_num: int = 0

    for char in compressed_str:
        if char.isdigit():
            # Собираем число посимвольно (работает для любой разрядности: 1, 10, 300)
            current_num = current_num * 10 + int(char)
        elif char == '[':
            # Сохраняем накопленную строку и число в стек, чтобы заняться вложенной частью
            stack.append((current_str, current_num))
            # Сбрасываем текущие рабочие переменные
            current_str = ""
            current_num = 0
        elif char == ']':
            # Достаем из стека родительскую строку и коэффициент умножения
            prev_str, num = stack.pop()
            # Раскрываем текущие скобки и приклеиваем к родительской строке
            current_str = prev_str + current_str * num
        else:
            # Если это просто буква — добавляем к текущей строке
            current_str += char

    return current_str


if __name__ == "__main__":
    # Считываем строку, очищая от лишних пробелов и переносов
    input_data: str = sys.stdin.read().strip()
    print(decode_instructions(input_data))