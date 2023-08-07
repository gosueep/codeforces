# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        A = list(map(int, input().split()))
        
        sorted = True
        for i in range(1, N):
            if A[i] < A[i-1]:
                sorted = False
                break
        
        ops = 0
        if sorted:
            mindiff = 1e10
            for i in range(1,N):
                # for j in range(i+1, N):
                mindiff = min(mindiff, abs(A[i]-A[i-1]))
            ops = mindiff // 2 +1
            
        print(ops)