# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N, k = map(int, input().split())
        paper = input().strip()
        
        paints = 0
        i=0
        while i < N:
            if paper[i] == 'B':
                i += k
                paints += 1
            else:
                i += 1
        
        print(paints)
        