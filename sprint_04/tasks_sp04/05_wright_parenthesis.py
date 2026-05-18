# Правильные скобочные последовательности

def is_correct_bracket_seq(seq: str) -> bool:
    opens = {'(': -3, '[': -2, '{': -1}
    closes = {')': 3, ']': 2, '}': 1}
    stack = []
    for char in seq:
        if char in opens:
            stack.append(opens[char])
        elif char in closes:
            if not stack or stack[-1] + closes[char] != 0:
                return False
            stack.pop()
    return not stack


seq = input()
print(is_correct_bracket_seq(seq))