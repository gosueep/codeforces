# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        n = int(input())

        print(' '.join([str(i+1) for i in range(n)]))
