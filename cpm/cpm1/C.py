# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        arr = list(map(int, input().split()))
        
        m = max(arr)
        b = []
        c = []
        for i in arr:
            if i == m:
                c.append(i)
            else:
                b.append(i)
        
        if len(b) ==0 or len(c) == 0:
            print(-1)
        else:
            print(len(b), len(c))
            print(' '.join(str(x) for x in b))
            print(' '.join(str(x) for x in c))