n = int(input())

holes = set()
pos = {}
for _ in range(n):
    dino, hole = input().split()
    hole = int(hole)
    holes.add(hole)
    pos[dino] = hole

out = {}
for h in holes:
    out[h] = []
for dino in pos:
    out[pos[dino]].append(dino)

for h in sorted(holes):
    if h != 0:
        if len(out[h]) == 0:
            print(h, 'n/a')
        else:
            print(h, ' '.join(sorted(out[h])))
    
    