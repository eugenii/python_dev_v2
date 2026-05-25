# Жадные алгоритмы. Камни с Марса.
import sys


def solution(stones, needed_masses):
    """Поиск максмального количества удовлетворённых лабораторий."""
    needed_masses.sort(reverse=True)
    stones.sort(reverse=True)
    res = 0
    pos_stone = 0
    for mass in needed_masses:
        if stones[pos_stone] >= mass:
            res += 1
            pos_stone += 1
            if pos_stone == len(stones):
                break

    return res


data = sys.stdin.read().splitlines()
orders = int(data[0])
needed_masses = list(map(int, data[1].split()))
number_of_stones = int(data[2])
stones = list(map(int, data[3].split()))
print(solution(stones, needed_masses))
