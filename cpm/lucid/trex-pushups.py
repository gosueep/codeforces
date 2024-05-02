n = int(input())
arr = list(map(int, input().split()))

holes = 0
for i in range(n-1):
    if arr[i] - arr[i+1] >= 4:
        holes += 1
print(holes)