# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N, water = map(int, input().split())
        arr = list(map(int, input().split()))
        
        l,r=1, int(1e10)
        while r-l > 1:
            k = (r+l) // 2
            
            total = 0
            for i in arr:
                total += max(k - i, 0)

            if total > water:
                r = k
            else:
                l = k
        
        # print(l,r)
        print(l)
        