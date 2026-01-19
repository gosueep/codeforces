# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        p = list(map(int, input().split()))
        target = N+1
        q = [str(target - x) for x in p]
        print(' '.join(q))