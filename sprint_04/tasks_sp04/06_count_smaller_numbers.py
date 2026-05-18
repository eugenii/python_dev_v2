# A. Количество чисел, меньших, чем заданное

data = [int(i) for i in input().split()]

sorted_data = sorted(data)

for i in data:
    print(sorted_data.index(i))
