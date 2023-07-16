N = int(input())
A = list(map(int, input().split()))
dp = [0 for i in range(N)]

dp[1] = A[1] - A[0]
for i in range(2, N):
    dp[i] = min(dp[i-1] + abs(A[i]-A[i-1]), dp[i-2] + abs(A[i]-A[i-2]))

print(dp[-1])