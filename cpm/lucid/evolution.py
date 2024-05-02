n,g,p0,p1,p2 = map(float, input().split())

for _ in range(int(n)):
    zero = (1-g)**2
    one = 2*(1-g)*(g)
    two = g**2
    
    g = zero*p0 + one*p1 + two*p2

print(g)
