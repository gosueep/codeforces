W = int(input())
N = int(input())
total_area = 0
for i in range(N):
    w, l = map(int, input().split())
    total_area += w * l
print(total_area // W)

