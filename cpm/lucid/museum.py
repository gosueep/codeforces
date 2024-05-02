from collections import defaultdict

n = int(input())

d = defaultdict(int)
for _ in range(n):
    for dino in input().split(','):
        d[dino] += 1

k = max(d, key=d.get)
print(k)
print(d[k])