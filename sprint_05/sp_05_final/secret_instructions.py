# Шифрованные инструкции. Финальное задание спринта 5.
import sys


def collect(line: list[str]) -> str:
    """Собираем основную часть инструкции."""
    result = []
    pos = 0
    while pos < len(line):
        if line[pos].isalpha():
            result.append(line[pos])
            pos += 1
            continue
        if line[pos] == '[':
            pos += 1
            continue
        if line[pos].isdigit():
            number = get_number(line[pos: pos + 3])
            pos += len(str(number)) 
            result.append(number)
            continue
        if line[pos] == ']':
            res = ''
            x = result.pop()
            while not isinstance(x, int):
                res = x + res
                x = result.pop()
            result.append(res * x)
            pos += 1
    return ''.join(result)


def get_number(line: str) -> int:
    res = line[0]
    if not line[1].isdigit():
        return int(res)
    if not line[2].isdigit():
        return int(res + line[1])
    return int(res + line[1] + line[2])


if __name__ == "__main__":
    data = sys.stdin.read().strip()
    print(collect(data))