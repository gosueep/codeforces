# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N, M, k = map(int, input().split())
        x, y = map(int, input().split())
        possible = True
        for _ in range(k):
            kx, ky = map(int, input().split())
            md = abs(kx-x) + abs(ky-y)
            if md % 2 == 0:
                possible = False
        
        if possible:
            print("YES")
        else:
            print("NO")
            