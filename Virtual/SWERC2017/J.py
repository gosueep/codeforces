n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

colors = [0, 0, 0]

colorIndex = 2

for start in range(n):
    i = start
    j = 0

    while 0<= i < n and 0 <= j < n:
        colors[colorIndex] += A[j] * B[i]
        i -= 1
        j += 1

    colorIndex = (colorIndex + 1) % 3

for start in range(1, n):
    i = n-1
    j = start

    while 0<= i < n and 0 <= j < n:
        colors[colorIndex] += A[j] * B[i]
        i -= 1
        j += 1
    colorIndex = (colorIndex + 1) % 3

for color in colors:
    print(color, end=' ')