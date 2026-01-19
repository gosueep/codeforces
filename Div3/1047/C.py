# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        a,b = map(int, input().split())

        # if b is even - dump
        if b % 2 == 0:
            d = b // 2
            a = a*d
            b = 2
            if a % 2 == 0:
                total = a+b
            else:
                total = -1
        # if b is odd
        else:
            # if a is even, not doable
            if a % 2 == 0:
                total = -1
            else:
                total = a*b + 1

        print(total)
