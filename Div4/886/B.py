# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        
        best = -1
        bestI = -1
        for i in range(N):
            length, qual = map(int, input().split())
            if length <= 10:
                if qual > best:
                    bestI = i+1
                    best = qual
        print(bestI)