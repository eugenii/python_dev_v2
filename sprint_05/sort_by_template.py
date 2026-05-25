# Сортировка по шаблону.
import sys


def solution(data: list) -> list:
    result = []
    containers = list(map(int, data[1].split()))
    template = list(map(int, data[3].split()))
    collection = {}
    for item in containers:
        collection[item] = collection.get(item, 0) + 1
    for item in template:
        if item in collection:
            result.extend([item] * collection[item])
            collection.pop(item)
    for item in sorted(collection.items()):
        result.extend([item[0]] * item[1])
    return result



if __name__ == "__main__":
    data = sys.stdin.read().splitlines()
    print(*solution(data))



