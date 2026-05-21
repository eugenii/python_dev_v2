# Поик подстроки в строке

def max_unique_substring_len(s: str) -> str:

    # Словарь для хранения символов и идексов их последнего вхождения
    seen_chars = {}

    left = 0
    max_len = 0

    for right, char in enumerate(s):
        if char in seen_chars and seen_chars[char] >= left:
            left = seen_chars[char] + 1    # Смещаем СТРОГО за предидущее вхождение.
        
        seen_chars[char] = right   # Записываем индекс текущего символа

        # Счиатем длину окна
        max_len = max(max_len, right - left + 1)

    return max_len


if __name__ == '__main__':
    print(max_unique_substring_len(input()))