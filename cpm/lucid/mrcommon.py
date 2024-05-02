n = int(input())

p = {}
for _ in range(n):
    anc, des = input().split('--')
    p[des.strip()] = anc.strip()

one = input().strip()
two = input().strip()

s1 = set()
s2 = set()
while True:
    if one in p: one = p[one]
    if two in p: two = p[two]
    s1.add(one)
    s2.add(two)
    
    if one in s2:
        print(one)
        break
    if two in s1:
        print(two)
        break   