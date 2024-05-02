# from collections import defaultdict
import sys
input = sys.stdin.readline
from functools import lru_cache

@lru_cache(maxsize=None)
def fact(x):
    out = x
    for i in range(x-1, 0, -1):
        out = (out * i) % 998244353
    return out

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        
        out = 0
        if N % 2 == 0:
            out = pow(fact(N//2), 2, 998244353)
        
        print(out)