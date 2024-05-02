d = {}
n = int(input())
for _ in range(n):
    species = input().strip()
    d[species] = [input().strip() for _ in range(int(input()))]

m = int(input())
for _ in range(m):
    atts = [input().strip() for _ in range(int(input()))]
    maxl = -1
    maxs = 'Possible New Discovery'
    best = []
    for s in d:
        count = 0
        noton = 0
        for a in atts:
            if a in d[s]: count += 1
            else: noton += 1
        l = 100 * (count - noton) / len(d[s])
        if l>50 or (50-l) < 0.0000001:
            best.append((s, l))
            if l>maxl:
                l = maxl
                maxs = s

    if len(best) == 0:
        print('Possible New Discovery')
    else:
        print(max(best, key=lambda x: x[1])[0])