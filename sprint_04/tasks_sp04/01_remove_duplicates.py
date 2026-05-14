# Удаление дубликатов.
import sys

data = sys.stdin.read().strip().split('\n')

n = int(data[0])
probs = list(map(int, data[1].split()))
probs.sort()
start_len = len(probs)
probs = set(probs)
duplicates = start_len - len(probs)
res = ''
for i in sorted(probs):
    res += str(i) + ' '
res += ('_ ') * duplicates
res.rstrip()
print(res)