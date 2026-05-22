N, M, x, y = map(int, input().split())


head = (x - 1) * M - 1

if x % 2 != 0:
    tail = y
else:
    tail = M - y + 1

res = head + tail
print(res)