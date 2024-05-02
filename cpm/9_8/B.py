# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N, m = map(int, input().split())
        arr = list(map(int, input().split()))
        if sum(arr) == m:
            print('YES')
        else:
            print('NO')
        