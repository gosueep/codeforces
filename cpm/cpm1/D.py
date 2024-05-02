# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        # N = int(input())
        arr = list(map(int, input().split()))
        
        a,b,c = arr
        # print(a,b,c)
        
        poss = False
        for x,y,z in [(a,b,c), (a,c,b), (b,c,a)]:
            if x == y and z%2 == 0:
                # print(x,y,z)
                poss = True
                break
            elif abs(x-y) == z:
                # print(x,y,z)
                # print(abs(x-y), z)
                poss = True
                break
        if poss:
            print("YES")
        else:
            print("NO")
        
        