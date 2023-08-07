# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N, cardboard = map(int, input().split())
        lens = list(map(int, input().split()))
        a,b,c = 4*N, 0, -1*cardboard
        
        for i in lens:
            b += i
            c += i**2
        b *= 4
        
        # print(a,b,c)
        root = (b**2 - 4*a*c)**(1/2)
        # print(root)
        r1 = (-b + root) / (2*a)
        # r2 = (b + root) / (2*a)
        print(int(r1))