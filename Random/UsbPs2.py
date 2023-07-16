usbs, ps2s, both = map(int, input().split())
M = int(input())
mice = []
for _ in range(M):
    cost, type = input().split()
    mice.append((int(cost), type))
totalnum, totalcost = 0, 0
for cost, type in sorted(mice, key= lambda x: x[0]):

    if both == 0 and usbs == 0 and ps2s == 0:
        break

    if type == 'USB':
        if usbs > 0:
            totalcost += cost
            totalnum += 1
            usbs -= 1
        elif both > 0:
            totalcost += cost
            totalnum += 1
            both -= 1
    elif type == 'PS/2':
        if ps2s > 0:
            totalcost += cost
            totalnum += 1
            ps2s -= 1
        elif both > 0:
            totalcost += cost
            totalnum += 1
            both -= 1
    
print(totalnum, totalcost)