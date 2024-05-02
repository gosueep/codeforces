# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N, k = map(int, input().split())
        fruits = list(map(int, input().split()))
        heights = list(map(int, input().split()))
        
        best = 0
        dp = [[0,0] for _ in range(N)]
        dp[0] = [0,0]
        if fruits[0] <= k: 
            dp[0][0] = fruits[0]
            best = 1
        
        l=0
        total = 0
        for i in range(1,N):
            if heights[i-1] % heights[i] == 0:
                total += fruits[i]
                
                while total > k and l <= i:
                    total -= dp[l][0]
                    l += 1
                
                if l > i: l = i
                
                currlen = i-l + 1
                best = max(currlen, best)
            else:
                total = 0
            dp[i] = [total,l]
            
        print(dp)
        print(best)
            