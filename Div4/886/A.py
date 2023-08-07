# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        a,b,c = map(int, input().split())
        
        if a+b >= 10 or a+c >= 10 or b+c >= 10:
            print('YES')
        else:
            print('NO')
            