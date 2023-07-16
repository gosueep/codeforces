usbs, ps2s, both = map(int, input().split())
M = int(input())
usb_mice = []
ps2_mice = []
for _ in range(M):
    cost, type = input().split()
    if type == 'USB':
        usb_mice.append(int(cost))
    elif type == 'PS/2':
        ps2_mice.append(int(cost))

amt, cost = 0, 0
both_mice = []

i = min(len(usb_mice), usbs)
amt += i
cost += sum(usb_mice[:i])
both_mice += usb_mice[i:]

i = min(len(ps2_mice), ps2s)
amt += i
cost += sum(ps2_mice[:i])
both_mice += ps2_mice[i:]

i = min(len(both_mice), both)
amt += i
cost += sum(both_mice[:i])
    
print(amt, cost)