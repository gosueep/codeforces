# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        out = []
        for i in range(1,N//2+1):
            out += [i*2, i*2-1]
        if N % 2 != 0:
            out.insert(len(out)-1, N)
        print(' '.join(str(x) for x in out))