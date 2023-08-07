# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':   
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        alist = list(map(int, input().split()))
        blist = list(map(int, input().split()))
        
        even = False
        odd = False
        for i in range(N):
            ops = 0
            a, b = alist[i], blist[i] 
            while a != 0:
                c = abs(a-b)
                a, b = b, c
                ops += 1
            if ops % 2 == 0:
                even = True
            else:
                odd = True
            print(ops)
            # if even and odd:
            #     break
        print(even, odd)
        if even and odd:
            print('NO')
        else:
            print('YES')
        
        
            