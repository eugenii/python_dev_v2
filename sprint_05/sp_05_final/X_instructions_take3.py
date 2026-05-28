# Финальное задание спринта 5 "Шифрованные инструкции"
# Yandex context solution ID 162602342  (new)
import sys
 
NUMBERS = set('0123456789')

def decode_instructions(instructions: str) -> str:
    """Расшифровывает сжатую строку инструкций марсохода.
    Args: 
    stack: list для хранения промежуточных (вложенных) частей.
    current_result: str для хранения текущей собираемой строки.
    current_num: int  для хранения текущего числа повторений строки. 

    Returns: 
    current_result: str  возвращаемая расшифрованная строка.
    """
 
    stack: list[tuple[str, int]] = []
    current_result: str = ""
    current_num: str = ''
    for symb in instructions:
        if symb in NUMBERS:
            current_num = current_num + symb
        elif symb == '[':
            stack.append((current_result, int(current_num)))
            current_result = ''
            current_num = ''
        elif symb == ']':
            prev_str, num = stack.pop()
            current_result = prev_str + current_result * num
        else:
            current_result += symb
    return current_result
 

if __name__ == "__main__":
    input_data: str = sys.stdin.read().strip()
    print(decode_instructions(input_data))
