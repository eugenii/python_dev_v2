# Индекс для вставки. (Бинарный поиск)
import sys


def solve(probs: list, target: int) -> int: 
    """Binary search for index of target in probs."""
    if not probs:
        return 0
    
    left = 0
    right = len(probs)
    while left < right:
        mid = (left + right) // 2
        if probs[mid] < target:
            left = mid + 1
            continue
        right = mid
    return left
    

def main():

    data = sys.stdin.read().strip().split('\n')

    probs = list(map(int, data[0].split()))
    target = int(data[1])
    print(solve(probs, target))


if __name__ == '__main__':
    main()