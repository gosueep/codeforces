# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        A = list(map(int, input().split()))
        
        A.sort()
        
        amt = N-1
        out = []
        i = 0
        # print(N)
        while i < len(A) and amt > 0:
            out.append(A[i])
            i += amt
            # print(i, out)
            amt -= 1
        
        out.append(A[-1])
        print(' '.join(str(x) for x in out))