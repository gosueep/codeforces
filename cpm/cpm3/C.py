# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N, h = map(int, input().split())
        arr = list(map(int, input().split()))
        
        l,r = 0,int(1e20)

        while r-l > 1:
            k = (r+l) // 2
            
            dmg = 0
            p = -1
            for i in arr:
                newp = i+k
                if p > i:
                    dmg += newp-p
                else:
                    dmg += k
                p = newp

            if dmg >= h:
                r = k
            else:
                l = k
        print(r)
        
        