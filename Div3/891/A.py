# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        A = map(int, input().split())
        
        odds, evens = 0,0
        for i in A:
            if i % 2 == 0:
                evens += 1
            else:
                odds += 1
        
        if odds % 2 == 0:
            print('YES')
        else:
            print('NO')