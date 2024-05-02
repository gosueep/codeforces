# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N, k = map(int, input().split())
        arr = list(map(int, input().split()))
        
        for i in range(k):
            arr[i] = N - arr[i]
        arr.sort()
    
        total = 0
        m = 0
        for i in arr:
            if (total + i) > (N-1):
                break
            total += i
            m += 1

        print(m)
        
        