# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        ropes = 0
        for _ in range(N):
            h, l = map(int, input().split())
            if h > l:
                ropes += 1

        print(ropes)