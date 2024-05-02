# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    length, N = map(int, input().strip().split())
    arr = list(map(int, input().split()))
    
    out = [0 for x in range(length)]
    
    for i in arr:
        out[i-1] += 1
    print(min(out))